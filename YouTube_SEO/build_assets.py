"""Build the YouTube channel art set at YouTube's real specs.

  avatar   800x800   (renders as a 98px circle - must read tiny)
  banner   2048x1152 (safe area for text/logo is only 1235x338, centred)
  thumbs   1280x720  (must read as a 210px-wide phone thumbnail)
  watermark 150x150  transparent

Palette and paw motif match the logo, scene dividers and outro so the whole
channel reads as one brand.
"""
import math, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, 'images')
REF = os.path.join(BASE, '..', 'series', 'character-refs')
FONT = os.path.join(BASE, '..', 'ep02-chonk', 'font.ttf')

NAVY = (0, 0, 72)
NAVY_D = (0, 0, 48)
CREAM = (240, 240, 240)
GOLD = (240, 216, 120)
SKY = (120, 168, 216)

logo = Image.open(os.path.join(REF, 'logo-sticker.png')).convert('RGBA')


def F(sz):
    return ImageFont.truetype(FONT, sz)


def stripes(im, step=96, lean=200, col=NAVY, bgcol=NAVY_D):
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, im.width, im.height], fill=bgcol)
    k = -6
    while k * step < im.width + lean * 2:
        x = k * step
        d.polygon([(x + lean, -40), (x - lean, im.height + 40),
                   (x - lean - step * .45, im.height + 40), (x + lean - step * .45, -40)], fill=col)
        k += 1
    return im


def paw(d, cx, cy, s, fill, edge, wid):
    d.ellipse([cx - s * .62, cy - s * .42, cx + s * .62, cy + s * .72], fill=fill, outline=edge, width=wid)
    for ang, r in ((-148, .30), (-108, .31), (-72, .31), (-32, .30)):
        a = math.radians(ang)
        tx, ty = cx + math.cos(a) * s * .78, cy + math.sin(a) * s * .86
        d.ellipse([tx - s * r, ty - s * r * .9, tx + s * r, ty + s * r * .9], fill=fill, outline=edge, width=wid)


