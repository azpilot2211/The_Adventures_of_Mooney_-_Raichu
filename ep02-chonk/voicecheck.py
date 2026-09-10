"""Measure per-shot voice character so drifting performances can be found without ears.

For every shot that carries dialogue we estimate the speaker's pitch (median F0 via
autocorrelation over voiced frames) and brightness (spectral centroid). A character
whose voice is consistent should cluster; an outlier shot is a re-cast.
"""
import subprocess, sys, json
import numpy as np

SR = 16000
FRAME = 1024        # 64 ms
HOP = 512
FMIN, FMAX = 70, 450

# who speaks in which shot (from chonk.html)
SPEAKER = {
    'CO-1_v2_vet-exit': 'LYNDIE', 'CO-2_carrier': 'MOONEY', 'CO-4_carrier-again': 'MOONEY',
    'CO-5_the-portion': 'MOONEY',
    'A-1_v2_keep-an-eye': 'LYNDIE', 'A-2_i-will-die': 'RAICHU', 'A-3_she-meant-generally': 'MOONEY',
    'A-4_never-given-a-job': 'RAICHU', 'A-5_lots-of-jobs': 'MOONEY', 'A-6_name-one': 'RAICHU',
    'A-7_watch-the-door': 'MOONEY', 'A-8_and': 'RAICHU', 'A-9_raccoon-lives-here': 'MOONEY',
    'A-10_gary-morning': 'GARY', 'A-11_garys-fine': 'RAICHU', 'A-12_never-been-hungry': 'MOONEY',
    'B-1_ive-been-reading': 'RAICHU', 'B-2_you-cant-read': 'MOONEY',
    'B-3_deciding-what-they-say': 'RAICHU', 'B-4_where-did-you-get-lasers': 'MOONEY',
    'B-5_the-drawer': 'RAICHU', 'B-6_no-laser-drawer': 'MOONEY', 'B-7_i-made-one': 'RAICHU',
    'B-8_who-here-is-tired': 'RAICHU', 'B-10_nobodys-told-you': 'RAICHU',
    'B-12_im-going-to-tell-you': 'RAICHU',
    'C-3_what-do-you-have': 'MOONEY', 'C-4_half-a-sandwich': 'GERALD',
    'C-5_what-do-you-want': 'MOONEY', 'C-6_everything-you-own': 'GERALD',
    'C-7_i-own-a-bowl': 'MOONEY', 'C-8_then-i-want-the-bowl': 'GERALD',
    'C-11_disappointed': 'GARY', 'C-12_nobody-asked-you-gary': 'MOONEY',
    'D-2_wheres-your-bowl': 'RAICHU', 'D-3_what-bowl': 'MOONEY',
    'D-4_you-had-a-bowl': 'RAICHU', 'D-5_did-i': 'MOONEY',
    'E-1_i-wanted-to-help': 'RAICHU', 'E-2_i-know': 'MOONEY',
    'E-3_i-learned-something': 'MOONEY', 'E-4_thats-not': 'RAICHU',
    'E-5_id-do-it-again': 'MOONEY',
    'TZ-1_FINAL_gary-moves-in': 'GARY+MOONEY',
}


def pcm(path):
    raw = subprocess.run(
        ['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR),
         '-f', 's16le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float64) / 32768.0


def analyse(x):
    """median F0 over voiced frames, and spectral centroid.

    The gate is adaptive: many shots are short and quiet, so a fixed RMS
    threshold rejected almost everything. We take the loudest ~35% of frames
    and accept any with a clear autocorrelation peak.
    """
    if x.size < FRAME * 2:
        return None, None, 0
    win = np.hanning(FRAME)
    lo, hi = SR // FMAX, SR // FMIN
    n = 1 << (2 * FRAME - 1).bit_length()
    freqs = np.fft.rfftfreq(n, 1 / SR)[:FRAME // 2]

    starts = list(range(0, len(x) - FRAME, HOP))
    rms = np.array([np.sqrt(np.mean(x[i:i + FRAME] ** 2)) for i in starts])
    if rms.max() < 1e-5:
        return None, None, 0
    gate = max(np.percentile(rms, 65), rms.max() * 0.12)

    f0s, cents = [], []
    for i, r in zip(starts, rms):
        if r < gate:
            continue
        w = x[i:i + FRAME] * win
        S = np.fft.rfft(w, n)
        ac = np.fft.irfft(S * np.conj(S), n)[:FRAME]
        if ac[0] <= 0:
            continue
        ac /= ac[0]
        seg = ac[lo:hi]
        if seg.size == 0:
            continue
        k = int(np.argmax(seg))
        if seg[k] < 0.22:
            continue
        f0s.append(SR / float(lo + k))
        mag = np.abs(S[:FRAME // 2])
        if mag.sum() > 0:
            cents.append(float((freqs * mag).sum() / mag.sum()))
    cen = float(np.median(cents)) if cents else None
    if len(f0s) < 3:
        return None, cen, len(f0s)
    return float(np.median(f0s)), cen, len(f0s)


def main():
    import assemble
    rows = []
    for name, path in assemble.SEQ:
        who = SPEAKER.get(name)
        if not who:
            continue
        f0, cen, n = analyse(pcm(path))
        rows.append(dict(shot=name, who=who, f0=f0, centroid=cen, frames=n))

    by = {}
    for r in rows:
        by.setdefault(r['who'], []).append(r)

    for who in ['MOONEY', 'RAICHU', 'GERALD', 'GARY', 'LYNDIE', 'GARY+MOONEY']:
        rs = [r for r in by.get(who, []) if r['f0']]
        if not rs:
            continue
        f0s = np.array([r['f0'] for r in rs])
        med = np.median(f0s)
        print('\n%s  -  %d shots, median F0 %.0f Hz' % (who, len(rs), med))
        print('   %-32s %8s %8s %10s %6s' % ('shot', 'F0 Hz', 'dev', 'centroid', 'n'))
        for r in sorted(rs, key=lambda r: -abs(r['f0'] - med)):
            dev = r['f0'] - med
            flag = '   <-- OUTLIER' if abs(dev) > 0.18 * med else ''
            print('   %-32s %8.0f %+8.0f %10.0f %6d%s'
                  % (r['shot'], r['f0'], dev, r['centroid'] or 0, r['frames'], flag))
        missing = [r['shot'] for r in by.get(who, []) if not r['f0']]
        if missing:
            print('   (no reliable pitch: %s)' % ', '.join(missing))

    json.dump(rows, open('qa/voicecheck.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
