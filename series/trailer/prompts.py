# -*- coding: utf-8 -*-
"""Channel trailer - 30-second cut of LL-BG-Cards/trailer.txt.

Budget decided the length: video is 4.5 credits/second now and the minimum
shot is 4s, so the full 45s script costs ~439. The 30s cut drops the
"bigger adventures" tease block (the weakest section anyway with only one
episode in the can) and lands at 14 shots / 62s / ~279 credits, leaving a
retry budget out of the 327.6 available.

Three rules carried over from Episode 1, all of them learned the hard way:

1. **Every dialogue shot is single-speaker.** `voice_change` converts every
   voice on a track, so a two-shot with both cats talking can never be put on
   the locked voices. The couch exchange is four lines; it is shot as two
   takes of two lines each rather than one two-shot.
2. **The narrator is not generated here.** Narration goes on in post with one
   consistent voice. Ten of the fourteen shots therefore ask for NO dialogue
   at all, which is also the most reliable thing this model does.
3. **Every spoken line is capped** with `only()` - exact words, nothing else.
   Without it Seedance invents a second sentence to fill the shot.

The reveal card is built locally (`card.py`), not generated: navy/cream/gold,
the logo sticker, and the subscribe line. Free.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', 'ep02-chonk', 'prompts'))
from blocks import STYLE, MOONEY, RAICHU, REF_CAST     # noqa: E402

S = []
def shot(key, dur, prompt, refs):
    S.append(dict(key=key, dur=dur, prompt=" ".join(prompt.split()), refs=refs))

# Byte-identical per room, every shot (rule 1). The living room in blocks.py
# has an armchair - the trailer needs a couch, so it gets its own block and
# every trailer shot in that room uses this exact string.
LOUNGE = (
    "LOCATION: INTERIOR, INSIDE THE HOUSE - the living room of a Cape Cod cottage. "
    "A worn upholstered couch with soft cushions, a side table with a lamp, a rug, "
    "a window with morning sunlight coming through it. "
    "THIS SHOT IS ENTIRELY INDOORS: do not show deck boards, do not show grey shingle siding, "
    "do not show a garden, do not show sky or harbour."
)

KITCHEN = (
    "LOCATION: INTERIOR, INSIDE THE HOUSE - the kitchen of a Cape Cod cottage. "
    "Painted shaker cabinets, a wooden countertop, tiled floor, a window over the sink, warm indoor light. "
    "THIS SHOT IS ENTIRELY INDOORS: do not show deck boards, do not show grey shingle siding, "
    "do not show a garden, do not show sky or harbour."
)

V_MOONEY = "in a deep, slow, gravelly, half-asleep drawl"
V_RAICHU_CLEAR = ("in a bright, eager, boyish voice at a normal speaking pitch - "
                  "quick but CLEARLY ARTICULATED, every word crisp and easy to understand, "
                  "not squeaky, not shrill, not mumbled, not rushed together")

SILENT = ("THERE IS NO DIALOGUE IN THIS SHOT. Nobody speaks, nobody talks, "
          "no voice is heard, no words are spoken at any point.")

def only(words):
    return ("He says EXACTLY these words and NOTHING else: \"%s\" "
            "He speaks no other words at any point in this shot. No second sentence, "
            "no muttering, no whispering, no trailing off, no ad-libbed dialogue, "
            "and he does not say anyone's name unless it is in that line. "
            "Before and after that one line he is completely silent." % words)

# Both cats in frame is the highest-risk shot type this pipeline has - Episode 1's
# physical comedy was all single-cat or montage for that reason. Rule 11 in full
# on every one of them.
LOCKED_TWO = ("A STATIC LOCKED-OFF WIDE SHOT. BOTH CATS REMAIN FULLY INSIDE THE FRAME "
              "FOR THE ENTIRE SHOT - neither cat leaves frame, neither cat is cropped off "
              "at the edge. EXACTLY TWO CATS. No humans, no bird, no other animals.")

ONE_CAT = "EXACTLY ONE CAT. No humans, no bird, no other animals."

# ---------------- 0-5s: THE PERFECT DAY (narration in post) ----------------
shot("T-1_meet-mooney", 4, f"""
{STYLE} {LOUNGE} {MOONEY} Mooney is sprawled on his side across the couch cushions, fast asleep,
one paw hanging off the edge, belly rising and falling slowly. A warm shaft of morning sunlight
lies across him. The camera is locked off and slowly, almost imperceptibly, pushes in.
{ONE_CAT} {SILENT}
Audio: birdsong outside the window, a soft ticking clock, gentle peaceful music.
""", [REF_CAST])

shot("T-2_one-eye", 4, f"""
{STYLE} {LOUNGE} {MOONEY} Close on Mooney's face asleep on the couch cushion. He slowly opens ONE
eye, just one, and looks flatly at the camera without moving anything else. The other eye stays shut.
{ONE_CAT} {SILENT}
Audio: birdsong, gentle peaceful music, one soft comic woodwind note.
""", [REF_CAST])

shot("T-3_treats", 5, f"""
{STYLE} {LOUNGE} {MOONEY} Mooney eats a small treat off the rug with great contentment, chews twice,
then immediately flops back down onto his side and shuts his eyes, entirely satisfied.
{ONE_CAT} {SILENT}
Audio: happy crunching, a contented sigh, gentle peaceful music.
""", [REF_CAST])

# ---------------- 5-10s: AND THEN THERE'S RAICHU ----------------
shot("T-4_raichu-peeks", 5, f"""
{STYLE} {LOUNGE} {RAICHU} Raichu peers around the edge of a doorway into the living room, only his
head and one paw visible past the door frame. His eyes go wide as he spots something off-screen,
and a slow mischievous grin spreads across his face. His ear tufts prick straight up.
{ONE_CAT} {SILENT}
Audio: the music stops dead, one rising suspense note, a single mischievous plucked string.
""", [REF_CAST])

shot("T-5_crouch", 4, f"""
{STYLE} {LOUNGE} {RAICHU} Raichu crouches low to the rug in a hunting stance, shoulders down,
haunches up, eyes locked forward, tail tip twitching fast. He wiggles his back end once,
about to pounce. {ONE_CAT} {SILENT}
Audio: a tense drum roll building, tail swish, one comic timpani hit.
""", [REF_CAST])

# ---------------- 10-20s: CHAOS ----------------
shot("T-6_launch", 4, f"""
{STYLE} {LOUNGE} {RAICHU} Raichu launches himself off the rug and streaks across the living room in
a blur of fur. Behind him a table lamp rocks violently back and forth on the side table and does not
quite fall over. {ONE_CAT} {SILENT}
Audio: a fast whoosh, scrabbling claws on rug, a lamp wobbling, chaotic comedy music starting.
""", [REF_CAST])

shot("T-7_eyes-open", 4, f"""
{STYLE} {LOUNGE} {MOONEY} Extreme close-up on Mooney asleep. Both of his eyes SNAP wide open at once,
pupils huge, absolutely alarmed. He does not move anything except his eyes.
{ONE_CAT} {SILENT}
Audio: one sharp orchestral stab, a crash somewhere off-screen.
""", [REF_CAST])

shot("T-8_kitchen-chase", 5, f"""
{STYLE} {KITCHEN} {RAICHU} {MOONEY} {LOCKED_TWO} RAICHU tears across the kitchen floor from left to
right carrying a stolen sock in his mouth, ears flat, going flat out. MOONEY thunders after him a
moment later, heavy and furious and much slower, paws skidding on the tiles. The camera does not move
and both cats cross the frame within it. {SILENT}
Audio: skittering claws on tile, heavy galloping, frantic chase music.
""", [REF_CAST])

shot("T-9_box-tumble", 4, f"""
{STYLE} {LOUNGE} {RAICHU} {MOONEY} {LOCKED_TWO} A large cardboard box sits on the rug. It rocks, tips
over onto its side, and BOTH CATS tumble out of it together in a tangle of legs and tails and come to
rest sprawled on the rug, blinking. {SILENT}
Audio: cardboard scraping, a soft thump, one comic slide whistle, cymbal.
""", [REF_CAST])

shot("T-10_why-do-i-follow", 5, f"""
{STYLE} {LOUNGE} {MOONEY} Close on Mooney sitting on the rug facing camera, fur completely dishevelled,
staring off-screen with total flat exhaustion. Only his mouth moves. {ONE_CAT}
MOONEY says, {V_MOONEY}: "Why do I keep following you?"
{only("Why do I keep following you?")}
Audio: faint room tone, the chase music winding down.
""", [REF_CAST])

shot("T-11_because-its-fun", 4, f"""
{STYLE} {LOUNGE} {RAICHU} Close on Raichu sitting upright on the rug facing camera, delighted with
himself, ear tufts high, beaming. {ONE_CAT}
HE STARTS TALKING IMMEDIATELY - the line begins in the first half second.
RAICHU says, {V_RAICHU_CLEAR}: "Because it's fun!"
{only("Because it's fun!")}
Audio: faint room tone, one bright cheerful music sting.
""", [REF_CAST])

# ---------------- 20-27s: THE PUNCHLINE ----------------
shot("T-12_couch-settle", 4, f"""
{STYLE} {LOUNGE} {MOONEY} Mooney climbs back onto the couch, turns around once, settles down heavily
into the cushions, lets out a long contented sigh and closes both eyes. Everything is peaceful again.
{ONE_CAT} {SILENT}
Audio: a long contented sigh, cushions creaking, the gentle peaceful music returning.
""", [REF_CAST])

shot("T-13_i-have-an-idea", 5, f"""
{STYLE} {LOUNGE} {RAICHU} Raichu slowly rises up from behind the back of the couch until only his eyes
and ear tufts show above it, then a little further. He is whispering, conspiratorial and thrilled.
{ONE_CAT} No other cat is visible in this shot.
RAICHU says, {V_RAICHU_CLEAR}, in an excited whisper: "Mooney. I have an idea."
{only("Mooney. I have an idea.")}
Audio: a quiet room, one small suspense note.
""", [REF_CAST])

shot("T-14_oh-no", 5, f"""
{STYLE} {LOUNGE} {MOONEY} Close on Mooney lying on the couch with his eyes shut. He says one flat word
without opening them. Then, a beat later, BOTH EYES SNAP OPEN and he says the second line with dawning
horror. Only his mouth and eyes move. {ONE_CAT}
MOONEY says, {V_MOONEY}: "No." Then after a pause, eyes wide open: "Oh, no."
{only("No. ... Oh, no.")}
Audio: a quiet room, one comic sting on the eye-snap.
""", [REF_CAST])

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    json.dump(S, open(os.path.join(here, "trailer.json"), "w", encoding="utf-8"), indent=1)
    tot = sum(s["dur"] for s in S)
    spoken = [s["key"] for s in S if "says," in s["prompt"]]
    print("%d shots | %ds | %.0f credits" % (len(S), tot, tot * 4.5))
    print("%d spoken (1 credit each to revoice): %s" % (len(spoken), ", ".join(spoken)))
    for s in S:
        print("  %-26s %ds" % (s["key"], s["dur"]))
