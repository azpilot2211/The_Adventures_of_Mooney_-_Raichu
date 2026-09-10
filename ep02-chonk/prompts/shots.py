# -*- coding: utf-8 -*-
"""All 36 remaining shots for Episode 2 'Chonk'. Dialogue copied verbatim from chonk.html."""
import json
from blocks import *

NO_TEXT = ("Do not show any readable text, do not show any alphabet letters, "
           "do not show any words or writing anywhere in frame.")

S = []
def shot(key, dur, prompt, refs, chain=None):
    S.append(dict(key=key, dur=dur, prompt=" ".join(prompt.split()), refs=refs, chain=chain))

# ---------------- ACT TWO (remainder) ----------------
shot("B-6_no-laser-drawer", 5, f"""
{STYLE} {KITCHEN_DAY} {MOONEY} Mooney lies flat on the kitchen floor, chin on his paws, looking up
off-screen with total contempt. The camera is low and close on him. Only his mouth moves; the rest of
him is completely still. EXACTLY ONE CAT. No humans, no bird, no other animals.
MOONEY says, {V_MOONEY}: "We don't have a laser drawer."
Audio: refrigerator hum, faint kitchen room tone.
""", [REF_CAST])

shot("B-7_i-made-one", 6, f"""
{STYLE} {KITCHEN_DAY} {RAICHU} Raichu sits upright facing camera, patient and reasonable, explaining
something obvious to a child. He blinks slowly, entirely sincere. EXACTLY ONE CAT. No humans, no bird,
no other animals. No books, no newspapers, no printed matter anywhere in frame.
RAICHU says, {V_RAICHU}: "We do now. I made one. I put the lasers in it. It's the laser drawer."
Audio: faint kitchen room tone.
""", [REF_CAST])

shot("B-8_who-here-is-tired", 7, f"""
{STYLE} {FENCE_DAY} {CATS6} {RAICHU} The six neighbourhood cats sit in a row along the top of the fence,
evenly spaced, facing camera, motionless. Below them on the grass RAICHU paces back and forth beside a
chart he has scratched into a patch of bare sand - meaningless scribbled lines and crude claw marks, not
writing. He taps the chart with one paw, addressing the cats like a rally speaker.
EXACTLY SEVEN CATS: six ordinary cats on the fence and RAICHU on the grass. No humans, no bird, no other
animals. {NO_TEXT}
RAICHU says, {V_RAICHU}: "Who here is tired of being told what a healthy weight is?"
Audio: outdoor wind, distant gull, grass rustle.
""", [REF_CATS6, REF_CAST])

shot("B-9_blank-faces-1", 5, f"""
{STYLE} {FENCE_DAY} {CATS6} A locked-off static wide shot of the six neighbourhood cats sitting in a row
along the top of the fence, facing camera. Nobody moves. Nobody speaks. One cat blinks once, slowly.
The shot holds far too long on their blank vacant faces. No camera movement whatsoever.
EXACTLY SIX CATS. No humans, no bird, no other animals, no Maine Coon, no tuxedo cat.
There is no dialogue in this shot. Nobody speaks. Complete silence from the cats.
Audio: wind, one distant gull, crickets.
""", [REF_CATS6])

shot("B-10_nobodys-told-you", 4, f"""
{STYLE} {FENCE_DAY} {RAICHU} Raichu on the grass below the fence, looking up, his confidence faltering
for the first time. His ear tufts twitch. EXACTLY ONE CAT. No humans, no bird, no other animals.
RAICHU says, {V_RAICHU}: "...Nobody's told you?"
Audio: wind, distant gull.
""", [REF_CAST])

shot("B-11_blank-faces-2", 4, f"""
{STYLE} {FENCE_DAY} {CATS6} A locked-off static wide shot of the six neighbourhood cats sitting in a row
along the top of the fence, facing camera. Still nothing. Nobody moves, nobody reacts, nobody speaks.
The shot holds far too long on their blank vacant faces. No camera movement whatsoever.
EXACTLY SIX CATS. No humans, no bird, no other animals, no Maine Coon, no tuxedo cat.
There is no dialogue in this shot. Nobody speaks. Complete silence from the cats.
Audio: the same wind, the same distant gull.
""", [REF_CATS6], chain="B-9_blank-faces-1")

