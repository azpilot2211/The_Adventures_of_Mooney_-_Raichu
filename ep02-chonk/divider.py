"""Build the scene-divider bumper for The Adventures of Mooney & Raichu.

A diagonal sticker band sweeps across the frame carrying a paw print, in the
logo's own palette (navy / cream / gold) with the logo's white contour stroke.
It sweeps fully in and fully out, so cutting into and out of it reads as one
continuous wipe even though both cuts are hard.

Four variants, so eight dividers in one episode never repeat back to back:

  L, R  the sticker band sweeps across, left-to-right and right-to-left
  P     the paw stamps down out of the card with an overshoot and a ring
  S     five diagonal slats snap shut from alternating sides, like blinds

All four are 0.80s, cover the full frame throughout (an early version swept
the band over black and read as a dropout), and share the navy/cream/gold.

Audio is synthesised per design: a swept noise whoosh for the bands, an
impact and ring for the stamp, a run of clicks for the slats.
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


def ground(sk):
    """The navy card every variant sits on: dark ground, lighter diagonal stripes."""
    im = Image.new('RGB', (W, H), NAVY_D)
    d = ImageDraw.Draw(im)
    for k in range(-4, 34):
        sx = k * 96
        d.polygon([(sx + (H + 80) / 2 * sk, -40), (sx - (H + 80) / 2 * sk, H + 40),
                   (sx - 40 - (H + 80) / 2 * sk, H + 40), (sx - 40 + (H + 80) / 2 * sk, -40)],
                  fill=NAVY)
    return im, d


def stamp_paw(im, cx, cy, size, spin=0.0):
    """Paste a rotated paw centred on (cx, cy)."""
    if size < 4:
        return
    r = int(size * 1.3)
    pim = Image.new('RGBA', (2 * r, 2 * r), (0, 0, 0, 0))
    paw(ImageDraw.Draw(pim), r, r, size, NAVY, GOLD, max(3, int(size * 0.055)))
    if spin:
        pim = pim.rotate(spin, resample=Image.BICUBIC)
    im.paste(pim, (int(cx - r), int(cy - r)), pim)


def render(outdir, rtl=False):
    """Navy card, always fully covering, with a cream sticker band sweeping across."""
    os.makedirs(outdir, exist_ok=True)
    for i in range(N):
        t = i / (N - 1)
        e = t * t * (3 - 2 * t)
        sk = -SKEW if rtl else SKEW
        im, d = ground(sk)
        # the travelling cream band, gold edged
        travel = e * (W + 1.3 * BAND_W) - 0.65 * BAND_W
        lead = (W - travel) if rtl else travel
        d.polygon(band_poly(lead + 10, -40, H + 40, sk), fill=GOLD)
        d.polygon(band_poly(lead, -40, H + 40, sk), fill=CREAM)
        cx = lead - BAND_W / 2.0
        if -260 < cx < W + 260:
            stamp_paw(im, cx, H / 2, 168, (t - 0.5) * 30)
        im.save('%s/%03d.png' % (outdir, i))
    return N


def render_stamp(outdir):
    """A cream disc drops in, overshoots, settles, and throws one gold ring."""
    os.makedirs(outdir, exist_ok=True)
    R = H * 0.40
    for i in range(N):
        t = i / (N - 1)
        im, d = ground(SKEW)
        # ease-out-back: lands at 0.45 of the shot, overshoots, settles
        u = min(1.0, t / 0.45)
        s = 1 - (1 - u) ** 3
        scale = s * 1.0 + (1 - u) ** 2 * math.sin(u * math.pi) * 0.55   # bounce
        rr = R * (0.15 + 0.85 * scale) if t < 0.45 else R
        cx, cy = W / 2.0, H / 2.0
        d.ellipse([cx - rr - 9, cy - rr - 9, cx + rr + 9, cy + rr + 9], fill=GOLD)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=CREAM)
        stamp_paw(im, cx, cy, rr * 0.58, (1 - u) * 22)
        # the impact ring expands away after the landing
        if t > 0.45:
            k = (t - 0.45) / 0.55
            ring = R * (1.05 + k * 1.3)
            wid = max(2, int(16 * (1 - k)))
            if wid > 2:
                ImageDraw.Draw(im).ellipse(
                    [cx - ring, cy - ring, cx + ring, cy + ring], outline=GOLD, width=wid)
        im.save('%s/%03d.png' % (outdir, i))
    return N


def render_slats(outdir):
    """Five diagonal slats snap shut from alternating sides, like blinds closing."""
    os.makedirs(outdir, exist_ok=True)
    K = 5
    sh = H / float(K)
    for i in range(N):
        t = i / (N - 1)
        im, d = ground(SKEW)
        for k in range(K):
            # each slat starts 0.055s after the one above it
            u = max(0.0, min(1.0, (t - k * 0.09) / 0.55))
            e = 1 - (1 - u) ** 3
            if e <= 0:
                continue
            y0, y1 = k * sh - 2, (k + 1) * sh + 2
            span = W + 120
            if k % 2:                                    # from the right
                x0, x1 = W + 60 - span * e, W + 60
            else:                                        # from the left
                x0, x1 = -60, -60 + span * e
            dy = (y1 - y0) / 2.0
            quad = [(x1 + dy * SKEW, y0), (x1 - dy * SKEW, y1),
                    (x0 - dy * SKEW, y1), (x0 + dy * SKEW, y0)]
            d.polygon([(x + (10 if k % 2 else -10), y) for x, y in quad], fill=GOLD)
            d.polygon(quad, fill=CREAM)
        # the paw lands on the closed blind at the end
        u = max(0.0, min(1.0, (t - 0.62) / 0.30))
        if u > 0:
            stamp_paw(im, W / 2.0, H / 2.0, (1 - (1 - u) ** 3) * H * 0.21)
        im.save('%s/%03d.png' % (outdir, i))
    return N


def _write(path, mix):
    st = np.stack([mix, mix], axis=1)
    import wave
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(48000)
        w.writeframes((st * 32767).astype('<i2').tobytes())


def audio_stamp(path):
    """One dry impact where the disc lands, plus a short gold ring after it."""
    sr = 48000
    n = int(sr * DUR)
    t = np.arange(n) / sr
    rng = np.random.default_rng(23)
    tc = DUR * 0.45
    k = np.clip(t - tc, 0, None)
    hit = (np.sin(2 * np.pi * 68 * k) * np.exp(-k * 19) * 0.80
           + rng.normal(0, 1, n) * np.exp(-k * 60) * 0.30)
    ring = (np.sin(2 * np.pi * 1180 * k) + 0.5 * np.sin(2 * np.pi * 1790 * k)) \
        * np.exp(-k * 9) * 0.14
    body = hit + ring
    body[t < tc] = 0
    # a short rise into the landing so the cut in does not feel abrupt
    rise = np.clip(t / tc, 0, 1) ** 3 * rng.normal(0, 1, n) * 0.12
    rise[t >= tc] = 0
    _write(path, np.clip(body + rise, -1, 1) * 0.85)


def audio_slats(path):
    """Five wooden clicks in sequence, then the paw's soft thump."""
    sr = 48000
    n = int(sr * DUR)
    t = np.arange(n) / sr
    rng = np.random.default_rng(29)
    mix = np.zeros(n)
    for i in range(5):
        tc = 0.055 + i * 0.09
        k = np.clip(t - tc, 0, None)
        click = (np.sin(2 * np.pi * (340 + 55 * i) * k) * np.exp(-k * 85)
                 + rng.normal(0, 1, n) * np.exp(-k * 150) * 0.55) * 0.42
        click[t < tc] = 0
        mix += click
    tc = 0.62
    k = np.clip(t - tc, 0, None)
    thump = np.sin(2 * np.pi * 76 * k) * np.exp(-k * 22) * 0.62
    thump[t < tc] = 0
    _write(path, np.clip(mix + thump, -1, 1) * 0.85)


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


BUILDERS = {
    'L': (lambda fr: render(fr, False), lambda w: audio(w, False)),
    'R': (lambda fr: render(fr, True),  lambda w: audio(w, True)),
    'P': (render_stamp, audio_stamp),
    'S': (render_slats, audio_slats),
}


def build(tag, rtl=None):
    frames, snd = BUILDERS[tag]
    fr = 'qa/div_%s' % tag
    frames(fr)
    snd('qa/div_%s.wav' % tag)
    out = 'clips/DIV-%s.mp4' % tag
    subprocess.run(['ffmpeg', '-y', '-v', 'error',
                    '-framerate', str(FPS), '-i', '%s/%%03d.png' % fr,
                    '-i', 'qa/div_%s.wav' % tag,
                    '-c:v', 'libx264', '-crf', '17', '-preset', 'medium',
                    '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                    '-shortest', out], check=True)
    print('built %s (%d frames, %.2fs)' % (out, N, DUR))


if __name__ == '__main__':
    for tag in (sys.argv[1:] or sorted(BUILDERS)):
        build(tag)
