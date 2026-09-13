# -*- coding: utf-8 -*-
"""All 61 generated shots of Episode 2 "House Rules", as finished prompts.

    python shots.py             render, validate, write shots_prompts.json
    python shots.py B-6         print one prompt in full

THE ACTION TEXT IS NOT REPEATED HERE. It is imported from ../script.py, so the
script the humans read and the prompts the model gets can never drift apart —
edit a line in the script and the prompt changes with it. What this file adds is
the wrapper the model needs and a script does not: style, location, character
sheets, head-counts, the dialogue cap, the negatives, and the directed audio.

Everything audio comes from blocks.py, which is where the technique out of the
owner's example prompt lives. Per shot this file supplies only:

    location, who is in it, the concrete Foley, and a music override when the
    score changes inside the shot.

The act's score cue, the mix paragraph, the silence-after-the-line and the
no-text negative are all stamped on automatically. Nothing to forget.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))

_cwd = os.getcwd()
import script as SCRIPT          # noqa: E402  (chdirs on import)
os.chdir(_cwd)
from blocks import *             # noqa: E402,F401,F403

M, R, G, B = "MOONEY", "RAICHU", "GARY", "GERALD"
SHEET = {M: MOONEY, R: RAICHU, G: GARY, B: GERALD}
REF = {M: REF_CAST, R: REF_CAST, G: REF_GARY, B: REF_GERALD}

# Head-count line. Ambiguity here is what put Mooney in a crowd shot in Episode 1.
def count(cast):
    """The head count, and it stays SHOUTED.

    Episode 1's rule 2 is an explicit capitalised count in every prompt; D-7 cast
    Mooney as one of six feral cats without it. An earlier version of this
    function ran .capitalize() over the whole line, which quietly lowercased
    EXACTLY ONE CAT on every silent shot until the validator caught it.
    """
    cats = [c for c in cast if c in (M, R)]
    head = {0: "NO CATS IN FRAME AT ALL", 1: "EXACTLY ONE CAT",
            2: "EXACTLY TWO CATS"}[len(cats)]
    tail = [("EXACTLY ONE RACCOON" if G in cast else "no raccoon"),
            ("EXACTLY ONE SEAGULL" if B in cast else "no bird"),
            ("exactly two humans" if "HUMANS" in cast else "no humans")]
    return head + ", " + ", ".join(tail) + ", no other animals."


# code -> (location, cast, foley, music override or None, extra staging or None)
SHOTS = {
 "CO-1": (FRONT_DOOR, (G,), "a tumbler CLUNK, a long door CREEEAK, unhurried footsteps", None,
          "Close on the cat flap at the bottom of the door. The camera does not move."),
 "CO-2": (LOUNGE, (M,), "a clock, faint room tone", None, "Only his mouth moves."),
 "CO-3": (LOUNGE, (R,), "faint room tone, one delighted tail thump", None, None),
 "CO-4": (LOUNGE, (G,), "cardboard, a small glass CLINK, one sentimental harp", None, None),
 "CO-5": (LOUNGE, (M,), "a clock, faint room tone", None, "Only his mouth moves."),

 "A-1":  (LOUNGE, (G,), "cardboard flexing, a small proud pause", None, None),
 "A-2":  (LOUNGE, (M,), "faint room tone", None, "Only his mouth moves."),
 "A-3":  (LOUNGE, (G,), "a wheel ratchet TICK-TICK-TICK slowing to single ticks",
          "the bureaucratic march swelling absurdly for the spin and stopping dead on the last tick", None),
 "A-4":  (LOUNGE, (G,), "one last tick, a page turning", None, None),
 "A-5":  (LOUNGE, (M,), "faint room tone", None, "Only his mouth moves."),
 "A-6":  (LOUNGE, (G,), "a page turning, one small dismissive woodwind note on the last word", None,
          "He does not look up."),
 "A-7":  (LOUNGE, (R,), "eager scrabbling paws on a rug", None, None),
 "A-8":  (LOUNGE, (G,), "the wheel ratchet again, shorter, one final tick", None, None),
 "A-9":  (KITCHEN, (M, R), "running water, one squeaky plate, a clock, no voices at all",
          "the march reduced to one small music-box loop, thin and endless",
          "A STATIC LOCKED-OFF WIDE SHOT held far too long. Both cats stand upright on their hind "
          "legs at the sink wearing tiny aprons, one washing and one drying, and neither ever "
          "looks at the other."),
 "A-10": (LOUNGE, (M,), "faint room tone", None,
          "He turns his head and looks DIRECTLY INTO THE CAMERA LENS and speaks to it."),
 "A-11": (LOUNGE, (R,), "faint room tone, one wounded sniff", None, None),
 "A-12": (LOUNGE, (M,), "faint room tone", None, "Only his mouth moves."),
 "A-13": (LOUNGE, (M,), "a heavy cat getting to his feet, one decisive floorboard creak",
          "the prim march stops dead and one low determined note takes its place", None),

 "B-1":  (FENCE_NIGHT, (R, B), "night crickets through glass, one slow wingbeat", None,
          "Seen from inside the dark kitchen: RAICHU up on the windowsill at the glass, GERALD "
          "outside on the moonlit fence with a small paper bag under one foot."),
 "B-2":  (FENCE_NIGHT, (B,), "night crickets, one low bass note", None, "He does not blink."),
 "B-3":  (FENCE_NIGHT, (R, B), "a collar buckle CHINK on wood, paper rustle, one tense violin note",
          "low noir bass, a deal being done at a window",
          "Close on the windowsill from outside. A cat collar slides one way, a small paper bag "
          "slides the other. Gerald turns the collar over with his bill at length."),
 "B-4":  (LOUNGE, (R,), "a string CREAK, tiptoeing pads, one long held breath", None,
          "The bucket on the door frame and the string must both be clearly visible in frame."),
 "B-5":  (LOUNGE, (G,), "a small CLUNK, SCRITCH SCRITCH of a pencil being sharpened",
          "the scheming pizzicato deflating into one defeated trombone slide",
          "CRITICAL: Gary never looks at the string and never looks up at the bucket. He is not "
          "defeating a trap, he is a man who has found a bucket. No reaction of any kind."),
 "B-6":  (LOUNGE, (M,), "faint room tone", None, "Only his mouth moves."),
 "B-7":  (LOUNGE, ("HUMANS",), "two bins set down on floorboards, one small pleased humming note",
          "the warm domestic music arriving for the first time, on the humans' side",
          "Close on the floor beside the armchair. A woman's HANDS ONLY set a second bin down "
          "beside the first and square them both up. NO FACE IN FRAME, no animal in frame."),
 "B-8":  (HALL, (R,), "a long skittering marble RATTLE across bare boards", None, None),
 "B-9":  (HALL, (G, M), "marbles under a calm unhurried walk, a rising WHOOP, a long comic slide, "
          "a distant CRASH of saucepans",
          "scheming tiptoe pizzicato holding its breath under Gary's walk, then the full chase "
          "orchestra landing a hit exactly on the slip and a cymbal on the off-screen impact",
          LOCKED_TWO + " Straight down the hallway. Gary crosses left to right and fully exits "
          "before Mooney enters. Gary never looks down at the marbles."),
 "B-10": (HALL, (M,), "one settling marble, faint room tone", None,
          "Upside down against the wall with his legs folded over his head, completely calm."),
 "B-11": (HALL, (G,), "a soft brush, marbles pouring into glass, one prim little woodwind phrase",
          "the prim bureaucratic march returning, entirely satisfied with itself",
          "He sweeps, jars, shelves and squares up without once looking at anything but the job."),
 "B-12": (FENCE_NIGHT, (R, B), "night crickets through glass", None,
          "The identical window shot as B-1. Same framing, same night."),
 "B-13": (FENCE_NIGHT, (B,), "night crickets", None, "He does not blink."),
 "B-14": (FENCE_NIGHT, (R, B), "plastic sliding on wood, paper rustle, the same tense violin note",
          "low noir bass, the same deal a second time",
          "Close on the windowsill. A television remote slides one way, a handsaw slides back."),
 "B-15": (LOUNGE, (R,), "rhythmic SHHK SHHK of a handsaw on floorboards",
          "a slowly rising oboe of dramatic irony, entirely aware of what is coming", None),
 "B-16": (LOUNGE, (R, G), "a CRACK, a long descending WHEEEE, a distant THUD",
          "the oboe cutting out on the crack, one comedy timpani hit on the thud",
          "The armchair with Gary in it stays completely motionless while the floor gives way."),
 "B-17": (LOUNGE, (G,), "a page turning", None, "He does not look up."),
 "B-18": (LOUNGE, ("HUMANS",), "a torch click, a happy echo down a hole, one discovery chord",
          "the warm domestic music swelling for a hole in the floor",
          "MICHAEL kneels beside a neat round hole in the floorboards shining a torch into it, "
          "delighted. No animals in frame."),

 "C-1":  (FENCE_NIGHT, (R, B), "night crickets through glass", None,
          "The same window shot for the third time."),
 "C-2":  (FENCE_NIGHT, (B,), "night crickets, one smug gull call", None, "He does not blink."),
 "C-3":  (FENCE_NIGHT, (R, B), "a small avalanche of toys, one bell, paper rustle, a smug gull call",
          "low noir bass at its most pleased with itself",
          "Wide on the windowsill, stacked with a toy mouse, a catnip banana, two collars and a "
          "ball with a bell in it. Raichu pushes the whole pile across with both paws."),
 "C-4":  (LOUNGE, (M, R), "SNAP, SPROING, FWOOMPH, TWANG with three ricochet PINGs, a final BONK",
          "full Tom-and-Jerry chase orchestra running continuously across all four gags with a "
          "musical hit precisely on each impact and a cymbal on the last",
          "A fast comedy montage in one continuous take. EVERY TRAP GOES WRONG FOR THE CAT WHO "
          "SET IT; no raccoon appears at any point. " + beats(
              (0, 3, "a mousetrap the size of a door snaps shut on absolutely nothing, SNAP, and "
                     "both cats stare at it"),
              (3, 6, "quick cut: a rope snare hoists MOONEY up by one back leg, SPROING, and he "
                     "revolves slowly upside down, unbothered"),
              (6, 9, "quick cut: a desk fan catches a burst bag of flour, FWOOMPH, and both cats "
                     "are instantly completely white"),
              (9, 12, "quick cut: RAICHU fires a grape from a slingshot, TWANG, it ricochets off "
                      "three walls, PING PING PING, and comes back and hits him, BONK"))),
 "C-5":  (LOUNGE, (M, R, G), "rope creaking as two cats revolve, one light switch CLICK",
          "the chase orchestra collapsing into a single sad clarinet on the click",
          LOCKED_TWO + " Both cats hang upside down in the doorway, flour-white and wound in the "
          "same rope. Gary steps over them without looking and reaches up out of frame."),
 "C-6":  (LOUNGE_DARK, (M,), "total silence in a dark room, one floorboard settling",
          "no music at all until the very end of the line",
          "Almost complete darkness. Only two pairs of reflective cat eyes are clearly visible."),
 "C-7":  (LOUNGE_DARK, (R,), "total silence in a dark room",
          "one small mad determined note underneath, and nothing else",
          "Almost complete darkness, his eyes catching the light. Absolute certainty."),
 "C-8":  (LOUNGE, (G,), "a clock, a pencil scratch, one warm domestic phrase",
          "the warm domestic music, unhurried, entirely at home",
          "A wide locked-off shot of a spotless sunlit living room that looks like a show home."),
 "C-9":  (LOUNGE, (M,), "faint room tone", None, "He is looking at the room, not at the raccoon."),
 "C-10": (LOUNGE, (R,), "faint room tone", None, "Eyes narrowed at the tidiest room he has seen."),

 "D-1":  (LOUNGE, (G, "HUMANS"), "a camera shutter, warm domestic murmur", None,
          "MICHAEL and LYNDIE stand over the armchair photographing Gary in it. Gary looks at "
          "the camera. He does not smile, but it reads as a smile."),
 "D-2":  (LOUNGE, (M, R), "rope creaking, one long drip, a single fly",
          "the warm domestic music carrying on completely undisturbed, which is the joke",
          LOCKED_TWO + " Both cats flour-white and still tangled in rope in the doorway behind "
          "the humans, dripping onto the floorboards. Nobody in the room turns around."),
 "D-3":  (LOUNGE, (G,), "a camera shutter, warm domestic murmur", None,
          "A woman's voice speaks warmly from off-screen; NOBODY IS VISIBLE SAYING IT and no "
          "human appears in frame. Hold on Gary in the armchair while she speaks."),
 "D-4":  (LOUNGE, (M,), "faint room tone, one rope creak", None,
          "He turns his head and looks DIRECTLY INTO THE CAMERA LENS and speaks to it."),
 "D-5":  (KITCHEN, (G, "HUMANS"), "one coin CHINK on wood, a cash-register DING far too pleased "
          "with itself", None,
          "Close on the counter only. Gary slides a single coin across it with one claw and a "
          "human hand picks it up and pockets it. NEITHER FACE IS IN FRAME - hands and paws only."),
 "D-6":  (LOUNGE, (R,), "faint room tone", None,
          "His ear tufts go flat for the first time in the series."),
 "D-7":  (LOUNGE, (G,), "a pencil scratch, a clock",
          "the warm domestic music at its warmest, entirely on his side",
          "He does not look up. He means it completely kindly."),
 "D-8":  (LOUNGE, (M,), "faint room tone", None, "Only his mouth moves."),
 "D-9":  (LOUNGE, (), "a wheel ratchet TICK-TICK-TICK slowing, one small doomed chime",
          "the bureaucratic march returning, slower and more final",
          "Close on the chore wheel alone, spinning and slowing. It stops on the same wedge."),
 "D-10": (KITCHEN, (M, R), "running water, one squeaky plate, a clock, no voices at all",
          "the same thin little music-box loop from Act One, unchanged",
          "The IDENTICAL shot from Act One: a static locked-off wide, both cats upright at the "
          "sink in aprons, one washing and one drying, neither looking at the other. Too long."),

 "E-1":  (DECK_SUNSET, (M, R), "gentle evening water, a distant harbour bell, evening gulls", None,
          LOCKED_TWO + " Both cats side by side at the wooden railing facing out over the water, "
          "MOONEY on the left and RAICHU on the right, still faintly white with flour. BOTH LOOK "
          "LEVEL AND STRAIGHT AHEAD AT THE HARBOUR - neither looks upward, there is nothing above "
          "them. Raichu speaks without turning his head."),
 "E-2":  (DECK_SUNSET, (M, R), "a distant harbour bell, evening gulls",
          "the earnest strings swelling under a long warm sincere pause",
          LOCKED_TWO + " The same two-shot. Only Mooney's mouth moves; Raichu is still."),
 "E-3":  (DECK_SUNSET, (M,), "evening gulls, gentle water",
          "fully earnest orchestral strings, the whole apparatus of a sincere ending, no wink",
          "Mooney turns to face the camera directly, warm golden light on his face. Played with "
          "total sincerity. HE IS NOT WEARING GLASSES IN THIS SHOT."),
 "E-4":  (DECK_SUNSET, (M, R), "evening gulls, one small surprised woodwind note",
          "the earnest strings faltering very slightly, then carrying on",
          LOCKED_TWO + " A wider two-shot at the rail. MOONEY IS NOW WEARING SMALL ROUND READING "
          "GLASSES exactly like the raccoon's - he was not wearing them a moment ago and no "
          "attention is drawn to how they arrived. He gazes serenely at the harbour while Raichu "
          "stares at him."),
 "E-5":  (DECK_SUNSET, (M,), "evening gulls, one final warm resolving chord", None,
          "Close on Mooney in the reading glasses, looking out at the water. He does not turn "
          "his head."),

 "TZ-1": (LOUNGE, (M, G), "a pencil scratch, a clock, one comic sting",
          "one short bright comic sting as the second armchair registers",
          "TWO matching armchairs side by side where there was one. GARY sits in the left one "
          "with his crossword; MOONEY sits in the right one in identical small round reading "
          "glasses with his own crossword. Neither looks up or reacts. An unseen cat objects "
          "from off-screen; nobody is visible saying it."),
}

SKIP = {"TS-1", "EC-1"}          # reused plates, nothing to generate

# Transitions worth naming. Everything unlisted is an ordinary television cut.
# Smash cuts go into and out of the cutaways, where the discontinuity IS the joke;
# holds go on the beats where the pause is the punchline.
CUTS = {
    "A-9":  "hold",     # the sink, held far too long
    "B-9":  "smash",    # Raichu drops through the floor
    "B-13": "smash",    # into the boat cutaway
    "B-14": "hold",     # the boat, held too long, never explained
    "C-13": "hold",     # the catapult rocking to a stop after they have gone
    "D-5":  "smash",    # the coin
    "D-10": "hold",     # the sink again, identical, held identically
    "E-4":  "hold",     # Gary sits down between them and nobody reacts
}


def strip_html(t):
    return re.sub(r"<[^>]+>", "", t).replace("  ", " ").strip()


def build():
    out = []
    for a in SCRIPT.ACTS:
        for sh in a["shots"]:
            code = sh["code"]
            if code in SKIP:
                continue
            if code not in SHOTS:
                raise SystemExit("no prompt metadata for %s" % code)
            loc, cast, foley, music, staging = SHOTS[code]
            sheets = " ".join(SHEET[c] for c in cast if c in SHEET)

            body = [STYLE, ON_MODEL, ANIMATION, loc, sheets, strip_html(sh["action"])]
            if staging:
                body.append(staging)
            body.append(count(cast))

            if sh["lines"]:
                for who, said in sh["lines"]:
                    name = who.replace(" (off)", "").upper()
                    delivery = {"MOONEY": V_MOONEY, "RAICHU": V_RAICHU,
                                "GARY": V_GARY, "GERALD": V_GERALD}.get(name, "warmly")
                    line = strip_html(said)
                    body.append('%s says, %s: "%s"' % (name, delivery, line))
                if len({w for w, _ in sh["lines"]}) == 1:
                    who = sh["lines"][0][0].replace(" (off)", "").title()
                    body.append(only(" ".join(strip_html(l) for _, l in sh["lines"]), who))
            else:
                body.append(SILENT)

            if code.startswith("B-") or code in ("C-13",):
                body.append(HARMLESS)
            if "HUMANS" in cast:
                body.append(MEOWS)
            if code in CUTS:
                body.append(TRANSITION[CUTS[code]])
            body.append(NO_TEXT)
            body.append(audio(code, foley, music=music))

            refs = []
            for c in cast:
                if c in REF and REF[c] not in refs:
                    refs.append(REF[c])
            if "HUMANS" in cast:
                refs += [REF_MICHAEL, REF_LYNDIE]
            if loc is LOUNGE and REF_LIVINGROOM not in refs:
                refs.append(REF_LIVINGROOM)

            out.append(dict(key=code, dur=sh["dur"], refs=refs[:4],
                            prompt=" ".join(" ".join(body).split())))
    return out


def main():
    shots = build()
    json.dump(shots, open(os.path.join(HERE, "shots_prompts.json"), "w", encoding="utf-8"),
              indent=1)

    if len(sys.argv) > 1:
        for s in shots:
            if s["key"] == sys.argv[1]:
                print("%s  %ds  %.0f credits  refs=%d\n%s\n%s"
                      % (s["key"], s["dur"], s["dur"] * 4.5, len(s["refs"]), "-" * 70, s["prompt"]))
                return
        raise SystemExit("no shot %r" % sys.argv[1])

    # every prompt must carry the things that are easy to forget
    bad = []
    for s in shots:
        p = s["prompt"]
        for must, why in [("Audio professionally mixed", "mix block"),
                          ("Score:", "score cue"),
                          ("NO on-screen text", "text negative"),
                          ("no other animals.", "head count"),
                          ("identical in every shot", "on-model rule"),
                          ("secondary animation", "animation rule")]:
            if must not in p:
                bad.append("%s missing %s" % (s["key"], why))
        if "says," in p and "NOTHING else" not in p and s["key"] != "TZ-1":
            bad.append("%s has dialogue but no cap" % s["key"])
        if "says," not in p and "NO DIALOGUE" not in p.upper():
            bad.append("%s is silent but never says so" % s["key"])
        if "DO NOT FILL EVERY SECOND" not in p:
            bad.append("%s missing the silence rule" % s["key"])
    humans = [x["key"] for x in shots if "two humans" in x["prompt"]]
    for k in humans:
        pr = next(x["prompt"] for x in shots if x["key"] == k)
        if "CANNOT understand" not in pr:
            bad.append("%s has humans in frame but no meows rule" % k)
    if bad:
        raise SystemExit("INCOMPLETE PROMPTS:\n  " + "\n  ".join(bad))

    secs = sum(s["dur"] for s in shots)
    talk = [s for s in shots if "says," in s["prompt"]]
    print("%d prompts | %ds | %.0f credits at 4.5/s" % (len(shots), secs, secs * 4.5))
    print("%d with dialogue, %d silent" % (len(talk), len(shots) - len(talk)))
    print("longest prompt %d chars, shortest %d"
          % (max(len(s["prompt"]) for s in shots), min(len(s["prompt"]) for s in shots)))
    print("every prompt carries the mix block, a score cue, the text negative and a head count")
    print("-> shots_prompts.json")


if __name__ == "__main__":
    main()