shot("B-12_im-going-to-tell-you", 5, f"""
{STYLE} {FENCE_DAY} {RAICHU} Raichu straightens up on the grass below the fence. Something enormous has
just occurred to him and his eyes go wide with purpose. EXACTLY ONE CAT. No humans, no bird, no other
animals.
RAICHU says, {V_RAICHU}: "Okay. I'm going to tell you."
Audio: wind, one rising musical sting.
""", [REF_CAST])

shot("B-13_movement-montage", 7, f"""
{STYLE} {FENCE_DAY} {CATS6} {RAICHU} A fast comedic montage of a fitness movement taking hold in the back
garden. Ordinary cats attempt jumping jacks badly and completely out of sync. One cat walks on top of a
loose log that rolls under it like a treadmill. RAICHU, with a small whistle gripped in his mouth, blows
it directly into a sleeping cat's ear. One cat lies face-down and motionless in a flowerbed, finished.
No humans, no bird. {NO_TEXT}
There is no dialogue in this shot. Nobody speaks.
Audio: whistle blast, rhythmic panting, one collapse thud.
""", [REF_CATS6, REF_CAST])

shot("B-14_the-banner", 6, f"""
{STYLE} {FENCE_DAY} {RAICHU} A tiny hand-painted cloth banner is strung between two hydrangea bushes,
covered in crude claw-scratch marks and simple painted shapes - NOT letters, NOT words. RAICHU stands
below it looking up, genuinely moved, one paw held over his chest, eyes shining. EXACTLY ONE CAT.
No humans, no bird, no other animals. {NO_TEXT}
There is no dialogue in this shot. Nobody speaks.
Audio: a single reverent choir note, breeze in fabric.
""", [REF_CAST])

# ---------------- ACT THREE ----------------
shot("C-1_empty-bowl-night", 5, f"""
{STYLE} {KITCHEN_NIGHT} {MOONEY} Mooney sits alone in the dark kitchen directly in front of a small empty
ceramic bowl, lit only by cold blue moonlight. He does not move at all. His stomach makes a long
undignified gurgling noise. The shot holds on him. It happens again. EXACTLY ONE CAT.
No humans, no bird, no other animals. There is no dialogue in this shot. Nobody speaks.
Audio: refrigerator hum, long stomach growl, ticking clock.
""", [REF_CAST])

shot("C-2_gerald-at-the-window", 6, f"""
{STYLE} {KITCHEN_NIGHT} {MOONEY} {GERALD} Mooney sits on the kitchen counter at the window, silhouetted,
looking out. Through the glass, on the moonlit fence outside, sits GERALD the enormous herring gull,
holding a small crumpled brown paper bag in one foot. Gerald is perfectly still. He has been waiting.
He knew Mooney would come. EXACTLY ONE CAT AND EXACTLY ONE BIRD. No humans, no other animals.
There is no dialogue in this shot. Nobody speaks.
Audio: night crickets, one slow wingbeat, low bass note.
""", [REF_CAST, REF_GERALD])

shot("C-3_what-do-you-have", 4, f"""
{STYLE} {KITCHEN_NIGHT} {MOONEY} Close on Mooney at the kitchen window in cold blue moonlight, looking out.
Flat, transactional, no emotion. Only his mouth moves. EXACTLY ONE CAT. No humans, no bird, no other animals.
MOONEY says, {V_MOONEY}: "What do you have."
Audio: night crickets, refrigerator hum.
""", [REF_CAST])

shot("C-4_half-a-sandwich", 4, f"""
{STYLE} {FENCE_NIGHT} {GERALD} Close on GERALD sitting on the moonlit fence outside, holding a small
crumpled brown paper bag in one foot. He does not look inside the bag. He already knows what is in the
bag. He does not blink. EXACTLY ONE BIRD. No cats, no humans, no other animals.
GERALD says, {V_GERALD}: "Half a sandwich."
Audio: night crickets, one slow wingbeat.
""", [REF_GERALD])

