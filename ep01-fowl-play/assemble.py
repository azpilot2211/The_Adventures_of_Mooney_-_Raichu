import subprocess, os, sys
os.chdir(r'C:\Users\azpil\Downloads\The_Adventures_of_Mooney_&_Raichu\ep01-fowl-play')
SEQ = [
    # cold open
    'CO-1_v2_sandwich','CO-2_raichu-bursts','CO-3_v2_gerald-eats',
    # main title + windowsill gag
    'TS-1_FINAL_main-title','WG-1_windowsill-gag',
    # act one - declaration of war
    'A1-1_raichu-paces','A1-2_mooney-sunbeam','A1-3_raichu-wheels','A1-4_mooney-one-eye',
    'A1-5_battle-map','A1-6_mooney-deadpan','A1-7_aggressively',
    # act two - the ladder
    'T1-1_box-trap','T1-2_its-a-box','T1-3_ambush','T1-4_gerald-under-box','T1-5_box-drops',
    'T2-1_sprinkler-rig','T2-2_seagulls-ocean','T2-3_gerald-sprayed','T2-4_mooney-sprayed',
    'T3-1_meet-todd','T3-2_todd','T3-3_gerald-todd','T3-4_raichu-skids','T3-5_day-three',
    'T4-1_montage',
    # act three - phase twelve
    'A3-1_phase-twelve','A3-2_how-long-asleep','A3-3_tuesday','A3-4_the-bait','A3-5_gerald-surveys',
    'A3-6_come-on','A3-7_walks-around','A3-8_lunge-trigger','A3-9_collapse',
    # resolution - the nap
    'R-1_hes-better','R-2_bird-with-schedule','R-3_asleep-on-sandwich','R-4_gerald-returns',
    'R-5_paw-on-foot','R-6_gerald-gives-up','R-7_how-did-you','R-8_i-didnt',
    # end
    'EC-1_FINAL_endcard','TZ-1_FINAL_teaser',
]
OUT = sys.argv[1] if len(sys.argv)>1 else 'FOWL-PLAY_EPISODE-1.mp4'
def dur(p): return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
missing=[n for n in SEQ if not os.path.exists('clips/%s.mp4'%n)]
if missing: print('MISSING:',missing); sys.exit(1)
ins,parts=[],[]; t=0.0
print('%-3s %-26s %7s %8s'%('#','shot','dur','starts'))
for i,n in enumerate(SEQ):
    p='clips/%s.mp4'%n; d=dur(p)
    print('%-3d %-26s %6.2fs %7.2fs'%(i+1,n,d,t)); t+=d
    ins+=['-i',p]
    parts.append('[%d:v:0]scale=1280:720,fps=24,setsar=1[v%d];[%d:a:0]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo[a%d]'%(i,i,i,i))
graph=';'.join(parts)+';'+''.join('[v%d][a%d]'%(i,i) for i in range(len(SEQ)))+'concat=n=%d:v=1:a=1[v][a]'%len(SEQ)
subprocess.run(['ffmpeg','-y','-v','error']+ins+['-filter_complex',graph,'-map','[v]','-map','[a]',
    '-c:v','libx264','-crf','19','-preset','medium','-c:a','aac','-b:a','192k',OUT],check=True)
d=dur(OUT)
print('\n%d shots | %.2fs (%d:%04.1f) | %.1f MB -> %s'%(len(SEQ),d,d//60,d%60,os.path.getsize(OUT)/1e6,OUT))
