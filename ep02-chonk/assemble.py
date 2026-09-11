"""Assemble Episode 1 'Chonk'.

Differences from ep01's assemble.py:
  * per-clip loudness matching, because the raw Seedance clips land anywhere
    between -7 and -22 dB peak and the dialogue jumps in volume between shots.
    The gain is CLAMPED so near-silent ambience shots (B-9, B-11) don't get
    boosted up to dialogue level and turn the wind into a roar.
  * handles clips outside clips/ (the reused main title and end card).
"""
import subprocess, os, sys, json, re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

REUSE = '../series/reusable'

SEQ = [
    # cold open
    ('CO-1_v2_vet-exit',        'clips/CO-1_v2_vet-exit.mp4'),
    ('CO-2_carrier',            'clips/CO-2_carrier.mp4'),
    ('CO-3_counter-fail',       'clips/CO-3_counter-fail.mp4'),
    ('CO-4_carrier-again',      'clips/CO-4_carrier-again.mp4'),
    ('CO-5_the-portion',        'clips/CO-5_the-portion.mp4'),
    # --- divider: cold open -> titles ---
    ('DIV-1_open',              'clips/DIV-L.mp4'),
    # main title (reused, free)
    ('TS-1_main-title',         'clips/TS-1_FINAL_main-title.mp4'),   # reused plate + episode line
    # act one - the sentence
    ('A-1_v2_keep-an-eye',      'clips/A-1_v2_keep-an-eye.mp4'),
    ('A-2_i-will-die',          'clips/A-2_i-will-die.mp4'),
    ('A-3_she-meant-generally', 'clips/A-3_she-meant-generally.mp4'),
    ('A-4_never-given-a-job',   'clips/A-4_never-given-a-job.mp4'),
    ('A-5_lots-of-jobs',        'clips/A-5_lots-of-jobs.mp4'),
    ('A-6_name-one',            'clips/A-6_name-one.mp4'),
    ('A-7_watch-the-door',      'clips/A-7_watch-the-door.mp4'),
    ('A-8_and',                 'clips/A-8_and.mp4'),
    ('A-9_raccoon-lives-here',  'clips/A-9_raccoon-lives-here.mp4'),
    ('A-10_gary-morning',       'clips/A-10_gary-morning.mp4'),
    ('A-11_garys-fine',         'clips/A-11_garys-fine.mp4'),
    ('A-12_never-been-hungry',  'clips/A-12_never-been-hungry.mp4'),
    # --- divider: act one -> act two ---
    ('DIV-1b_to-act-two',       'clips/DIV-R.mp4'),
    # act two - the movement
    ('B-1_ive-been-reading',    'clips/B-1_ive-been-reading.mp4'),
    ('B-2_you-cant-read',       'clips/B-2_you-cant-read.mp4'),
    ('B-3_deciding-what-they-say', 'clips/B-3_deciding-what-they-say.mp4'),
    # --- divider: before the laser reveal ---
    ('DIV-1c_to-lasers',        'clips/DIV-L.mp4'),
    ('B-4_where-did-you-get-lasers', 'clips/B-4_where-did-you-get-lasers.mp4'),
    ('B-5_the-drawer',          'clips/B-5_the-drawer.mp4'),
    ('B-6_no-laser-drawer',     'clips/B-6_no-laser-drawer.mp4'),
    ('B-7_i-made-one',          'clips/B-7_i-made-one.mp4'),
    # --- divider: kitchen -> back fence ---
    ('DIV-2_to-fence',          'clips/DIV-R.mp4'),
    ('B-8_who-here-is-tired',   'clips/B-8_who-here-is-tired.mp4'),
    ('B-9_blank-faces-1',       'clips/B-9_blank-faces-1.mp4'),
    ('B-10_nobodys-told-you',   'clips/B-10_nobodys-told-you.mp4'),
    ('B-11_blank-faces-2',      'clips/B-11_blank-faces-2.mp4'),
    ('B-12_im-going-to-tell-you', 'clips/B-12_im-going-to-tell-you.mp4'),
    ('B-13_movement-montage',   'clips/B-13_movement-montage.mp4'),
    ('B-14_the-banner',         'clips/B-14_the-banner.mp4'),
    # --- divider: garden day -> kitchen night ---
    ('DIV-3_to-night',          'clips/DIV-L.mp4'),
    # act three - the black market
    ('C-1_empty-bowl-night',    'clips/C-1_empty-bowl-night.mp4'),
    ('C-2_gerald-at-the-window','clips/C-2_gerald-at-the-window.mp4'),
    ('C-3_what-do-you-have',    'clips/C-3_what-do-you-have.mp4'),
    ('C-4_half-a-sandwich',     'clips/C-4_half-a-sandwich.mp4'),
    ('C-5_what-do-you-want',    'clips/C-5_what-do-you-want.mp4'),
    ('C-6_everything-you-own',  'clips/C-6_everything-you-own.mp4'),
    ('C-7_i-own-a-bowl',        'clips/C-7_i-own-a-bowl.mp4'),
    ('C-8_then-i-want-the-bowl','clips/C-8_then-i-want-the-bowl.mp4'),
    ('C-9_the-transaction',     'clips/C-9_the-transaction.mp4'),
    ('C-10_eating-in-the-dark', 'clips/C-10_eating-in-the-dark.mp4'),
    ('C-11_disappointed',       'clips/C-11_disappointed.mp4'),
    ('C-12_nobody-asked-you-gary','clips/C-12_nobody-asked-you-gary.mp4'),
    ('C-13_escalation-montage', 'clips/C-13_escalation-montage.mp4'),
    # --- divider: night -> morning ---
    ('DIV-4_to-morning',        'clips/DIV-R.mp4'),
    # act four - collapse
    ('D-1_the-clean-circle',    'clips/D-1_the-clean-circle.mp4'),
    ('D-2_wheres-your-bowl',    'clips/D-2_wheres-your-bowl.mp4'),
    ('D-3_what-bowl',           'clips/D-3_what-bowl.mp4'),
    ('D-4_you-had-a-bowl',      'clips/D-4_you-had-a-bowl.mp4'),
    ('D-5_did-i',               'clips/D-5_did-i.mp4'),
    ('D-6_the-throne',          'clips/D-6_the-throne.mp4'),
    # --- divider: kitchen -> garden ---
    ('DIV-5_to-garden',         'clips/DIV-L.mp4'),
    ('D-7_the-collapse',        'clips/D-7_the-collapse.mp4'),
    ('D-8_alone-in-the-wreckage','clips/D-8_alone-in-the-wreckage.mp4'),
    # --- divider: garden -> deck at sunset ---
    ('DIV-6_to-deck',           'clips/DIV-R.mp4'),
    # resolution - the wrong moral
    ('E-1_i-wanted-to-help',    'clips/E-1_i-wanted-to-help.mp4'),
    ('E-2_i-know',              'clips/E-2_i-know.mp4'),
    ('E-3_i-learned-something', 'clips/E-3_i-learned-something.mp4'),
    ('E-4_thats-not',           'clips/E-4_thats-not.mp4'),
    ('E-5_id-do-it-again',      'clips/E-5_id-do-it-again.mp4'),
    # end card (reused, free) + teaser
    ('EC-1_endcard',            REUSE + '/END-CARD.mp4'),
    ('TZ-1_gary-moves-in',      'clips/TZ-1_FINAL_gary-moves-in.mp4'),  # + teaser text
    # --- like & subscribe outro, paw-pressed ---
    ('OUTRO_like-subscribe',    'clips/OUTRO_like-subscribe.mp4'),
]