shot("C-5_what-do-you-want", 4, f"""
{STYLE} {KITCHEN_NIGHT} {MOONEY} Close on Mooney at the kitchen window in cold blue moonlight. Flat and
transactional. Only his mouth moves. EXACTLY ONE CAT. No humans, no bird, no other animals.
MOONEY says, {V_MOONEY}: "What do you want."
Audio: night crickets, refrigerator hum.
""", [REF_CAST])

shot("C-6_everything-you-own", 5, f"""
{STYLE} {FENCE_NIGHT} {GERALD} Close on GERALD on the moonlit fence, completely still, pale eyes fixed
forward. Utterly matter-of-fact. EXACTLY ONE BIRD. No cats, no humans, no other animals.
GERALD says, {V_GERALD}: "Everything you own."
Audio: night crickets, low bass note.
""", [REF_GERALD])

shot("C-7_i-own-a-bowl", 4, f"""
{STYLE} {KITCHEN_NIGHT} {MOONEY} Close on Mooney at the kitchen window in cold blue moonlight. A long flat
beat before he answers. Only his mouth moves. EXACTLY ONE CAT. No humans, no bird, no other animals.
MOONEY says, {V_MOONEY}: "I own a bowl."
Audio: night crickets, refrigerator hum.
""", [REF_CAST])

shot("C-8_then-i-want-the-bowl", 5, f"""
{STYLE} {FENCE_NIGHT} {GERALD} Close on GERALD on the moonlit fence. He does not blink. Not one feather
moves. EXACTLY ONE BIRD. No cats, no humans, no other animals.
GERALD says, {V_GERALD}: "Then I want the bowl."
Audio: night crickets, one low ominous note.
""", [REF_GERALD])

shot("C-9_the-transaction", 7, f"""
{STYLE} {KITCHEN_NIGHT} {MOONEY} {GERALD} The transaction, played exactly like a tense drug deal. Mooney
slides the small empty ceramic bowl across the moonlit windowsill with one paw. GERALD, on the fence side,
inspects the bowl at length, turning it over carefully with his bill. He nods once, slowly. The crumpled
brown paper bag slides the other way across the sill toward Mooney.
EXACTLY ONE CAT AND EXACTLY ONE BIRD. No humans, no other animals.
There is no dialogue in this shot. Nobody speaks.
Audio: ceramic scrape, paper rustle, single tense violin note.
""", [REF_CAST, REF_GERALD])

shot("C-10_eating-in-the-dark", 6, f"""
{STYLE} {KITCHEN_NIGHT} {MOONEY} Mooney crouches under the kitchen table in the dark, hunched low over the
open crumpled paper bag, eating fast. He is guilty and ecstatic at the same time. His eyes dart to the
doorway between bites. EXACTLY ONE CAT. No humans, no bird, no other animals.
There is no dialogue in this shot. Nobody speaks.
Audio: frantic wet chewing, one paranoid pause, chewing resumes.
""", [REF_CAST])

shot("C-11_disappointed", 5, f"""
{STYLE} {KITCHEN_NIGHT} {GARY} GARY the raccoon stands in the dark kitchen doorway in his small round
reading glasses, holding a folded newspaper crossword down at his side. He is not angry. He is calmly,
devastatingly disappointed. He does not move. Only his mouth moves.
EXACTLY ONE RACCOON. No cats, no humans, no bird.
GARY says, {V_GARY}: "I'm not mad. I'm disappointed."
Audio: refrigerator hum, distant clock.
""", [REF_GARY])

shot("C-12_nobody-asked-you-gary", 6, f"""
{STYLE} {KITCHEN_NIGHT} {MOONEY} Mooney under the kitchen table in the dark does not stop eating for even
one second. He speaks around a mouthful of sandwich, cheeks full, entirely unrepentant.
EXACTLY ONE CAT. No humans, no bird, no raccoon, no other animals.
MOONEY says, with his mouth full, {V_MOONEY}: "Nobody asked you, Gary."
Audio: wet chewing, paper rustle.
""", [REF_CAST])

