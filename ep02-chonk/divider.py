"""Build the scene-divider bumper for The Adventures of Mooney & Raichu.

A diagonal sticker band sweeps across the frame carrying a paw print, in the
logo's own palette (navy / cream / gold) with the logo's white contour stroke.
It sweeps fully in and fully out, so cutting into and out of it reads as one
continuous wipe even though both cuts are hard.

Two variants (left-to-right, right-to-left) so consecutive dividers alternate
instead of looking copy-pasted.

Audio is synthesised: a noise whoosh that sweeps with the band, plus a soft
low thump on the covered frame.
"""
import math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw

W, H, FPS = 1280, 720, 24
DUR = 0.80
N = int(round(DUR * FPS))

NAVY = (0, 0, 72)
NAVY_D = (0, 0, 48)
CREAM = (240, 240, 240)
GOLD = (240, 216, 120)

BAND_W = int(W * 0.62)
SKEW = 0.38          # diagonal lean of the band edges


def band_poly(lead, y0, y1, skew=SKEW):
    """Quad for a diagonal-edged band whose leading edge is at x=lead."""
    dy = (y1 - y0) / 2.0
    return [(lead + dy * skew, y0), (lead - dy * skew, y1),
            (lead - BAND_W - dy * skew, y1), (lead - BAND_W + dy * skew, y0)]


def paw(d, cx, cy, s, fill, outline, wid):
    """A simple cat paw: main pad plus four toes."""
    d.ellipse([cx - s * 0.62, cy - s * 0.42, cx + s * 0.62, cy + s * 0.72],
              fill=fill, outline=outline, width=wid)
    for ang, r in ((-148, 0.30), (-108, 0.31), (-72, 0.31), (-32, 0.30)):
        a = math.radians(ang)
        tx, ty = cx + math.cos(a) * s * 0.78, cy + math.sin(a) * s * 0.86
        d.ellipse([tx - s * r, ty - s * r * 0.9, tx + s * r, ty + s * r * 0.9],
                  fill=fill, outline=outline, width=wid)


def render(outdir, rtl=False):
    """Navy card, always fully covering, with a cream sticker band sweeping across."""
    os.makedirs(outdir, exist_ok=True)
    for i in range(N):
        t = i / (N - 1)
        e = t * t * (3 - 2 * t)
        im = Image.new('RGB', (W, H), NAVY_D)
        d = ImageDraw.Draw(im)
        sk = -SKEW if rtl else SKEW
        # static diagonal stripes on the navy ground
        for k in range(-4, 34):
            sx = k * 96
            d.polygon([(sx + (H + 80) / 2 * sk, -40), (sx - (H + 80) / 2 * sk, H + 40),
                       (sx - 40 - (H + 80) / 2 * sk, H + 40), (sx - 40 + (H + 80) / 2 * sk, -40)],
                      fill=NAVY)
        # the travelling cream band, gold edged
        travel = e * (W + 1.3 * BAND_W) - 0.65 * BAND_W
        lead = (W - travel) if rtl else travel
        d.polygon(band_poly(lead + 10, -40, H + 40, sk), fill=GOLD)
        d.polygon(band_poly(lead, -40, H + 40, sk), fill=CREAM)
        cx = lead - BAND_W / 2.0
        if -260 < cx < W + 260:
            spin = (t - 0.5) * 30
            pim = Image.new('RGBA', (420, 420), (0, 0, 0, 0))
            paw(ImageDraw.Draw(pim), 210, 210, 168, NAVY, GOLD, 9)
            pim = pim.rotate(spin, resample=Image.BICUBIC)
            im.paste(pim, (int(cx - 210), int(H / 2 - 210)), pim)
        im.save('%s/%03d.png' % (outdir, i))
    return N


def audio(path, rtl=False):
    sr = 48000
    n = int(sr * DUR)
    t = np.arange(n) / sr
    rng = np.random.default_rng(7 if not rtl else 11)
    # whoosh: noise pushed through a sweeping one-pole bandpass-ish filter
    noise = rng.normal(0, 1, n)
    f = 300 + 2600 * np.sin(np.pi * np.clip(t / DUR, 0, 1)) ** 1.5
    y = np.zeros(n)
    lp = 0.0
    hp = 0.0
    for i in range(n):
        a = min(0.99, 2 * math.pi * f[i] / sr)
        lp += a * (noise[i] - lp)
        hp += (a * 0.25) * (lp - hp)
        y[i] = lp - hp
    env = np.sin(np.pi * np.clip(t / DUR, 0, 1)) ** 1.8
    y *= env * 0.5
    # soft thump as the band covers frame
    tc = DUR * 0.5
    k = np.clip((t - tc), 0, None)
    thump = np.sin(2 * np.pi * 82 * k) * np.exp(-k * 26) * 0.55
    thump[t < tc] = 0
    mix = np.clip(y + thump, -1, 1)
    mix *= 0.85
    st = np.stack([mix, mix], axis=1)
    import wave
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((st * 32767).astype('<i2').tobytes())


def build(tag, rtl):
    fr = 'qa/div_%s' % tag
    render(fr, rtl)
    audio('qa/div_%s.wav' % tag, rtl)
    out = 'clips/DIV-%s.mp4' % tag
    subprocess.run(['ffmpeg', '-y', '-v', 'error',
                    '-framerate', str(FPS), '-i', '%s/%%03d.png' % fr,
                    '-i', 'qa/div_%s.wav' % tag,
                    '-c:v', 'libx264', '-crf', '17', '-preset', 'medium',
                    '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                    '-shortest', out], check=True)
    print('built %s (%d frames, %.2fs)' % (out, N, DUR))


if __name__ == '__main__':
    build('L', False)
    build('R', True)
