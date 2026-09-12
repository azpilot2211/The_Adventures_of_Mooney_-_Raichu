# -*- coding: utf-8 -*-
"""Round-two shots for Episode 1 'Chonk' - the owner's change list of 2026-09-11.

Seven re-shoots. Six of them exist because of one newly-diagnosed failure mode,
written up here because it will bite House Rules too:

    Seedance PADS A SHORT LINE WITH INVENTED SPEECH.

Measured with a voiced-span map (qa/speech_map.py): A-8 carries the scripted
word "And?" plus a second, unscripted utterance 3.4s in. B-10 speaks its line
at 1.4s and then mutters for another 1.2s. D-4 has three utterances where the
script has one. C-7 opens by calling the seagull "Mooney". Every one of the
owner's "I don't understand what he's saying" notes is this, not the voice.

So each line below is capped: exact words, nothing else, silent either side.
The other lesson from the first pass (HANDOFF rule 4) applies too - the
adjectives in the voice description drive the delivery harder than any
reference clip, and "high-pitched excitable squeak" was itself producing the
squeaky garble the owner could not parse. Raichu is revoiced to Miles
afterwards anyway, so what this asks for is ARTICULATION, not pitch.
"""
import json
from blocks import *

S = []
def shot(key, dur, prompt, refs, chain=None):
    S.append(dict(key=key, dur=dur, prompt=" ".join(prompt.split()), refs=refs, chain=chain))

# New location block - the cold open's car was shot before blocks.py existed.
CAR = (
    "LOCATION: INTERIOR of a car - the back seat, where a grey plastic pet carrier is strapped in place. "
    "Dark upholstery, soft daylight through the side windows. "
    "THIS SHOT IS ENTIRELY INSIDE THE CAR: do not show a kitchen, do not show a garden, "
    "do not show any room of a house."
)

# E-2's own frame, uploaded 2026-09-11, so the re-shot E-1 and E-4 sit at the
# rail facing the harbour like the rest of the E run instead of against the wall.
REF_E2_STAGING = "3fc8ede1-523f-458b-a8b4-d09afe28a827"

# Replaces V_RAICHU for every re-shoot. Same character, asked for clarity
# instead of pitch; see the module docstring.
V_RAICHU_CLEAR = ("in a bright, eager, boyish voice at a normal speaking pitch - "
                  "quick but CLEARLY ARTICULATED, every word crisp and easy to understand, "
                  "not squeaky, not shrill, not mumbled, not rushed together")

def only(words):
    """The cap. Without it the model invents a second sentence to fill the shot."""
    return ("He says EXACTLY these words and NOTHING else: \"%s\" "
            "He speaks no other words at any point in this shot. No second sentence, "
            "no muttering, no whispering, no trailing off, no ad-libbed dialogue, "
            "and he does not say anyone's name. "
            "Before and after that one line he is completely silent." % words)

# ---------------- COLD OPEN ----------------
# Owner: "voice is messed up and cuts off before he ends."
# Confirmed: speech runs to within 0.06s of the clip end. Michael's off-screen
# line is dropped so the shot becomes Mooney-solo and voice_change can reach it
# (voice_change converts EVERY voice on the track). CO-1 already establishes
# "She said structurally", so the joke survives.
shot("CO-2_carrier", 6, f"""
{STYLE} {CAR} {MOONEY} Mooney's face fills the barred grille door of the pet carrier on the back seat,
both green eyes level and completely unimpressed, whiskers against the bars. The camera is locked off and
close on the carrier door. Only his mouth moves; the rest of him is completely still.
EXACTLY ONE CAT. No humans in frame, no bird, no other animals.
NOBODY ELSE SPEAKS IN THIS SHOT - there is no second voice, no driver, no voice from off-screen.
HE STARTS TALKING IMMEDIATELY - the line begins within the first half second - and he finishes the whole
sentence with well over a second of silence to spare before the shot ends. The sentence is never cut off.
MOONEY says, {V_MOONEY}: "I'd like to see her jump onto a counter."
{only("I'd like to see her jump onto a counter.")}
Audio: car interior rumble, faint road noise.
""", [REF_CAST])

# ---------------- ACT ONE ----------------
# Owner: "right after Mooney says 'You were supposed to watch the door' I don't
# know what Raichu is saying and his voice is high pitched."
shot("A-8_and", 4, f"""
{STYLE} {KITCHEN_DAY} {RAICHU} Raichu sits upright on the kitchen floor facing camera, tail curled round
his feet, giving one flat unimpressed blink. He is entirely unbothered. After the single word he simply
holds the stare in silence and does not move. EXACTLY ONE CAT. No humans, no bird, no other animals.
HE STARTS TALKING IMMEDIATELY - the word comes in the first half second.
RAICHU says, {V_RAICHU_CLEAR}: "And?"
{only("And?")}
Audio: faint kitchen room tone.
""", [REF_CAST])