shot("C-13_escalation-montage", 7, f"""
{STYLE} {KITCHEN_NIGHT} {MOONEY} {GERALD} A montage of successive night-time deals at the same moonlit
kitchen window. Mooney pushes objects across the sill one after another: a cat collar, a toy mouse, a
knitted catnip banana, a television remote, a man's wristwatch. On the fence behind GERALD, a growing
hoard of stolen household objects is assembling into a shape that is unmistakably a throne.
EXACTLY ONE CAT AND EXACTLY ONE BIRD. No humans, no other animals.
There is no dialogue in this shot. Nobody speaks.
Audio: repeated ceramic scrapes, paper bags, smug gull call.
""", [REF_CAST, REF_GERALD])

# ---------------- ACT FOUR ----------------
shot("D-1_the-clean-circle", 6, f"""
{STYLE} {KITCHEN_DAY} {RAICHU} Morning. Raichu walks into the kitchen and stops dead, one paw still raised.
On the tiled floor in front of him is a clean, dust-free circle where a bowl used to stand. The camera
pushes in slowly on the empty circle. EXACTLY ONE CAT. No humans, no bird, no other animals.
There is no dialogue in this shot. Nobody speaks.
Audio: one ominous low string, ticking clock.
""", [REF_CAST])

shot("D-2_wheres-your-bowl", 5, f"""
{STYLE} {KITCHEN_DAY} {RAICHU} Close on Raichu in the kitchen, ear tufts rigid, staring off-screen with
dawning suspicion. EXACTLY ONE CAT. No humans, no bird, no other animals.
RAICHU says, {V_RAICHU}: "Where's your bowl."
Audio: faint kitchen room tone, ticking clock.
""", [REF_CAST])

shot("D-3_what-bowl", 4, f"""
{STYLE} {KITCHEN_DAY} {MOONEY} Close on Mooney lying on the kitchen floor, utterly relaxed. Only his mouth
moves. EXACTLY ONE CAT. No humans, no bird, no other animals.
MOONEY says, {V_MOONEY}: "What bowl."
Audio: faint kitchen room tone.
""", [REF_CAST])

shot("D-4_you-had-a-bowl", 6, f"""
{STYLE} {KITCHEN_DAY} {RAICHU} Close on Raichu, absolutely certain and getting louder, leaning in.
EXACTLY ONE CAT. No humans, no bird, no other animals.
RAICHU says, {V_RAICHU}: "You had a bowl."
Audio: faint kitchen room tone.
""", [REF_CAST])

shot("D-5_did-i", 5, f"""
{STYLE} {KITCHEN_DAY} {MOONEY} Close on Mooney on the kitchen floor holding unbroken eye contact with the
camera. Absolutely no shame is visible anywhere on him. Only his mouth moves.
EXACTLY ONE CAT. No humans, no bird, no other animals.
MOONEY says, {V_MOONEY}: "Did I."
Audio: faint kitchen room tone, one deadpan wood block.
""", [REF_CAST])

shot("D-6_the-throne", 7, f"""
{STYLE} {KITCHEN_DAY} {RAICHU} {GERALD} Raichu turns his head very slowly toward the kitchen window.
Through the glass, outside on the fence in daylight, GERALD sits on top of a throne assembled from cat
collars, toys, a television remote and a wristwatch, surveying his territory with total serenity.
EXACTLY ONE CAT AND EXACTLY ONE BIRD. No humans, no other animals.
There is no dialogue in this shot. Nobody speaks.
Audio: triumphant villain brass, one regal gull call.
""", [REF_CAST, REF_GERALD])

shot("D-7_the-collapse", 6, f"""
{STYLE} {FENCE_DAY} {CATS6} The movement collapses. The six neighbourhood cats have discovered the betrayal
and gone completely feral. One screams from a roof ridge. One tears down the little hand-painted banner
with its claws. One has simply lain down flat in the middle of the road and given up. The chart scratched
in the sand has been violently scratched out. No humans, no bird. {NO_TEXT}
There is no dialogue in this shot. Nobody speaks.
Audio: overlapping cat yowls, fabric tearing, distant siren.
""", [REF_CATS6])