# Measured spread across the 60 shots is -51 to -20 LUFS (median -29.4), so the
# target sits near the dialogue cluster and the clamp is wide enough to reach it.
# Ambience-only shots (B-9/B-11 blank faces, D-8, C-10) sit far below the clamp
# and therefore STAY quieter than dialogue, which is what the edit wants.
# Head trims. Seedance front-loads dead air: the character often stands there
# for seconds before speaking. Measured with pacing.py (first sustained run of
# voiced frames), then cut so each line lands ~0.6s in. Shots whose opening
# carries a visual beat (a reveal, a character noticing, Gerald's stillness)
# keep a longer lead-in. Set TRIM to an empty dict to restore untrimmed pacing.
TRIM = {
    'CO-2_carrier':                     1.13,   # line at 1.73s -> shot 2.91s
    'A-1_v2_keep-an-eye':               1.90,   # line at 2.50s -> shot 3.19s
    'A-3_she-meant-generally':          1.51,   # line at 2.11s -> shot 2.53s
    'A-4_never-given-a-job':            1.99,   # line at 2.59s -> shot 3.10s
    'A-7_watch-the-door':               0.74,   # line at 1.34s -> shot 4.30s
    'A-9_raccoon-lives-here':           0.68,   # line at 1.28s -> shot 3.36s
    'A-10_gary-morning':                2.52,   # line at 4.22s -> shot 2.56s
    'B-1_ive-been-reading':             1.80,   # line at 3.52s -> shot 2.17s
    'B-2_you-cant-read':                1.13,   # line at 1.73s -> shot 2.91s
    'B-4_where-did-you-get-lasers':     2.04,   # line at 3.94s -> shot 4.01s
    'B-5_the-drawer':                   2.30,   # line at 2.94s -> shot 1.80s
    'B-6_no-laser-drawer':              2.09,   # line at 2.69s -> shot 2.95s
    'B-8_who-here-is-tired':            2.01,   # line at 3.71s -> shot 5.09s
    'B-10_nobodys-told-you':            0.97,   # line at 1.57s -> shot 3.13s
    'B-12_im-going-to-tell-you':        3.05,   # line at 3.65s -> shot 2.04s
    'C-3_what-do-you-have':             2.06,   # line at 2.66s -> shot 1.99s
    'C-5_what-do-you-want':             1.77,   # line at 2.37s -> shot 2.27s
    'C-6_everything-you-own':           1.82,   # line at 3.42s -> shot 3.26s
    'C-7_i-own-a-bowl':                 1.10,   # line at 1.70s -> shot 2.95s
    'C-8_then-i-want-the-bowl':         0.54,   # line at 2.14s -> shot 4.54s
    'C-12_nobody-asked-you-gary':       2.28,   # line at 2.88s -> shot 3.76s
    'D-2_wheres-your-bowl':             3.05,   # line at 3.65s -> shot 2.04s
    'D-3_what-bowl':                    1.70,   # line at 2.30s -> shot 2.34s
    'D-5_did-i':                        2.34,   # line at 2.94s -> shot 2.70s
    'E-1_i-wanted-to-help':             4.20,   # line at 4.80s -> shot 2.90s
    'E-2_i-know':                       3.62,   # line at 4.22s -> shot 2.42s
    'E-4_thats-not':                    1.61,   # line at 2.21s -> shot 3.48s
    'E-5_id-do-it-again':               3.30,   # line at 3.90s -> shot 2.74s
}

