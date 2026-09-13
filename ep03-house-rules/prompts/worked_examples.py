# -*- coding: utf-8 -*-
"""Three shots written out in full, to settle what the new audio direction looks
like before all sixty-three get written.

One dialogue shot, one action shot, and the montage as time-coded beats. Run it
to print the prompts; diff them against ep02-chonk/prompts/shots.py to see the
difference the example prompt made.

    python worked_examples.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blocks import *          # noqa: F401,F403

OUT = []


def show(key, dur, prompt, refs, why):
    OUT.append((key, dur, " ".join(prompt.split()), refs, why))


# ---------------------------------------------------------------- dialogue
# The audio job here is the opposite of the action shots: get out of the way.
# "The score drops away under the line and stops on it" comes from only().
show("A-6_thats-not-on-the-wheel", 5, f"""
{STYLE} {LOUNGE} {GARY} Close on Gary in the battered armchair, reading glasses on, not looking
up from the cardboard wheel in his paws. He is kind about it, which is worse. Only his mouth
moves. EXACTLY ONE RACCOON. No cats in frame, no humans, no bird. {NO_TEXT}
HE STARTS TALKING IMMEDIATELY - the line begins in the first half second.
GARY says, {V_GARY}: "That's not on the wheel."
{only("That's not on the wheel.", "Gary")}
{audio("A-6", "a page turning", "a clock", "one small dismissive woodwind note on the last word")}
""", [REF_GARY, REF_LIVINGROOM],
     "Dialogue: SFX stay tiny, the score ducks and stops on the punchline, silence is asked "
     "for by name rather than only forbidden.")

# ---------------------------------------------------------------- action
# Every impact gets its own capitalised effect at the moment it lands, and the
# score is told to hit with them rather than just 'be comedic'.
show("B-6_the-marbles", 7, f"""
{STYLE} {HALL} {GARY} {MOONEY} {LOCKED_TWO} EXACTLY ONE RACCOON AND ONE CAT. No humans, no bird.
Locked-off wide straight down the hallway. GARY strolls across a floor covered in scattered
marbles without once looking down, paws behind his back, entirely level, and exits the far end.
A beat of nothing. Then MOONEY steps into the hall, WHOOP, goes straight up into the air with all
four legs out, and SKKKRRT, slides the entire length of the floorboards and out of frame. CRASH,
a distant collapse of saucepans. {HARMLESS} {SILENT} {NO_TEXT}
{audio("B-6", "marbles skittering under a calm unhurried walk", "one rising WHOOP as the cat goes up",
       "a long comic slide", "a distant CRASH of saucepans",
       music="scheming tiptoe pizzicato holding its breath under Gary's walk, then the full "
             "Tom-and-Jerry chase orchestra landing a hit exactly on the slip and a cymbal "
             "crash on the off-screen impact")}
""", [REF_CAST, REF_GARY],
     "Action: SFX inline in capitals on the beat, the score told to hit WITH the gag, and the "
     "harmless-slapstick hedge on the most refusal-prone act in the episode.")

# ---------------------------------------------------------------- beat blocks
# The example carries four beats in one 15-second take by time-coding them. This
# is the montage the script asks for, written that way.
show("B-11_the-montage", 12, f"""
{STYLE} {LOUNGE} {RAICHU} {MOONEY} A fast comedy montage in one continuous take, four gags, each
landing cleanly on its own beat. EXACTLY TWO CATS. No humans, no bird, no raccoon in frame.
{beats(
  (0, 3, "a mousetrap the size of a door snaps shut on absolutely nothing, SNAP, and the cats "
         "stare at it"),
  (3, 6, "quick cut: a rope snare hoists MOONEY up by one back leg, SPROING, and he revolves "
         "slowly upside down, entirely unbothered"),
  (6, 9, "quick cut: a desk fan catches a burst bag of flour, FWOOMPH, and both cats are "
         "instantly completely white"),
  (9, 12, "quick cut: RAICHU fires a grape from a slingshot, TWANG, it ricochets off three walls, "
          "PING PING PING, and comes straight back and hits him, BONK"))}
{HARMLESS} {SILENT} {NO_TEXT}
{audio("B-11", "SNAP", "SPROING", "FWOOMPH", "TWANG and three ricochet PINGs", "a final BONK",
       music="full Tom-and-Jerry chase orchestra running continuously across all four gags with "
             "a musical hit precisely on each impact and a cymbal on the last one")}
""", [REF_CAST],
     "Beat blocks: four gags pinned to their own seconds in one take. Buys reliability and "
     "comic rhythm, not credits - cost is per second either way - but a trap and its payoff "
     "can no longer be generated as two takes that fail to match.")


if __name__ == "__main__":
    for key, dur, prompt, refs, why in OUT:
        print("=" * 78)
        print("%s   %ds   %.0f credits   refs=%d" % (key, dur, dur * 4.5, len(refs)))
        print("why: %s" % why)
        print("-" * 78)
        print(prompt)
        print()
    print("=" * 78)
    print("%d shots, %ds, %.0f credits to test the technique before writing the other sixty."
          % (len(OUT), sum(d for _, d, _, _, _ in OUT),
             sum(d for _, d, _, _, _ in OUT) * 4.5))