shot("D-8_alone-in-the-wreckage", 7, f"""
{STYLE} {FENCE_DAY} {RAICHU} Raichu stands completely alone in the wreckage of his movement, a small whistle
still hanging around his neck, his long ear tufts drooping for the first time. He bends down and picks up a
torn corner of the hand-painted banner and just looks at it. This is a genuinely sad image, played straight.
EXACTLY ONE CAT. No humans, no bird, no other animals. {NO_TEXT}
There is no dialogue in this shot. Nobody speaks.
Audio: everything goes quiet, one sad clarinet, wind.
""", [REF_CAST], chain="D-7_the-collapse")

# ---------------- RESOLUTION ----------------
shot("E-1_i-wanted-to-help", 7, f"""
{STYLE} {DECK_SUNSET} {MOONEY} {RAICHU} The two cats sit side by side on the deck at sunset, both facing out
toward the harbour, neither looking at the other. Warm golden light rims their fur. This is composed and
lit exactly like the sincere final scene of a real animated feature. Play it completely straight - no wink,
no comedy. EXACTLY TWO CATS. No humans, no bird, no other animals.
RAICHU says, {V_RAICHU}: "I just wanted to help you."
Audio: gentle warm strings, distant harbour bell, evening gulls.
""", [REF_CAST])

shot("E-2_i-know", 6, f"""
{STYLE} {DECK_SUNSET} {MOONEY} {RAICHU} The two cats side by side on the deck at sunset, still not looking
at each other. A long, warm, sincere pause before Mooney answers. Strings swell underneath. Played
completely straight and sincere. EXACTLY TWO CATS. No humans, no bird, no other animals.
MOONEY says, {V_MOONEY}: "I know."
Audio: swelling warm strings, distant harbour bell.
""", [REF_CAST])

shot("E-3_i-learned-something", 8, f"""
{STYLE} {DECK_SUNSET} {MOONEY} Mooney turns to face the camera directly at sunset, warm golden light on his
face. This is a completely earnest, heartfelt "I learned something today" speech, delivered with total
sincerity and warmth, as though it were the genuine moral of a children's cartoon. No irony, no wink.
EXACTLY ONE CAT. No humans, no bird, no other animals.
MOONEY says, warmly and sincerely, {V_MOONEY}: "You know, I learned something today. I learned that if you
want something badly enough, and you're willing to lie to everyone who loves you - you can get it."
Audio: fully earnest orchestral strings, evening gulls.
""", [REF_CAST])

shot("E-4_thats-not", 5, f"""
{STYLE} {DECK_SUNSET} {RAICHU} Raichu turns his head sharply toward Mooney, alarmed, starting to object and
getting cut off. EXACTLY ONE CAT. No humans, no bird, no other animals.
RAICHU says, {V_RAICHU}: "That's not-"
Audio: strings continue warmly underneath.
""", [REF_CAST])

shot("E-5_id-do-it-again", 6, f"""
{STYLE} {DECK_SUNSET} {MOONEY} Mooney turns calmly back to face the sunset over the harbour, serene and
content. The music resolves warmly, exactly as though something lovely and heartwarming has just happened.
Played completely straight. EXACTLY ONE CAT. No humans, no bird, no other animals.
MOONEY says, {V_MOONEY}: "And I'd do it again."
Audio: warm resolving strings, distant harbour bell, evening gulls.
""", [REF_CAST])

# ---------------- TEASER ----------------
shot("TZ-1_gary-moves-in", 5, f"""
{STYLE} {LIVING_ROOM} {GARY} GARY the raccoon sits in the worn armchair in his small round reading glasses
with a folded newspaper crossword held in one paw and a pencil in the other - and he is now wearing a cat
collar around his neck. He does not look up from the crossword at any point. EXACTLY ONE RACCOON.
No cats visible, no humans, no bird. {NO_TEXT}
GARY says, without looking up, {V_GARY}: "Next week I move in properly."
Then an unseen cat answers from off-screen, {V_MOONEY}: "This is going to end badly."
Audio: pencil scratch, clock tick, one comic sting.
""", [REF_GARY, REF_LIVINGROOM])

json.dump(S, open("shots.json", "w", encoding="utf-8"), indent=1)
tot = sum(s["dur"] for s in S)
print(f"{len(S)} shots | {tot}s | {tot*3.5:.0f} credits")
for s in S:
    print(f"  {s['key']:<32} {s['dur']}s  refs={len(s['refs'])}  chain={s['chain'] or '-'}")
