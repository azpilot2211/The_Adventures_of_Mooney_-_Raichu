"""End-card outro: a cat paw presses LIKE and SUBSCRIBE.

Same navy/cream/gold sticker language as the scene dividers, and the same paw,
so the three brand elements (logo plaque, divider, outro) read as one system.
Text is drawn with PIL from the show font, which is reliable - unlike asking
the video model to render letters.
"""
import math, os, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1280, 720, 24
DUR = 5.0
N = int(round(DUR * FPS))

NAVY = (0, 0, 72)
NAVY_D = (0, 0, 48)
CREAM = (240, 240, 240)
GOLD = (240, 216, 120)
RED = (220, 40, 40)
GREY = (120, 120, 130)
FONT = 'font.ttf'

# beat timing (seconds)
T_BTN_IN   = 0.35
T_LIKE_HIT = 1.55
T_SUB_HIT  = 2.75
T_BELL     = 3.35

LIKE_C = (430, 430)
SUB_C  = (858, 430)
BTN_W, BTN_H = 330, 108


def ease_out_back(u, s=1.7):
    u = max(0.0, min(1.0, u))
    return 1 + (s + 1) * (u - 1) ** 3 + s * (u - 1) ** 2


def bg(d):
    d.rectangle([0, 0, W, H], fill=NAVY_D)
    for k in range(-4, 34):
        x = k * 96
        d.polygon([(x + 200, -40), (x - 200, H + 40),
                   (x - 240, H + 40), (x + 160, -40)], fill=NAVY)


def rrect(d, box, r, fill, outline=None, width=0):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def thumb(d, cx, cy, s, fill, edge):
    """Simple thumbs-up glyph."""
    d.rounded_rectangle([cx - s * 0.95, cy - s * 0.15, cx - s * 0.35, cy + s * 0.95],
                        radius=int(s * 0.14), fill=fill, outline=edge, width=3)
    d.rounded_rectangle([cx - s * 0.30, cy - s * 0.20, cx + s * 0.95, cy + s * 0.95],
                        radius=int(s * 0.22), fill=fill, outline=edge, width=3)
    d.polygon([(cx - s * 0.28, cy - s * 0.18), (cx + s * 0.10, cy - s * 1.05),
               (cx + s * 0.42, cy - s * 0.92), (cx + s * 0.26, cy - s * 0.18)],
              fill=fill, outline=edge)


def paw(d, cx, cy, s, fill, edge, wid):
    d.ellipse([cx - s * .62, cy - s * .42, cx + s * .62, cy + s * .72],
              fill=fill, outline=edge, width=wid)
    for ang, r in ((-148, .30), (-108, .31), (-72, .31), (-32, .30)):
        a = math.radians(ang)
        tx, ty = cx + math.cos(a) * s * .78, cy + math.sin(a) * s * .86
        d.ellipse([tx - s * r, ty - s * r * .9, tx + s * r, ty + s * r * .9],
                  fill=fill, outline=edge, width=wid)


def bell(d, cx, cy, s, tilt, fill, edge):
    """Notification bell: dome, flared body, rim bar, clapper."""
    side = int(s * 5)
    im = Image.new('RGBA', (side, side), (0, 0, 0, 0))
    dd = ImageDraw.Draw(im)
    o = side // 2
    top = o - s * 0.75
    dd.ellipse([o - s * 0.13, top - s * 0.42, o + s * 0.13, top - s * 0.14],
               fill=fill, outline=edge, width=3)                      # button on top
    dd.pieslice([o - s * 0.70, top - s * 0.10, o + s * 0.70, top + s * 1.30],
                180, 360, fill=fill, outline=edge, width=3)           # dome
    dd.polygon([(o - s * 0.70, top + s * 0.60), (o + s * 0.70, top + s * 0.60),
                (o + s * 0.95, top + s * 1.15), (o - s * 0.95, top + s * 1.15)],
               fill=fill, outline=edge)                               # flare
    dd.rounded_rectangle([o - s * 1.05, top + s * 1.10, o + s * 1.05, top + s * 1.36],
                         radius=int(s * 0.13), fill=fill, outline=edge, width=3)  # rim
    dd.ellipse([o - s * 0.20, top + s * 1.42, o + s * 0.20, top + s * 1.82],
               fill=fill, outline=edge, width=3)                      # clapper
    return im.rotate(tilt, resample=Image.BICUBIC, center=(o, int(top - s * 0.2)))


