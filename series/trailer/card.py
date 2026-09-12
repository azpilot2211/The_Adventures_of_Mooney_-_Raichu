"""Build the trailer's channel-reveal card locally. No credits.

The 30-second cut spends its whole budget on footage, so the reveal is a card
rather than a generated shot: the logo sticker drops in over the divider's navy
ground, the wordmark and the subscribe line type on under it, and a paw print
stamps the corner. Same palette as divider.py and the logo (navy #000048,
cream #f0f0f0, gold #f0d878) so it reads as part of the same channel.

    python card.py            -> clips/T-15_reveal.mp4

Text is drawn with PIL, not ffmpeg drawtext, because ffmpeg on Windows cannot
escape drive-letter colons inside a filtergraph (see HANDOFF tooling notes).
"""
import math
import os
import subprocess
import sys
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

W, H, FPS = 1280, 720, 24
DUR = 4.0
N = int(round(DUR * FPS))

NAVY_D = (0, 0, 48)
NAVY = (0, 0, 72)
CREAM = (240, 240, 240)
GOLD = (240, 216, 120)

FONT = os.path.join('..', '..', 'ep02-chonk', 'font.ttf')
LOGO = os.path.join('..', 'character-refs', 'logo-sticker.png')

# The logo sticker already reads "THE ADVENTURES OF MOONEY & RAICHU", so the
# card does not repeat it in type - only the two lines the logo does not say.
STRAP = 'NEW ADVENTURES  •  NEW MISCHIEF  •  NEW CHAOS'
CTA = 'SUBSCRIBE & JOIN THE ADVENTURE!'


def font(px):
    return ImageFont.truetype(FONT, px)


def centred(d, y, text, f, fill, shadow=NAVY_D):
    w = d.textbbox((0, 0), text, font=f)[2]
    x = (W - w) / 2
    d.text((x + 3, y + 3), text, font=f, fill=shadow)
    d.text((x, y), text, font=f, fill=fill)


def ground(d):
    d.rectangle([0, 0, W, H], fill=NAVY_D)
    for k in range(-4, 34):          # the divider's diagonal stripes
        sx = k * 96
        d.polygon([(sx + 400 * 0.38, -40), (sx - 400 * 0.38, H + 40),
                   (sx - 40 - 400 * 0.38, H + 40), (sx - 40 + 400 * 0.38, -40)],
                  fill=NAVY)


def ease_out_back(u):
    return 1 - (1 - u) ** 3 + (1 - u) ** 2 * math.sin(u * math.pi) * 0.35


def render(outdir):
    os.makedirs(outdir, exist_ok=True)
    logo = Image.open(LOGO).convert('RGBA')
    lw = int(W * 0.42)
    logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)

    f_strap = font(30)
    f_cta = font(42)

    for i in range(N):
        t = i / (N - 1)
        im = Image.new('RGB', (W, H), NAVY_D)
        d = ImageDraw.Draw(im)
        ground(d)

        # logo drops in over the first 0.45 of the card, with an overshoot
        u = min(1.0, t / 0.45)
        s = ease_out_back(u)
        lh = int(logo.height * max(0.05, s))
        lwid = int(logo.width * max(0.05, s))
        if lwid > 2:
            sc = logo.resize((lwid, lh), Image.LANCZOS)
            im.paste(sc, (int((W - lwid) / 2), int(H * 0.19 + (logo.height - lh) / 2)), sc)

        y = int(H * 0.19) + logo.height + 54
        if t > 0.50:
            centred(d, y, STRAP, f_strap, CREAM)
        if t > 0.66:
            # the CTA pulses so the eye lands on it last
            k = 0.5 + 0.5 * math.sin((t - 0.66) * 22)
            col = tuple(int(CREAM[j] + (GOLD[j] - CREAM[j]) * k) for j in range(3))
            centred(d, y + 62, CTA, f_cta, col)

        im.save('%s/%03d.png' % (outdir, i))
    return N


def audio(path):
    sr = 48000
    n = int(sr * DUR)
    t = np.arange(n) / sr
    rng = np.random.default_rng(41)
    mix = np.zeros(n)

    # a bright major arpeggio as the logo lands, then a warm pad under the text
    for k, (f0, tc) in enumerate([(523, 0.05), (659, 0.14), (784, 0.23), (1047, 0.32)]):
        kk = np.clip(t - tc, 0, None)
        note = np.sin(2 * np.pi * f0 * kk) * np.exp(-kk * 3.2) * 0.16
        note[t < tc] = 0
        mix += note
    pad = (np.sin(2 * np.pi * 131 * t) + 0.6 * np.sin(2 * np.pi * 196 * t)) * 0.05
    pad *= np.clip(t / 0.5, 0, 1) * np.clip((DUR - t) / 0.8, 0, 1)
    mix += pad
    # one soft impact on the logo landing
    tc = 0.32
    kk = np.clip(t - tc, 0, None)
    hit = (np.sin(2 * np.pi * 74 * kk) * np.exp(-kk * 17) * 0.55
           + rng.normal(0, 1, n) * np.exp(-kk * 70) * 0.18)
    hit[t < tc] = 0
    mix = np.clip(mix + hit, -1, 1) * 0.85

    st = np.stack([mix, mix], axis=1)
    with wave.open(path, 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((st * 32767).astype('<i2').tobytes())


if __name__ == '__main__':
    for p in (FONT, LOGO):
        if not os.path.exists(p):
            sys.exit('missing %s' % p)
    os.makedirs('clips', exist_ok=True)
    render('frames_card')
    audio('card.wav')
    out = 'clips/T-15_reveal.mp4'
    subprocess.run(['ffmpeg', '-y', '-v', 'error',
                    '-framerate', str(FPS), '-i', 'frames_card/%03d.png',
                    '-i', 'card.wav',
                    '-c:v', 'libx264', '-crf', '17', '-preset', 'medium',
                    '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                    '-shortest', out], check=True)
    print('built %s (%d frames, %.2fs)' % (out, N, DUR))
