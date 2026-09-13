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

 "B-1":  (LOUNGE, (R,), "a claw tapping cardboard, conspiratorial breathing", None, None),
 "B-2":  (LOUNGE, (R,), "a string CREAK, tiptoeing pads, one long held breath", None,
          "The bucket and the string must both be clearly visible in the same frame."),
 "B-3":  (LOUNGE, (G,), "a small CLUNK, SCRITCH SCRITCH of a pencil being sharpened",
          "the scheming pizzicato deflating into one defeated trombone slide", None),
 "B-4":  (LOUNGE, (M,), "faint room tone", None, "Only his mouth moves."),
 "B-5":  (HALL, (R,), "a long skittering marble RATTLE across bare boards", None, None),
 "B-6":  (HALL, (G, M), "marbles under a calm unhurried walk, a rising WHOOP, a long comic slide, "
          "a distant CRASH of saucepans",
          "scheming tiptoe pizzicato holding its breath under Gary's walk, then the full chase "
          "orchestra landing a hit exactly on the slip and a cymbal on the off-screen impact",
          LOCKED_TWO + " Shot straight down the hallway; Gary crosses left to right and exits "
          "before Mooney enters."),
 "B-7":  (HALL, (M,), "one settling marble, faint room tone", None,
          "He is upside down against the wall with his legs folded over his head and is completely calm."),
 "B-8":  (LOUNGE, (R,), "rhythmic SHHK SHHK of a handsaw on floorboards",
          "a slowly rising oboe of dramatic irony, entirely aware of what is about to happen", None),
 "B-9":  (LOUNGE, (R, G), "a CRACK, a long descending WHEEEE, a distant THUD",
          "the oboe cutting out on the crack, one comedy timpani hit on the thud",
          "The armchair with Gary in it must remain completely motionless while the floor gives way."),
 "B-10": (LOUNGE, (G,), "a page turning", None, "He does not look up."),
 "B-11": (LOUNGE, (M, R), "SNAP, SPROING, FWOOMPH, TWANG with three ricochet PINGs, a final BONK",
          "full Tom-and-Jerry chase orchestra running continuously across all four gags with a "
          "musical hit precisely on each impact and a cymbal on the last",
          "A fast comedy montage in one continuous take, four gags, each landing cleanly on its "
          "own beat. " + beats(
              (0, 3, "a mousetrap the size of a door snaps shut on absolutely nothing, SNAP"),
              (3, 6, "quick cut: a rope snare hoists MOONEY up by one back leg, SPROING, and he "
                     "revolves slowly upside down, unbothered"),
              (6, 9, "quick cut: a desk fan catches a burst bag of flour, FWOOMPH, and both cats "
                     "are instantly completely white"),
              (9, 12, "quick cut: RAICHU fires a grape from a slingshot, TWANG, it ricochets off "
                      "three walls, PING PING PING, and comes back and hits him, BONK"))),
 "B-12": (LOUNGE, (M, R, G), "rope creaking as two cats revolve, one light switch CLICK",
          "the chase orchestra collapsing into a single sad clarinet on the click",
          LOCKED_TWO + " Both cats hang upside down in the doorway, flour-white and wound in the "
          "same rope; Gary steps over them and reaches up out of frame for the switch."),
 "B-13": (LOUNGE_DARK, (M,), "total silence in a dark room, one floorboard settling",
          "no music at all until the very end of the line",
          "Almost complete darkness. Only two pairs of reflective cat eyes are clearly visible."),
 "B-14": (BOAT, (M, R), "gulls, one oar dipping, water, a resigned accordion",
          "a small resigned accordion waltz, entirely unexplained",
          LOCKED_TWO + " Raichu rows with ONE oar so the boat turns slowly in a circle. Mooney "
          "sits in the bow facing forward. Neither reacts to anything. Held too long."),

 "C-1":  (FENCE_NIGHT, (B,), "night crickets, one slow wingbeat", None,
          "Seen from inside the dark kitchen looking out through the window at the moonlit fence."),
 "C-2":  (KITCHEN_NIGHT, (M,), "night crickets through glass, refrigerator hum", None, None),
 "C-3":  (FENCE_NIGHT, (B,), "night crickets, one low bass note", None, "He does not blink."),
 "C-4":  (KITCHEN_NIGHT, (M,), "refrigerator hum", None, "Only his mouth moves."),
 "C-5":  (FENCE_NIGHT, (B,), "a long canvas SHHHHP, crickets resuming",
          "one enormous orchestral reveal chord, then back to low noir bass", None),
 "C-6":  (KITCHEN_NIGHT, (M,), "refrigerator hum", None, "Only his mouth moves."),
 "C-7":  (FENCE_NIGHT, (B,), "night crickets", None, "He does not blink."),
 "C-8":  (KITCHEN_NIGHT, (M,), "refrigerator hum", None, "Only his mouth moves."),
 "C-9":  (FENCE_NIGHT, (B,), "night crickets, one low ominous note", None, "He does not blink."),
 "C-10": (KITCHEN_NIGHT, (M,), "refrigerator hum, one small resigned note", None, None),
 "C-11": (GARDEN, (M, R), "ratchet CLICKs, rope creak, two cats straining, a stone CLUNK",
          "low noir bass giving way to a rising comic build",
          LOCKED_TWO + " Dawn light. The catapult must be fully inside frame with both cats."),
 "C-12": (GARDEN, (R,), "one rope creaking under tension", None, "One paw on the release."),
 "C-13": (GARDEN, (M, R, G), "a rope TWANG, a WHUMP, two howls dopplering away, two distant SPLASHES",
          "the comic build reaching its peak and cutting to nothing but crickets on the splashes",
          "A STATIC LOCKED-OFF VERY WIDE SHOT of the whole garden. The catapult arm swings the "
          "WRONG WAY and both cats are launched straight out of the top of frame. The catapult "
          "is undamaged and rocks gently to a stop. Behind it, in the lit kitchen window, GARY "
          "is small in frame and does not look up."),

 "D-1":  (LOUNGE, (G, "HUMANS"), "a camera shutter, warm domestic murmur", None,
          "MICHAEL and LYNDIE stand over the armchair photographing Gary in it. Gary looks at "
          "the camera. He does not smile, but it reads as a smile."),
 "D-2":  (LOUNGE, (M, R), "steady dripping, one long SQUELCH, a single fly",
          "the warm domestic music carrying on completely undisturbed, which is the joke",
          LOCKED_TWO + " Both cats soaked through and draped in seaweed, dripping onto the "
          "floorboards in the doorway. Nobody in the room turns around."),
 "D-3":  (LOUNGE, (G,), "a camera shutter, warm domestic murmur", None,
          "A woman's voice speaks warmly from off-screen; NOBODY IS VISIBLE SAYING IT and no "
          "human appears in frame. Hold on Gary in the armchair while she speaks."),
 "D-4":  (LOUNGE, (M,), "water running off a soaked cat onto floorboards", None,
          "He turns his head and looks DIRECTLY INTO THE CAMERA LENS and speaks to it, harbour "
          "water still running off his chin."),
 "D-5":  (KITCHEN, (G, "HUMANS"), "one coin CHINK on wood, a cash-register DING far too pleased "
          "with itself", None,
          "Close on the counter only. Gary slides a single coin across it with one claw and a "
          "human hand picks it up and pockets it. NEITHER FACE IS IN FRAME - hands and paws only."),
 "D-6":  (LOUNGE, (R,), "faint room tone", None,
          "His ear tufts go flat for the first time in the series."),
 "D-7":  (LOUNGE, (G,), "a pencil scratch, a clock",
          "the warm domestic music at its warmest, entirely on his side", "He does not look up."),
 "D-8":  (LOUNGE, (M,), "faint room tone", None, "Only his mouth moves."),
 "D-9":  (LOUNGE, (), "a wheel ratchet TICK-TICK-TICK slowing, one small doomed chime",
          "the bureaucratic march returning, slower and more final",
          "Close on the chore wheel alone, spinning and slowing. It stops on the same wedge."),
 "D-10": (KITCHEN, (M, R), "running water, one squeaky plate, a clock, no voices at all",
          "the same thin little music-box loop from Act One, unchanged",
          "The IDENTICAL shot from Act One: a static locked-off wide, both cats upright at the "
          "sink in aprons, one washing and one drying, neither looking at the other. Held too long."),

 "E-1":  (DECK_SUNSET, (M, R), "gentle evening water, a distant harbour bell, evening gulls", None,
          LOCKED_TWO + " Both cats sit side by side at the wooden railing facing out over the "
          "water, MOONEY on the left and RAICHU on the right, still damp, one strand of seaweed "
          "on Raichu's ear. BOTH LOOK LEVEL AND STRAIGHT AHEAD AT THE HARBOUR - neither looks "
          "upward, there is nothing above them. Raichu speaks without turning his head."),
 "E-2":  (DECK_SUNSET, (M, R), "a distant harbour bell, evening gulls",
          "the earnest strings swelling under a long warm sincere pause",
          LOCKED_TWO + " The same two-shot at the railing. Only Mooney's mouth moves; Raichu is "
          "still. Neither looks at the other."),
 "E-3":  (DECK_SUNSET, (M,), "evening gulls, gentle water",
          "fully earnest orchestral strings, the whole apparatus of a sincere ending, no wink",
          "Mooney turns to face the camera directly, warm golden light on his face. Played with "
          "total sincerity."),
 "E-4":  (DECK_SUNSET, (M, R, G), "a deck board creak, a pencil scratch, evening gulls",
          "the earnest strings continuing warmly and entirely undisturbed",
          LOCKED_TWO.replace("BOTH ANIMALS", "ALL THREE ANIMALS") + " GARY walks into frame, "
          "sits down on the deck between the two cats, and opens his crossword. Nobody reacts."),
 "E-5":  (DECK_SUNSET, (M,), "evening gulls, one final warm resolving chord", None,
          "He does not look at the raccoon beside him."),

 "TZ-1": (LOUNGE, (G,), "a pencil scratch, a clock, one comic sting",
          "one short bright comic sting on the second raccoon",
          "GARY sits in the armchair with his crossword. Sitting beside him, in an IDENTICAL "
          "pair of small round reading glasses, is a SECOND RACCOON. Two raccoons in frame, "
          "no cats visible. An unseen cat answers from off-screen."),
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

            body = [STYLE, loc, sheets, strip_html(sh["action"])]
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
                          ("no other animals.", "head count")]:
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