def fit_cover(im, w, h):
    r = max(w / im.width, h / im.height)
    im2 = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    return im2.crop(((im2.width - w) // 2, (im2.height - h) // 2,
                     (im2.width - w) // 2 + w, (im2.height - h) // 2 + h))


def outlined(d, xy, text, font, fill, edge, w, anchor='mm'):
    d.text(xy, text, font=font, fill=fill, anchor=anchor, stroke_width=w, stroke_fill=edge)


# ---------------------------------------------------------------- avatar A: paw roundel
def avatar_paw(path, S=800):
    im = Image.new('RGB', (S, S), NAVY_D)
    stripes(im, step=S // 8, lean=S // 5)
    d = ImageDraw.Draw(im)
    d.ellipse([S * .07, S * .07, S * .93, S * .93], outline=GOLD, width=int(S * .035))
    # No wordmark: at the 98px display size any text here turns to mush.
    # The paw alone is what has to be recognisable in a subscription feed.
    paw(d, S / 2, S * .52, S * .40, CREAM, NAVY, int(S * .014))
    im.save(path)


# ---------------------------------------------------------------- avatar B: Mooney's face
def avatar_face(path, S=800):
    src = Image.open(os.path.join(IMG, '_src_chonk.png')).convert('RGB')
    # tight crop on Mooney (left of frame in that shot)
    w, h = src.size
    box = (int(w * .10), int(h * .18), int(w * .55), int(h * .90))
    face = fit_cover(src.crop(box), S, S)
    im = Image.new('RGB', (S, S), NAVY_D)
    im.paste(face, (0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([S * .025, S * .025, S * .975, S * .975], outline=GOLD, width=int(S * .05))
    im.save(path)


# ---------------------------------------------------------------- banner
SAFE_W, SAFE_H = 1235, 338


def banner(path, guide_path=None, W=2048, H=1152):
    hero = Image.open(os.path.join(IMG, '_src_hero.png')).convert('RGB')
    im = fit_cover(hero, W, H)
    # push the photo back so the logo reads
    im = im.filter(ImageFilter.GaussianBlur(2.2))
    veil = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    vd = ImageDraw.Draw(veil)
    for y in range(H):                       # vertical darkening, strongest through the safe band
        c = abs(y - H / 2) / (H / 2)
        a = int(196 * (1 - c) ** 1.5) + 40
        vd.line([(0, y), (W, y)], fill=(0, 0, 40, min(235, a)))
    im = Image.alpha_composite(im.convert('RGBA'), veil).convert('RGB')

    # Size the wordmark by HEIGHT: the safe band is only 338px tall, so a
    # width-sized logo overflows it and phones crop the top off.
    lh = 196
    lg = logo.resize((int(lh * logo.width / logo.height), lh), Image.LANCZOS)
    top = H // 2 - SAFE_H // 2
    im.paste(lg, (W // 2 - lg.width // 2, top + 24), lg)

    d = ImageDraw.Draw(im)
    outlined(d, (W / 2, top + 24 + lh + 38), 'TWO CATS. ONE COUCH. ZERO REMORSE.',
             F(42), GOLD, (0, 0, 40), 6)
    outlined(d, (W / 2, top + 24 + lh + 84), 'new episodes every week',
             F(30), CREAM, (0, 0, 40), 5)
    im.save(path)

    if guide_path:
        g = im.copy()
        gd = ImageDraw.Draw(g)
        x0, y0 = W // 2 - SAFE_W // 2, H // 2 - SAFE_H // 2
        gd.rectangle([x0, y0, x0 + SAFE_W, y0 + SAFE_H], outline=(0, 255, 0), width=4)
        gd.text((x0 + 10, y0 + 8), 'SAFE ON ALL DEVICES 1235x338', font=F(30), fill=(0, 255, 0))
        gd.rectangle([W // 2 - 1138, 0, W // 2 + 1138, H], outline=(255, 200, 0), width=4)
        gd.text((W // 2 - 1130, 12), 'desktop 2276x1152', font=F(30), fill=(255, 200, 0))
        gd.rectangle([0, 0, W - 1, H - 1], outline=(255, 60, 60), width=6)
        gd.text((14, H - 46), 'TV / full upload 2048x1152', font=F(30), fill=(255, 60, 60))
        g.save(guide_path)


# ---------------------------------------------------------------- thumbnails
def thumb(path, src_name, word, ep, crop=None, word_col=GOLD, side='left'):
    src = Image.open(os.path.join(IMG, src_name)).convert('RGB')
    if crop:
        w, h = src.size
        src = src.crop((int(w * crop[0]), int(h * crop[1]), int(w * crop[2]), int(h * crop[3])))
    im = fit_cover(src, 1280, 720)
    d = ImageDraw.Draw(im)
    # contrast wedge behind the text
    veil = Image.new('RGBA', (1280, 720), (0, 0, 0, 0))
    vd = ImageDraw.Draw(veil)
    if side == 'left':
        vd.polygon([(0, 0), (700, 0), (520, 720), (0, 720)], fill=(0, 0, 40, 175))
    else:
        vd.polygon([(1280, 0), (600, 0), (780, 720), (1280, 720)], fill=(0, 0, 40, 175))
    im = Image.alpha_composite(im.convert('RGBA'), veil).convert('RGB')
    d = ImageDraw.Draw(im)
    cx = 300 if side == 'left' else 980

    f = F(150 if len(word) <= 6 else 104)
    outlined(d, (cx, 300), word, f, word_col, (0, 0, 40), 14)
    outlined(d, (cx, 415), 'MOONEY & RAICHU', F(44), CREAM, (0, 0, 40), 8)

    bw, bh = 190, 74                     # episode badge
    bx, by = cx - bw // 2, 470
    d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=18, fill=GOLD, outline=NAVY, width=5)
    outlined(d, (cx, by + bh / 2), ep, F(44), NAVY, NAVY, 0)
    paw(d, cx, 620, 54, CREAM, NAVY, 5)
    im.save(path)


def thumb_template(path):
    im = Image.new('RGB', (1280, 720), NAVY_D)
    stripes(im)
    d = ImageDraw.Draw(im)
    veil = Image.new('RGBA', (1280, 720), (0, 0, 0, 0))
    ImageDraw.Draw(veil).polygon([(0, 0), (700, 0), (520, 720), (0, 720)], fill=(0, 0, 40, 150))
    im = Image.alpha_composite(im.convert('RGBA'), veil).convert('RGB')
    d = ImageDraw.Draw(im)
    outlined(d, (300, 300), 'WORD', F(150), GOLD, (0, 0, 40), 14)
    outlined(d, (300, 415), 'MOONEY & RAICHU', F(44), CREAM, (0, 0, 40), 8)
    d.rounded_rectangle([205, 470, 395, 544], radius=18, fill=GOLD, outline=NAVY, width=5)
    outlined(d, (300, 507), 'EP 00', F(44), NAVY, NAVY, 0)
    paw(d, 300, 620, 54, CREAM, NAVY, 5)
    d.rectangle([64, 36, 1216, 684], outline=(0, 255, 0), width=3)
    d.text((72, 44), 'keep text inside this box - phones crop the edges', font=F(26), fill=(0, 255, 0))
    d.text((720, 660), 'drop episode still on the right half', font=F(30), fill=CREAM)
    im.save(path)


def watermark(path, S=150):
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([0, 0, S - 1, S - 1], fill=(0, 0, 72, 210))
    paw(d, S / 2, S / 2, S * .30, CREAM, NAVY, 3)
    im.save(path)


if __name__ == '__main__':
    avatar_paw(os.path.join(IMG, '01_avatar_paw_800x800.png'))
    avatar_face(os.path.join(IMG, '02_avatar_mooney_800x800.png'))
    banner(os.path.join(IMG, '03_banner_2048x1152.png'),
           os.path.join(IMG, '04_banner_SAFE-AREA-GUIDE.png'))
    thumb(os.path.join(IMG, '05_thumb_ep02_chonk.png'), '_src_chonk.png', 'CHONK', 'EP 2',
          crop=(.02, .02, .72, 1.0), side='right')
    thumb(os.path.join(IMG, '06_thumb_ep01_fowlplay.png'), '_src_gerald.png', 'FOWL PLAY', 'EP 1',
          side='left')
    thumb(os.path.join(IMG, '07_thumb_alt_ep02.png'), '_src_raichu.png', 'DIET', 'EP 2',
          side='right', word_col=CREAM)
    thumb_template(os.path.join(IMG, '08_thumbnail_TEMPLATE.png'))
    watermark(os.path.join(IMG, '09_watermark_150x150.png'))
    for f in sorted(os.listdir(IMG)):
        if f.startswith('_'):
            continue
        p = os.path.join(IMG, f)
        print('  %-40s %s  %.0f KB' % (f, Image.open(p).size, os.path.getsize(p) / 1024))
