import subprocess, sys, os
B = 'C:/Users/azpil/Downloads/The_Adventures_of_Mooney_&_Raichu/chicken-caper'
sys.path.insert(0, B)
from manifest import SHOTS
SRC, DST = B + '/audio', B + '/audio_trim'
os.makedirs(DST, exist_ok=True)
# manifest points at a dud take for shot 24 line 1 (~0.05s speech); alternate take from history
SWAP = {'24_1_mooney.mp3': 'alt_24_1_mooney.mp3'}
# peak detection at -45dB: low-level blips (one file starts with a -47.5dB tick) count as silence,
# keep 30ms pre-roll so consonant attacks survive
TRIM = ('silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.03:detection=peak,'
        'areverse,'
        'silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.03:detection=peak,'
        'areverse')

def dur(p):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],
        capture_output=True, text=True).stdout.strip())

def peak(p, ss=0.0, t=None):
    cmd = ['ffmpeg','-v','info']
    if t: cmd += ['-ss', str(ss), '-t', str(t)]
    o = subprocess.run(cmd + ['-i',p,'-af','volumedetect','-f','null','-'], capture_output=True, text=True).stderr
    m = [float(x.split('max_volume:')[1].split()[0]) for x in o.splitlines() if 'max_volume:' in x]
    return m[0] if m else -99.0

print('%-22s %7s %7s  %-8s %s' % ('line','before','after','head dB','note'))
saved = 0.0
for n, label, _, auds in SHOTS:
    for i, (aid, line, spk) in enumerate(auds, 1):
        name = '%02d_%d_%s.mp3' % (n, i, spk)
        src = SRC + '/' + SWAP.get(name, name)
        out = DST + '/' + name
        subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-af',TRIM,
                        '-c:a','libmp3lame','-q:a','2', out], check=True)
        d0, d1 = dur(src), dur(out)
        saved += d0 - d1
        # speech must now start within the first 150ms
        h = peak(out, 0, 0.15)
        print('%-22s %7.2f %7.2f  %-8.1f %s' % (name, d0, d1, h,
              ('LATE ONSET' if h < -40 else '') + ('  [alt take]' if name in SWAP else '')))
print('\ntrimmed %.2fs of dead air' % saved)
