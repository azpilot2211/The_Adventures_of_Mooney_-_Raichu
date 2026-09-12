"""Print a voiced/unvoiced timeline per clip, so you can see what a shot SAYS
without being able to hear it.

`pacing.py` answers "when does the line start". This answers "how many separate
utterances are in here, and where" - which is what catches Seedance padding a
short line with invented speech. A-2 "I will die before you eat again" shows six
voiced spans, one per word. A-8 "And?" showed two, 2.6s apart, and the second
one was never in the script.

    python speech_map.py clips/A-8_and.mp4=RAICHU clips/CO-2_carrier.mp4=MOONEY

Add --speech to gate on the 300-3400 Hz speech band instead of the character's
F0 range. Do that whenever the shot has engine rumble, gull cries, music or
anything else periodic: those register as voiced and will look like dialogue.
CO-2 appeared to hold four utterances until it was re-measured this way.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import voicecheck as V           # noqa: E402
from pacing import RANGE         # noqa: E402


def spans(path, who, speech_band=False, gate_frac=0.10):
    x = V.pcm(path)
    sr, FRAME, HOP = V.SR, V.FRAME, V.HOP
    if speech_band:
        import subprocess
        raw = subprocess.run(
            ['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(sr),
             '-af', 'highpass=f=300,lowpass=f=3400', '-f', 's16le', '-'],
            capture_output=True).stdout
        x = np.frombuffer(raw, dtype=np.int16).astype(np.float64) / 32768.0

    lo_hz, hi_hz = RANGE.get(who, (70, 480))
    lo, hi = sr // hi_hz, sr // lo_hz
    n = 1 << (2 * FRAME - 1).bit_length()
    win = np.hanning(FRAME)
    starts = range(0, len(x) - FRAME, HOP)
    rms = np.array([np.sqrt(np.mean(x[i:i + FRAME] ** 2)) for i in starts])
    gate = rms.max() * gate_frac

    marks = []
    for i, r in zip(starts, rms):
        ok = False
        if r >= gate:
            if speech_band:
                ok = True                      # band-limited energy is the test
            else:
                w = x[i:i + FRAME] * win
                S = np.fft.rfft(w, n)
                ac = np.fft.irfft(S * np.conj(S), n)[:FRAME]
                if ac[0] > 0:
                    seg = (ac / ac[0])[lo:hi]
                    ok = bool(seg.size and seg.max() >= 0.30)
        marks.append(ok)

    out, st = [], None
    for k, m in enumerate(marks):
        if m and st is None:
            st = k
        if not m and st is not None:
            if k - st >= 3:
                out.append((st * HOP / sr, k * HOP / sr))
            st = None
    if st is not None:
        out.append((st * HOP / sr, len(marks) * HOP / sr))
    return marks, out, len(x) / sr, HOP / sr


def report(path, who, speech_band=False):
    marks, sp, dur, hop = spans(path, who, speech_band)
    print('%-34s %-7s dur %.2fs%s'
          % (os.path.basename(path), who, dur, '  [speech band]' if speech_band else ''))
    print('   ' + ''.join('#' if m else '.' for m in marks)
          + '   (1 char = %.3fs)' % hop)
    for a, b in sp:
        print('   voiced %5.2f - %5.2f s  (%.2fs)' % (a, b, b - a))
    print('   %d utterance(s); last ends %.2fs before the clip does\n'
          % (len(sp), dur - (sp[-1][1] if sp else dur)))


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if a != '--speech']
    band = '--speech' in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)
    for arg in args:
        path, _, who = arg.partition('=')
        report(path, who or 'RAICHU', band)