# Owner: "'look now Garys fine.' correct punctuation so it flows better."
# The clip delivers it in six chopped pieces. Same words, one breath.
shot("A-11_garys-fine", 4, f"""
{STYLE} {KITCHEN_DAY} {RAICHU} Close on Raichu in the kitchen, completely relaxed and entirely unbothered,
brushing the whole subject away. EXACTLY ONE CAT. No humans, no bird, no other animals.
HE STARTS TALKING IMMEDIATELY - the line begins in the first half second.
RAICHU says, {V_RAICHU_CLEAR}: "Look, Gary's fine."
He says it as ONE SMOOTH CASUAL SENTENCE in a single breath, lightly and quickly, not word by word,
with no pause in the middle and no dragging.
{only("Look, Gary's fine.")}
Audio: faint kitchen room tone.
""", [REF_CAST])

# ---------------- ACT TWO ----------------
# Owner: "after he says that he looks up and i don't understand what he says."
# The clip speaks its line at 1.4s and then mutters for another 1.2s.
shot("B-10_nobodys-told-you", 4, f"""
{STYLE} {FENCE_DAY} {RAICHU} Raichu stands on the grass below the weathered fence looking UP at the cats
sitting on it, his confidence faltering for the first time. His ear tufts twitch. He asks one small
uncertain question and then stands there in silence, waiting for an answer that does not come.
EXACTLY ONE CAT. No humans, no bird, no other animals.
RAICHU says, {V_RAICHU_CLEAR}: "Nobody's told you?"
{only("Nobody's told you?")}
Audio: wind, one distant gull.
""", [REF_CAST])

# ---------------- ACT FOUR ----------------
# Owner: "after he askes what happened to your bowl, his next dialog isn't clear."
# Three separate utterances in the clip where the script has one line.
shot("D-4_you-had-a-bowl", 5, f"""
{STYLE} {KITCHEN_DAY} {RAICHU} Close on Raichu in the kitchen, absolutely certain, leaning in toward
Mooney off-screen and getting louder. He says one accusing sentence and then stops dead, holding the
stare. EXACTLY ONE CAT. No humans, no bird, no other animals.
RAICHU says, {V_RAICHU_CLEAR}: "You had a bowl."
He lands each of those four words clearly and separately, like an accusation.
{only("You had a bowl.")}
Audio: faint kitchen room tone.
""", [REF_CAST])

# ---------------- RESOLUTION ----------------
# Owner: "when he says 'I was only trying to help' hes looking at the sky."
# Confirmed from frames: the existing clip stages both cats against the shingle
# wall looking UP at nothing, which also breaks continuity with E-2/E-4/E-5,
# all of which sit them at the rail facing the harbour.
shot("E-1_i-wanted-to-help", 7, f"""
{STYLE} {DECK_SUNSET} {MOONEY} {RAICHU} A STATIC LOCKED-OFF WIDE TWO-SHOT from behind and slightly to the
side: the two cats sit side by side on the deck at the wooden railing, MOONEY on the left and RAICHU on
the right, BOTH FACING OUT ACROSS THE WATER at the sunset over the harbour, fishing boats and moored masts
soft in the distance. Warm golden light rims their fur. BOTH CATS REMAIN FULLY INSIDE THE FRAME FOR THE
ENTIRE SHOT. BOTH CATS LOOK LEVEL AND STRAIGHT AHEAD OUT AT THE HARBOUR - neither cat looks upward, neither
cat looks at the sky, there is nothing above them and nothing in the air to look at. Raichu speaks quietly
without turning his head, still looking at the water. This is composed and lit exactly like the sincere
final scene of a real animated feature. Play it completely straight - no wink, no comedy.
EXACTLY TWO CATS. No humans, no bird, no other animals.
RAICHU says, {V_RAICHU_CLEAR}, quietly and sincerely: "I just wanted to help you."
{only("I just wanted to help you.")}
Audio: gentle warm strings, distant harbour bell, evening gulls.
""", [REF_E2_STAGING, REF_CAST])

# Owner: "before Mooney says 'I'd do it again', Raichu starts to say something
# and is cut off." The clip says "Racy?" - the script's em-dash gave the model
# nothing to say, so it invented a word. He now gets a whole short sentence,
# clearly spoken; E-5 does the interrupting, in the edit, where it is reliable.
shot("E-4_thats-not", 6, f"""
{STYLE} {DECK_SUNSET} {MOONEY} {RAICHU} The same static wide two-shot on the deck at sunset, MOONEY on the
left and RAICHU on the right, both sitting at the wooden railing facing out over the harbour.
RAICHU TURNS HIS HEAD SIDEWAYS TO LOOK DIRECTLY AT MOONEY BESIDE HIM, alarmed, objecting - he does NOT look
upward, there is nothing above him. Mooney keeps facing the sunset and does not react at all.
BOTH CATS REMAIN FULLY INSIDE THE FRAME FOR THE ENTIRE SHOT. EXACTLY TWO CATS. No humans, no bird,
no other animals. ONLY RAICHU SPEAKS - Mooney says nothing whatsoever in this shot.
RAICHU says, {V_RAICHU_CLEAR}, urgently and very clearly: "That's not the lesson."
{only("That's not the lesson.")}
Audio: warm strings continuing underneath, distant harbour bell.
""", [REF_E2_STAGING, REF_CAST])

if __name__ == "__main__":
    json.dump(S, open("refix.json", "w", encoding="utf-8"), indent=1)
    tot = sum(s["dur"] for s in S)
    print(f"{len(S)} shots | {tot}s | {tot*3.5:.0f} credits")
    for s in S:
        print(f"  {s['key']:<32} {s['dur']}s  refs={len(s['refs'])}")