TARGET_LUFS = -23.0
GAIN_MIN, GAIN_MAX = -8.0, 14.0
PEAK_CEILING = -1.0              # never let the boost clip
BED_GAIN = 0.120                 # pink-noise room-tone floor, ~-52 dBFS under -23 LUFS dialogue
LIMIT_LIN = 0.891                # -1 dBFS output ceiling


def dur(p):
    return float(subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
        capture_output=True, text=True).stdout.strip())


def measure_lufs(p):
    """(integrated LUFS, true peak dBTP); LUFS is None when effectively silent."""
    out = subprocess.run(
        ['ffmpeg', '-hide_banner', '-nostats', '-i', p,
         '-af', 'loudnorm=I=%.1f:TP=-1.5:LRA=11:print_format=json' % TARGET_LUFS,
         '-f', 'null', '-'],
        capture_output=True, text=True).stderr
    m = re.findall(r'\{[^{}]*"input_i"[^{}]*\}', out, re.S)
    if not m:
        return None, 0.0
    try:
        d = json.loads(m[-1])
        v = float(d['input_i'])
        tp = float(d['input_tp'])
    except Exception:
        return None, 0.0
    return (None if v < -70 else v), tp


def gain_for(lufs, tp):
    """Clamped match toward TARGET_LUFS, then held below the peak ceiling."""
    if lufs is None:
        return 0.0
    g = max(GAIN_MIN, min(GAIN_MAX, TARGET_LUFS - lufs))
    return min(g, PEAK_CEILING - tp)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else 'CHONK_EPISODE-1.mp4'
    missing = [n for n, p in SEQ if not os.path.exists(p)]
    if missing:
        print('MISSING %d:' % len(missing))
        for m in missing:
            print('   ', m)
        sys.exit(1)

    print('%-3s %-30s %7s %8s %8s %7s' % ('#', 'shot', 'dur', 'starts', 'LUFS', 'gain'))
    ins, parts = [], []
    t = 0.0
    for i, (name, path) in enumerate(SEQ):
        t0 = TRIM.get(name, 0.0)
        d = dur(path) - t0
        lufs, tp = measure_lufs(path)
        gain = gain_for(lufs, tp)
        shown = 'silent' if lufs is None else '%.1f' % lufs
        print('%-3d %-30s %6.2fs %7.2fs %8s %6.1fdB' % (i + 1, name, d, t, shown, gain))
        t += d
        ins += (['-ss', '%.3f' % t0] if t0 else []) + ['-i', path]
        parts.append(
            '[%d:v:0]scale=1280:720:force_original_aspect_ratio=decrease,'
            'pad=1280:720:(ow-iw)/2:(oh-ih)/2,fps=24,setsar=1[v%d];'
            '[%d:a:0]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,'
            'volume=%.2fdB,afade=t=in:st=0:d=0.015,afade=t=out:st=%.3f:d=0.015[a%d]'
            % (i, i, i, gain, max(0.0, d - 0.015), i))

    # The raw Seedance clips carry no continuous room tone: 9 of the 60 drop to
    # absolute digital silence for 16.2s in total (D-2 alone is silent for 3.6s
    # of its 5.1s). That reads as the sound cutting out mid-scene. A pink-noise
    # floor well below dialogue keeps the room alive underneath without being
    # audible as hiss. The limiter then guarantees nothing clips.
    bed = len(SEQ)
    graph = (';'.join(parts) + ';'
             + ''.join('[v%d][a%d]' % (i, i) for i in range(len(SEQ)))
             + 'concat=n=%d:v=1:a=1[v][ac];' % len(SEQ)
             + '[%d:a]highpass=f=70,lowpass=f=1800,volume=%.4f[bed];' % (bed, BED_GAIN)
             + '[ac][bed]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[am];'
             + '[am]alimiter=limit=%.4f:attack=5:release=60[a]' % LIMIT_LIN)

    subprocess.run(['ffmpeg', '-y', '-v', 'error'] + ins
                   + ['-f', 'lavfi', '-i', 'anoisesrc=c=pink:r=48000:a=0.02']
                   + ['-filter_complex', graph, '-map', '[v]', '-map', '[a]',
                      '-c:v', 'libx264', '-crf', '19', '-preset', 'medium',
                      '-pix_fmt', 'yuv420p',
                      '-c:a', 'aac', '-b:a', '192k', out], check=True)

    d = dur(out)
    print('\n%d shots | %.2fs (%d:%04.1f) | %.1f MB -> %s'
          % (len(SEQ), d, d // 60, d % 60, os.path.getsize(out) / 1e6, out))


if __name__ == '__main__':
    main()