def build_frames(outdir, logo):
    os.makedirs(outdir, exist_ok=True)
    f_big = ImageFont.truetype(FONT, 52)
    f_sub = ImageFont.truetype(FONT, 46)
    f_tag = ImageFont.truetype(FONT, 34)
    for i in range(N):
        t = i / FPS
        im = Image.new('RGB', (W, H), NAVY_D)
        d = ImageDraw.Draw(im)
        bg(d)

        # logo plaque, small, top
        lw = int(W * 0.34)
        lg = logo.resize((lw, int(lw * logo.height / logo.width)), Image.LANCZOS)
        ly = 62
        pop = ease_out_back(min(1.0, t / 0.45))
        if pop > 0.01:
            sw = max(1, int(lg.width * pop)); sh = max(1, int(lg.height * pop))
            im.paste(lg.resize((sw, sh), Image.LANCZOS),
                     (W // 2 - sw // 2, ly + (lg.height - sh) // 2), lg.resize((sw, sh), Image.LANCZOS))

        liked = t >= T_LIKE_HIT
        subbed = t >= T_SUB_HIT

        for (cx, cy), kind in ((LIKE_C, 'like'), (SUB_C, 'sub')):
            delay = T_BTN_IN + (0.0 if kind == 'like' else 0.12)
            u = (t - delay) / 0.45
            if u <= 0:
                continue
            sc = ease_out_back(min(1.0, u))
            hit = T_LIKE_HIT if kind == 'like' else T_SUB_HIT
            if 0 <= t - hit < 0.14:            # squash on press
                sc *= 0.90
            bw, bh = BTN_W * sc, BTN_H * sc
            box = [cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2]
            if kind == 'like':
                fill = GOLD if liked else CREAM
                rrect(d, box, int(bh * 0.30), fill, NAVY, 5)
                if sc > 0.6:
                    thumb(d, cx - bw * 0.26, cy - bh * 0.02, bh * 0.26, NAVY, NAVY)
                    d.text((cx + bw * 0.10, cy), 'LIKE', font=f_big, fill=NAVY, anchor='mm')
            else:
                fill = GREY if subbed else RED
                rrect(d, box, int(bh * 0.30), fill, CREAM, 5)
                if sc > 0.6:
                    d.text((cx, cy), 'SUBSCRIBED' if subbed else 'SUBSCRIBE',
                           font=f_sub, fill=CREAM, anchor='mm')

        # burst when the like lands
        if 0 <= t - T_LIKE_HIT < 0.45:
            u = (t - T_LIKE_HIT) / 0.45
            for k in range(9):
                a = math.radians(k * 40 - 90)
                rr = 70 + u * 130
                px, py = LIKE_C[0] + math.cos(a) * rr, LIKE_C[1] + math.sin(a) * rr
                s = max(1, int(11 * (1 - u)))
                d.ellipse([px - s, py - s, px + s, py + s], fill=GOLD)

        # bell, appears after subscribe
        if t >= T_BELL:
            u = t - T_BELL
            tilt = math.sin(u * 22) * 20 * math.exp(-u * 1.7)
            bim = bell(d, 0, 0, 54, tilt, GOLD, NAVY)
            im.paste(bim, (W // 2 - bim.width // 2, 572 - bim.height // 2), bim)

        # paw travels: offscreen -> like -> subscribe -> offscreen
        keys = [(0.95, (W + 240, H + 200)), (T_LIKE_HIT - 0.05, (LIKE_C[0] + 40, LIKE_C[1] + 96)),
                (T_LIKE_HIT + 0.30, (LIKE_C[0] + 40, LIKE_C[1] + 128)),
                (T_SUB_HIT - 0.05, (SUB_C[0] + 40, SUB_C[1] + 96)),
                (T_SUB_HIT + 0.30, (SUB_C[0] + 40, SUB_C[1] + 128)),
                (T_SUB_HIT + 1.05, (W + 240, H + 220))]
        px = py = None
        for (t0, p0), (t1, p1) in zip(keys, keys[1:]):
            if t0 <= t <= t1:
                u = (t - t0) / max(1e-6, t1 - t0)
                u = u * u * (3 - 2 * u)
                px = p0[0] + (p1[0] - p0[0]) * u
                py = p0[1] + (p1[1] - p0[1]) * u
                break
        if px is None and t < keys[0][0]:
            px, py = keys[0][1]
        if px is not None and px < W + 200:
            press = 0.0
            for hit in (T_LIKE_HIT, T_SUB_HIT):
                if 0 <= t - hit < 0.14:
                    press = 16
            pim = Image.new('RGBA', (300, 300), (0, 0, 0, 0))
            paw(ImageDraw.Draw(pim), 150, 150, 96, CREAM, NAVY, 7)
            pim = pim.rotate(-24, resample=Image.BICUBIC)
            im.paste(pim, (int(px - 150), int(py - 150 + press)), pim)

        d.text((W // 2, 668), 'new episodes every week', font=f_tag, fill=GOLD, anchor='mm')
        im.save('%s/%03d.png' % (outdir, i))
    return N


def audio(path):
    sr = 48000
    n = int(sr * DUR)
    t = np.arange(n) / sr
    y = np.zeros(n)

    def click(at, f, amp, dec):
        k = np.clip(t - at, 0, None)
        m = (t >= at)
        y[m] += (np.sin(2 * np.pi * f * k) * np.exp(-k * dec) * amp)[m]

    def chime(at, f, amp):
        for h, a in ((1, 1.0), (2, .5), (3, .25)):
            click(at, f * h, amp * a, 5.5)

    # warm sustained pad so the outro is never dead air, and it feels like an ending
    pad_env = np.clip(np.minimum(t / 0.5, (DUR - t) / 0.9), 0, 1) ** 1.2
    for f, a in ((196.0, .085), (261.6, .065), (392.0, .045), (523.3, .028)):
        y += np.sin(2 * np.pi * f * t + f) * a * pad_env
    y += np.sin(2 * np.pi * 98.0 * t) * .05 * pad_env          # low body

    click(T_BTN_IN, 520, .18, 30)
    click(T_BTN_IN + .12, 620, .18, 30)
    click(T_LIKE_HIT, 300, .34, 26)      # press
    chime(T_LIKE_HIT + .05, 880, .20)
    click(T_SUB_HIT, 280, .34, 26)
    chime(T_SUB_HIT + .05, 1046, .22)
    for k in range(4):                    # bell shimmer
        chime(T_BELL + k * .16, 1320, .10)
    y = np.clip(y, -1, 1) * .85
    st = np.stack([y, y], 1)
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((st * 32767).astype('<i2').tobytes())


if __name__ == '__main__':
    logo = Image.open('../series/character-refs/logo-sticker.png').convert('RGBA')
    build_frames('qa/outro_fr', logo)
    audio('qa/outro.wav')
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-framerate', str(FPS),
                    '-i', 'qa/outro_fr/%03d.png', '-i', 'qa/outro.wav',
                    '-c:v', 'libx264', '-crf', '17', '-preset', 'medium',
                    '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                    '-shortest', 'clips/OUTRO_like-subscribe.mp4'], check=True)
    print('built clips/OUTRO_like-subscribe.mp4  (%d frames, %.1fs)' % (N, DUR))
