"""Lay the narrator's seven lines onto one track timed to the cut.

The TTS clips come back padded with silence either side and at wildly
different lengths, so each is trimmed to its speech before placement.
CUES are seconds into the assembled trailer - keep them in step with the
IN/OUT table in assemble.py, and re-check them whenever a shot's length
changes. Nothing is placed between 15.1s and 30.4s: that stretch is the four
character lines and the narrator stays out of it.

Voice: Sterling (preset dc382508-c8bd-443c-8cb2-46e57b8d2e6f), 0.1 credits a
line. Chosen unheard - swap the id and re-run if the owner prefers another
from series/VOICES.html.

    python narration.py    -> narration.wav, picked up by assemble.py
"""
import os
import subprocess
import wave

import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

SR = 48000
TOTAL = 35.2          # a little past the end of the cut
DUCK = 0.62           # narration sits under the shot audio, not over it

# (file, cue seconds, what it says - for the next person reading the cut)
CUES = [
    ('narr/1.wav',  0.50, 'Meet Moonie.'),
    ('narr/2.wav',  3.00, 'He likes the simple things in life.'),
    ('narr/3.wav',  6.90, 'And this... is Rye-choo.'),
    ('narr/4.wav',  9.70, 'Two cats.'),
    ('narr/5.wav', 11.00, 'One home.'),
    ('narr/6.wav', 12.50, "And absolutely no idea what they're doing."),
    ('narr/7.wav', 30.50, 'The Adventures of Moonie and Rye-choo.'),
]


def pcm(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1',
                          '-ar', str(SR), '-f', 's16le', '-'],
                         capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float64) / 32768.0


def trim_silence(x, frac=0.06, pad=0.05):
    """Cut the dead air the TTS pads onto both ends."""
    w = int(0.01 * SR)
    n = len(x) // w
    r = np.array([np.sqrt(np.mean(x[i * w:(i + 1) * w] ** 2)) for i in range(n)])
    if r.max() <= 0:
        return x
    on = r > r.max() * frac
    idx = np.flatnonzero(on)
    if not idx.size:
        return x
    a = max(0, (idx[0] * w) - int(pad * SR))
    b = min(len(x), ((idx[-1] + 1) * w) + int(pad * SR))
    return x[a:b]


def main():
    track = np.zeros(int(TOTAL * SR))
    print('%-44s %6s %6s' % ('line', 'cue', 'len'))
    for path, cue, text in CUES:
        x = trim_silence(pcm(path))
        # short fades so a hard TTS start does not click
        f = int(0.02 * SR)
        x[:f] *= np.linspace(0, 1, f)
        x[-f:] *= np.linspace(1, 0, f)
        i = int(cue * SR)
        end = min(len(track), i + len(x))
        track[i:end] += x[:end - i] * DUCK
        print('%-44s %5.2fs %5.2fs' % (text, cue, len(x) / SR))

    peak = np.max(np.abs(track))
    if peak > 0.98:
        track *= 0.98 / peak
    st = np.stack([track, track], axis=1)
    with wave.open('narration.wav', 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((st * 32767).astype('<i2').tobytes())
    print('\nnarration.wav  %.2fs  peak %.2f' % (TOTAL, peak))

    # overlap check - two lines on top of each other is the one failure mode here
    spans = []
    for path, cue, text in CUES:
        spans.append((cue, cue + len(trim_silence(pcm(path))) / SR, text))
    for (a1, b1, t1), (a2, b2, t2) in zip(spans, spans[1:]):
        if b1 > a2:
            print('OVERLAP: "%s" ends %.2fs, "%s" starts %.2fs' % (t1, b1, t2, a2))


if __name__ == '__main__':
    main()
