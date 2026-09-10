"""Find how long each dialogue shot waits before the character actually speaks.

Loudness alone is not enough: several shots open with a foley hit or ambience
before a long gap and then the line, so an RMS gate reports the wrong moment.
This looks for the first sustained run of VOICED frames - frames with a
detectable fundamental in the speaker's own pitch range - which is what
"when does the line start" actually means.
"""
import numpy as np
import voicecheck as V

# expected fundamental range per character, from the measured cast
RANGE = {
    'MOONEY': (70, 190), 'RAICHU': (200, 480), 'GERALD': (80, 200),
    'GARY': (70, 190), 'LYNDIE': (140, 320), 'GARY+MOONEY': (70, 320),
}


def voiced_onset(path, who, need=6):
    """Seconds until `need` consecutive voiced frames (~0.19s of speech)."""
    x = V.pcm(path)
    sr, FRAME, HOP = V.SR, V.FRAME, V.HOP
    if x.size < FRAME * 2:
        return None
    lo_hz, hi_hz = RANGE.get(who, (70, 480))
    lo, hi = sr // hi_hz, sr // lo_hz
    n = 1 << (2 * FRAME - 1).bit_length()
    win = np.hanning(FRAME)
    starts = list(range(0, len(x) - FRAME, HOP))
    rms = np.array([np.sqrt(np.mean(x[i:i + FRAME] ** 2)) for i in starts])
    if rms.max() < 1e-5:
        return None
    gate = rms.max() * 0.10
    run = 0
    for k, (i, r) in enumerate(zip(starts, rms)):
        ok = False
        if r >= gate:
            w = x[i:i + FRAME] * win
            S = np.fft.rfft(w, n)
            ac = np.fft.irfft(S * np.conj(S), n)[:FRAME]
            if ac[0] > 0:
                ac /= ac[0]
                seg = ac[lo:hi]
                if seg.size and seg.max() >= 0.30:
                    ok = True
        run = run + 1 if ok else 0
        if run >= need:
            return starts[k - need + 1] / sr
    return None


if __name__ == '__main__':
    import assemble
    rows = []
    for name, path in assemble.SEQ:
        who = V.SPEAKER.get(name)
        if not who:
            continue
        o = voiced_onset(path, who)
        if o is not None:
            rows.append((o, name, assemble.dur(path), who))
    print('%-30s %-7s %6s %9s' % ('shot', 'who', 'dur', 'voice@'))
    for o, name, d, who in sorted(rows, reverse=True):
        flag = '   <-- dead lead-in' if o > 1.2 else ''
        print('%-30s %-7s %5.2fs %8.2fs%s' % (name, who, d, o, flag))
    late = [r for r in rows if r[0] > 1.2]
    print('\n%d of %d dialogue shots wait over 1.2s before the line'
          % (len(late), len(rows)))
    print('trimming each to a 0.40s lead-in would recover %.1fs'
          % sum(r[0] - 0.40 for r in late))
