"""Assemble the channel trailer.

Same audio spine as ep02-chonk/assemble.py - per-clip loudness matching with a
clamp, a true-peak guard, a pink-noise floor so nothing drops to digital
silence, and a limiter on the master - because the raw clips land anywhere
between -12 and -40 LUFS and Seedance never supplies room tone.

What differs is the cutting. An episode lets a shot breathe; a trailer cuts on
the beat and gets out, so every entry here carries an explicit IN and OUT
measured off the clip rather than a head trim alone.

Two shots the content filter would not pass, after two rewordings each
(T-4 Raichu's reveal, T-12 Mooney settling back down):
  * Raichu is introduced by the crouch instead, which is the better shot.
  * The "peaceful again" beat REUSES T-1, so the trailer returns to the exact
    frame it opened on before Raichu ruins it. Free, and a stronger edit.
Rejected jobs are not charged.
"""
import json
import os
import re
import subprocess
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# (name, path, in, out)  - seconds into the source clip
SEQ = [
    ('T-1_meet-mooney',      'clips/T-1_meet-mooney.mp4',       0.30, 2.70),
    ('T-2_one-eye',          'clips/T-2_one-eye.mp4',           0.60, 2.80),
    ('T-3_treats',           'clips/T-3_treats.mp4',            0.80, 3.00),
    ('T-5_crouch',           'clips/T-5_crouch.mp4',            0.60, 2.80),
    ('T-6_launch',           'clips/T-6_launch.mp4',            0.40, 2.20),
    ('T-7_eyes-open',        'clips/T-7_eyes-open.mp4',         0.50, 1.80),
    ('T-8_kitchen-chase',    'clips/T-8_kitchen-chase.mp4',     0.20, 2.30),
    ('T-9_box-tumble',       'clips/T-9_box-tumble.mp4',        1.20, 3.40),
    # dialogue: the IN/OUT must contain the whole line (speech_map.py)
    ('T-10_why-do-i-follow', 'clips/T-10_why-do-i-follow.mp4',  0.20, 3.40),   # line 0.58-3.14
    ('T-11_because-its-fun', 'clips/T-11_because-its-fun.mp4',  0.00, 1.90),   # line 0.19-1.66
    ('T-1_reprise',          'clips/T-1_meet-mooney.mp4',       1.60, 3.20),   # peaceful again
    ('T-13_i-have-an-idea',  'clips/T-13_i-have-an-idea.mp4',   1.80, 4.00),   # line 2.21-3.68
    ('T-14_oh-no',           'clips/T-14_oh-no.mp4',            0.10, 4.90),   # line 0.35-4.61
    ('T-15_reveal',          'clips/T-15_reveal.mp4',           0.00, 4.00),
]

TARGET_LUFS = -23.0
GAIN_MIN, GAIN_MAX = -8.0, 14.0
PEAK_CEILING = -1.0
BED_GAIN = 0.120
LIMIT_LIN = 0.891
NARR = 'narration.wav'          # optional; mixed under the whole trailer if present
NARR_GAIN = 1.0


def dur(p):
    return float(subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
        capture_output=True, text=True).stdout.strip())


def measure_lufs(p, ss, t):
    out = subprocess.run(
        ['ffmpeg', '-hide_banner', '-nostats', '-ss', '%.3f' % ss, '-t', '%.3f' % t, '-i', p,
         '-af', 'loudnorm=I=%.1f:TP=-1.5:LRA=11:print_format=json' % TARGET_LUFS,
         '-f', 'null', '-'], capture_output=True, text=True).stderr
    m = re.findall(r'\{[^{}]*"input_i"[^{}]*\}', out, re.S)
    if not m:
        return None, 0.0
    try:
        d = json.loads(m[-1])
        v, tp = float(d['input_i']), float(d['input_tp'])
    except Exception:
        return None, 0.0
    return (None if v < -70 else v), tp


def gain_for(lufs, tp):
    if lufs is None:
        return 0.0
    g = max(GAIN_MIN, min(GAIN_MAX, TARGET_LUFS - lufs))
    return min(g, PEAK_CEILING - tp)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else 'TRAILER.mp4'
    missing = [n for n, p, a, b in SEQ if not os.path.exists(p)]
    if missing:
        print('MISSING:', ', '.join(missing))
        sys.exit(1)

    print('%-3s %-24s %7s %8s %8s %7s' % ('#', 'shot', 'cut', 'starts', 'LUFS', 'gain'))
    ins, parts = [], []
    t = 0.0
    for i, (name, path, a, b) in enumerate(SEQ):
        src = dur(path)
        b = min(b, src)
        d = b - a
        if d <= 0:
            sys.exit('%s: bad in/out %.2f-%.2f of %.2fs' % (name, a, b, src))
        lufs, tp = measure_lufs(path, a, d)
        gain = gain_for(lufs, tp)
        print('%-3d %-24s %6.2fs %7.2fs %8s %6.1fdB'
              % (i + 1, name, d, t, 'silent' if lufs is None else '%.1f' % lufs, gain))
        t += d
        ins += ['-ss', '%.3f' % a, '-t', '%.3f' % d, '-i', path]
        parts.append(
            '[%d:v:0]scale=1280:720:force_original_aspect_ratio=decrease,'
            'pad=1280:720:(ow-iw)/2:(oh-ih)/2,fps=24,setsar=1[v%d];'
            '[%d:a:0]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,'
            'volume=%.2fdB,afade=t=in:st=0:d=0.015,afade=t=out:st=%.3f:d=0.015[a%d]'
            % (i, i, i, gain, max(0.0, d - 0.015), i))

    bed = len(SEQ)
    graph = (';'.join(parts) + ';'
             + ''.join('[v%d][a%d]' % (i, i) for i in range(len(SEQ)))
             + 'concat=n=%d:v=1:a=1[v][ac];' % len(SEQ)
             + '[%d:a]highpass=f=70,lowpass=f=1800,volume=%.4f[bed];' % (bed, BED_GAIN)
             + '[ac][bed]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[am];')
    extra = ['-f', 'lavfi', '-i', 'anoisesrc=c=pink:r=48000:a=0.02']
    if os.path.exists(NARR):
        extra += ['-i', NARR]
        graph += ('[%d:a]aresample=48000,volume=%.2f[nar];' % (bed + 1, NARR_GAIN)
                  + '[am][nar]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[mx0];'
                  # summing two near-full-scale layers overshoots, and a 5ms
                  # attack lets the transient through - the first build peaked
                  # at 0.0 dBFS. Pre-attenuate, then limit with a fast attack.
                  + '[mx0]volume=-3dB[mx];'
                  + '[mx]alimiter=limit=%.4f:attack=1:release=60[a]' % LIMIT_LIN)
        print('\nmixing narration from %s' % NARR)
    else:
        graph += '[am]alimiter=limit=%.4f:attack=5:release=60[a]' % LIMIT_LIN
        print('\nno %s - building without narration' % NARR)

    subprocess.run(['ffmpeg', '-y', '-v', 'error'] + ins + extra
                   + ['-filter_complex', graph, '-map', '[v]', '-map', '[a]',
                      '-c:v', 'libx264', '-crf', '19', '-preset', 'medium',
                      '-pix_fmt', 'yuv420p',
                      '-c:a', 'aac', '-b:a', '192k', out], check=True)

    d = dur(out)
    print('%d shots | %.2fs | %.1f MB -> %s'
          % (len(SEQ), d, os.path.getsize(out) / 1e6, out))


if __name__ == '__main__':
    main()
