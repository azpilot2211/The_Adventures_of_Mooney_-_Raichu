import subprocess, os, sys, json
B = 'C:/Users/azpil/Downloads/The_Adventures_of_Mooney_&_Raichu/chicken-caper'
sys.path.insert(0, B)
from manifest import SHOTS
AUDIO_DIR = B + '/' + (sys.argv[1] if len(sys.argv) > 1 else 'audio')
OUT = B + '/' + (sys.argv[2] if len(sys.argv) > 2 else 'mooney_raichu_ep1.mp4')

def dur(p):
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration',
        '-of','csv=p=0',p], capture_output=True, text=True).stdout.strip())

def clip(n, label): return '%s/clips/%02d_%s.mp4' % (B, n, label)

# 1. lossless video concat (all clips share codec/res/fps)
lst = B + '/concat.txt'
with open(lst, 'w') as f:
    for n, label, _, _ in SHOTS:
        f.write("file '%s'\n" % clip(n, label))
silent = B + '/_video_silent.mp4'
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',lst,'-c','copy',silent], check=True)

# 2. place each line inside its shot; shrink lead-in/gap when a shot is tight
placements, t = [], 0.0
for n, label, _, auds in SHOTS:
    sd = dur(clip(n, label))
    if auds:
        paths = ['%s/%02d_%d_%s.mp3' % (AUDIO_DIR, n, i, spk) for i,(a,l,spk) in enumerate(auds,1)]
        ds = [dur(p) for p in paths]
        for head, gap, tail in [(0.5,0.35,0.30),(0.5,0.20,0.30),(0.30,0.15,0.25),(0.15,0.12,0.20),(0.10,0.08,0.10)]:
            if head + sum(ds) + gap*(len(ds)-1) + tail <= sd: break
        off = head
        for i,(aid,line,spk) in enumerate(auds,1):
            placements.append((paths[i-1], t+off, spk, line, n))
            off += ds[i-1] + gap
        end = head + sum(ds) + gap*(len(ds)-1)
        if end > sd: print('  ! shot %02d overruns by %.2fs' % (n, end-sd))
    t += sd

# 3. dialogue bed -> mux
ins, filt = [], []
for i,(p,start,spk,line,n) in enumerate(placements):
    ins += ['-i', p]
    filt.append('[%d:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,'
                'adelay=%d|%d[a%d]' % (i+1, int(start*1000), int(start*1000), i))
graph = ';'.join(filt) + ';' + ''.join('[a%d]'%i for i in range(len(placements))) + \
        'amix=inputs=%d:normalize=0:dropout_transition=0,apad[mix]' % len(placements)
subprocess.run(['ffmpeg','-y','-v','error','-i',silent] + ins + ['-filter_complex',graph,
    '-map','0:v','-map','[mix]','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',OUT], check=True)

json.dump([{'shot':n,'at':round(s,2),'speaker':k,'line':l} for _,s,k,l,n in placements],
          open(B + '/timeline.json','w'), indent=1)
print('OK ->', OUT, '%.2fs' % dur(OUT), '| %d lines placed' % len(placements))
