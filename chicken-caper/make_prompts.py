import json, re, sys
B = 'C:/Users/azpil/Downloads/The_Adventures_of_Mooney_&_Raichu/chicken-caper'
sys.path.insert(0, B)
from manifest import SHOTS

old = json.load(open(B + '/prompts_all.json'))

# identical wording in every prompt so the native voices stay consistent across 26 separate generations
VOICES = ("VOICES (identical in every shot): MOONEY speaks with a deep, slow, gravelly middle-aged male "
          "voice, flat, dry and sarcastic, like he is half asleep. RAICHU speaks with a bright, fast, "
          "excitable younger male voice. The neighbor is a MIDDLE-AGED WOMAN with a warm female voice. ")
LIPSYNC = ("TALKING ANIMATION REQUIRED: mouths, jaws and cheeks MUST move in clear sync with each spoken "
           "line. The listening character keeps his mouth closed. ")
SFX = ("AUDIO: generate natural ambience and comedic sound effects for this scene. ")

# phrases from the original prompts that actively suppressed lip sync and audio
KILL = [
    r'DO NOT render words or mouth-sync dialogue\.?',
    r'do not render words or mouth-sync dialogue\.?',
    r'\bSilent[;,]?\s*dialogue (?:will be )?added later\.?',
    r'\bSilent visual only,?\s*',
    r'\bSilent polished', r'\bsilent polished',
    r'\bSilent[,;]?\s+', r',\s*silent\b',
]

def clean(p):
    p = p.replace('\ufffd', '-')
    for k in KILL:
        p = re.sub(k, '', p)
    p = re.sub(r'\s{2,}', ' ', p).strip()
    # the originals ended "...silent polished cinematic 3D family cartoon"; restore a clean tail
    if not re.search(r'(cartoon|animation|quality)\.?$', p):
        p += ' Polished cinematic family-friendly 3D cartoon animation.'
    return p

def dialogue_block(auds):
    if not auds:
        return "NO DIALOGUE in this shot: ambience and sound effects only, both cats keep their mouths closed. "
    who = {'mooney': 'MOONEY', 'raichu': 'RAICHU', 'human': 'THE NEIGHBOR (middle-aged woman)'}
    lines = ' Then '.join('%s says, "%s"' % (who[s], l) for _, l, s in auds)
    return "SPOKEN DIALOGUE, in this exact order: %s. Speak these lines and no others. " % lines

# --- the two shots that rendered wrong ---
FIX = {
3: ("EPISODE 1 - THE GREAT CHICKEN CAPER. Chicken discovery shot. Inside the same cozy New England coastal "
    "home, using the supplied Mooney and Raichu reference faithfully. RAICHU, the large fluffy brown-black-gray "
    "Maine Coon tabby with tufted ears and huge striped tail, sits at the front window looking out. "
    "THE WINDOWSILL IS COMPLETELY EMPTY - no chicken, no food, no package, no object of any kind. "
    "ACROSS THE YARD at the neighboring gray-shingle house, THE NEIGHBOR IS A MIDDLE-AGED WOMAN. She has just "
    "parked and is ARRIVING HOME: she walks FORWARD ALONG THE FRONT PATH TOWARD HER OWN FRONT DOOR, AWAY from "
    "camera, carrying grocery bags and a clear takeout container with a rotisserie chicken. She goes UP her "
    "porch steps, OPENS HER FRONT DOOR AND STEPS INSIDE HER HOUSE WITH THE CHICKEN, and the door closes behind "
    "her. SHE MUST MOVE TOWARD THE HOUSE AND ENTER IT. She must NOT walk down the steps, must NOT walk toward "
    "camera, must NOT leave the house, must NOT be male. The chicken never touches Raichu's house, window, "
    "windowsill, yard or porch. Raichu notices from a distance: ears perk, eyes widen, whiskers forward, tail "
    "gives one excited swish. MOONEY, the black-and-white tuxedo cat, stays asleep on the couch in the "
    "background. Preserve both cats' exact faces, markings, colors and proportions. Warm Saturday morning light, "
    "gray shingle houses, white trim, hydrangeas, harbor-town atmosphere. EXACTLY ONE HUMAN, EXACTLY TWO CATS. "
    "No text, no labels, no extra cats, no clothing on the cats. One continuous cinematic shot with depth: "
    "Raichu inside foreground, empty windowsill, yard in middle distance, the woman and chicken entering the "
    "neighboring house in the background. Polished family animated feature-film quality."),
9: ("EPISODE 1 - THE GREAT CHICKEN CAPER. Fence crossing. SAME New England coastal backyard immediately after "
    "the sprinkler shot. Preserve Mooney and Raichu exactly. CAMERA: locked-off wide profile view from the side, "
    "so the fence runs left-to-right across frame and BOTH SIDES OF THE FENCE ARE CLEARLY VISIBLE. The cats' "
    "home yard is on the LEFT of the fence; the neighbor's yard is on the RIGHT. Weathered wooden fence about "
    "four feet tall with a broad stable top rail; cedar shed and hydrangeas in background. "
    "ACTION IN STRICT ORDER: (1) RAICHU, the fluffy Maine Coon tabby, starts in the LEFT yard, makes ONE "
    "graceful four-legged cat jump from the ground up onto the fence top rail, balances there briefly, then "
    "jumps DOWN THE FAR SIDE INTO THE RIGHT-HAND NEIGHBOR YARD AND STAYS THERE. RAICHU MUST END THE SHOT ON THE "
    "RIGHT SIDE OF THE FENCE. He must NOT jump back down into the left yard. (2) MOONEY, the rounder "
    "black-and-white tuxedo cat, still in the LEFT yard, jumps and catches the top rail with both front paws, "
    "hind legs scrabbling against the boards, struggles comically, then hauls himself UP ONTO THE TOP RAIL and "
    "sits there panting. MOONEY GOES OVER THE TOP OF THE FENCE. He must NEVER go under the fence, never squeeze "
    "between boards, never crawl through a gap, and must not fall or be hurt. (3) RAICHU, on the RIGHT side, "
    "looks back up at him impatiently. THE TWO CATS MUST END ON OPPOSITE SIDES OF THE FENCE. "
    "EXACTLY TWO CATS. No humans, no chicken, no food, no sprinkler spray, no other animals, no clothing, no "
    "text. No duplicated cats or limbs, no flying, no human-like hands, no morphing, no character swapping. "
    "Four-legged feline movement only. Warm Saturday morning. Polished cinematic 3D family cartoon."),
}

out = {}
for n, label, vid, auds in SHOTS:
    base = FIX[n] if n in FIX else clean(old[str(n)])
    out[n] = {'label': label, 'image': '3c223738-22f6-4de6-bfd6-6c62333be42c',
              'fixed': n in FIX, 'has_dialogue': bool(auds),
              'prompt': base + ' ' + VOICES + dialogue_block(auds) + (LIPSYNC if auds else '') + SFX}
json.dump(out, open(B + '/prompts_v2.json', 'w'), indent=1)

print('%-5s %-15s %-7s %-6s %s' % ('shot', 'label', 'fixed?', 'lines', 'chars'))
for n in sorted(out):
    o = out[n]
    print('%-5d %-15s %-7s %-6d %d' % (n, o['label'], 'REWROTE' if o['fixed'] else '', 
          len([a for a in SHOTS[n-1][3]]), len(o['prompt'])))
print('\nwrote prompts_v2.json  |  %d shots, %d rewritten' % (len(out), sum(1 for o in out.values() if o['fixed'])))
