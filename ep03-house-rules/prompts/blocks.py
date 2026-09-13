# -*- coding: utf-8 -*-
"""Shared prompt blocks for Episode 2 "House Rules".

Supersedes ep02-chonk/prompts/blocks.py. Same locations and characters, but the
audio is directed rather than listed, which is the whole change.

WHERE THIS CAME FROM
--------------------
The owner's example prompt (LL-BG-Cards/example-prompt.txt, 2026-09-13) does six
things our Episode 1 prompts never did. Ours ended with an ingredient list —
"wind, one distant gull, crickets." — and left the mix to chance:

1. It DIRECTS THE MIX, in its own sentence, last:
   "Audio professionally mixed for television: clear centered dialogue, subtle
   room ambience, cartoon Foley, precisely timed comedic SFX, original playful
   orchestral/jazz score that ducks under speech, musical stops around
   punchlines, no copyrighted music."
   "Clear centered dialogue" and "ducks under speech" speak straight to the
   thing the owner complained about all through Episode 1.

2. The MUSIC HAS A STATE AND THE STATE CHANGES. "Light playful pizzicato comedy
   music" … "Fast mischievous heist music begins." Ours named instruments; this
   names what the score is DOING and when it turns over.

3. "MUSICAL STOPS AROUND PUNCHLINES" — the single most cartoon-sounding
   instruction in the file, and free.

4. SFX INLINE, IN CAPITALS, ON THE BEAT — THUD, POP, BEEPS, WHIRR, ZAP, CRASH.
   Confirms the Lucky Lots sample; the script already writes them this way.

5. "BRIEF COMEDIC SILENCE AFTER MOONEY'S LINE" — the positive framing of our
   `only()` cap. Say what should be there (silence) as well as what should not
   (more words). Folded into only() below.

6. "HARMLESS SLAPSTICK ONLY" — the content filter refused two of fourteen
   trailer shots over wording that was in no way unsafe, and Act Two is nothing
   but slapstick. This line is a cheap hedge on the most exposed act we have.

NOT TAKEN: the example is for a 2D hand-drawn show and negates 3D. Ours is
established 3D Pixar-style across a finished episode and a trailer. Take the
technique, never the look.
"""

# ------------------------------------------------------------------ look
STYLE = ("3D animated cartoon, Pixar-style feature animation, soft cinematic lighting, "
         "shallow depth of field, expressive facial acting, exaggerated comedic timing. "
         "No photorealism, no live action, no imitation of any existing show's exact style.")

# From the full-episode document's global block. We pass a cast reference image on
# every shot, but never actually asked for on-model consistency in words, and
# Episode 1 drifted: Mooney reads as a normal-sized cat in several trailer shots
# despite an identical character block. Cheap to say, so say it.
ON_MODEL = ("The characters are EXACTLY as the reference image and identical in every shot: "
            "never change their coat patterns, proportions, eye appearance, relative size or "
            "overall design. Mooney is clearly and unmistakably the much fatter of the two cats.")

# Also from that document. Costs nothing and is the difference between a puppet and
# a performance.
ANIMATION = ("Natural blinking, breathing, ear flicks and tail movement throughout, with "
             "anticipation, follow-through and secondary animation on every action.")

NO_TEXT = ("NO on-screen text, no subtitles, no captions, no letters, no numbers, no logos "
           "and no watermarks anywhere in frame.")

# Act Two is wall-to-wall pratfalls. Two innocuous trailer shots were refused
# twice each; this is the cheapest insurance available.
HARMLESS = ("Harmless cartoon slapstick only — nobody is hurt, nobody is injured, "
            "everyone is fine immediately afterwards.")

# ------------------------------------------------------------------ audio
# Appended LAST to every single prompt, verbatim, the way the example does it.
AUDIO_MIX = (
    "Audio professionally mixed for broadcast television: clear centered dialogue, "
    "realistic room tone underneath everything so it never feels artificially silent, "
    "Foley for paws and furniture and objects, exaggerated cartoon effects used "
    "SELECTIVELY for jokes only. Original score that ducks 6 to 10 dB under dialogue and "
    "comes back between lines, and stops dead on the punchline. "
    "DO NOT FILL EVERY SECOND WITH MUSIC OR EFFECTS - silence and reaction pauses are "
    "part of the comedy. No copyrighted music."
)

# Series canon, from the owner's full-episode document: the humans cannot
# understand the cats. Every shot where a person shares the frame with a talking
# animal carries this, or Michael and Lyndie start reacting to dialogue they are
# not supposed to hear. Act Four of House Rules is built on it.
MEOWS = ("The humans CANNOT understand the animals. The cats' and the raccoon's speech is "
         "plain English to the audience, but any human in the shot hears only ordinary "
         "meowing and reacts accordingly - no human ever answers a cat's line or shows any "
         "sign of understanding it.")

# The score has a shape across the episode. Episode 1 had no score design at all -
# each shot named an instrument and the cut had no through-line. One cue state per
# act, named by what the music is DOING, and the transitions are written into the
# shot where they happen ("...music begins", "the music stops dead").
SCORE = {
    "CO": "light playful pizzicato domestic comedy music, unhurried and unsuspecting",
    "A":  "prim plucked strings and a small self-important bureaucratic march",
    "B":  "scheming tiptoe pizzicato that builds, breaking into a full Tom-and-Jerry "
          "chase orchestra with a musical hit on every impact",
    "C":  "low noir bass, single ominous held notes, a deal being done in the dark",
    "D":  "warm sincere domestic music that is entirely on Gary's side, which is the joke",
    "E":  "fully earnest orchestral strings, played completely straight",
}

def audio(shot_code, *sfx, music=None):
    """The Audio: line. SFX first as concrete Foley, then the score state, then the mix.

    Pass music= to override the act's cue when the score changes inside the shot -
    that is where "…begins" and "the music stops dead" belong.
    """
    cue = music if music is not None else SCORE[shot_code.split("-")[0]]
    parts = ", ".join(sfx)
    return "Audio: %s. Score: %s. %s" % (parts, cue, AUDIO_MIX)

# ------------------------------------------------------------------ dialogue
def only(words, who="He"):
    """The cap, now with the example's positive half.

    Episode 1's four "I can't understand him" notes were all one bug: Seedance
    pads a line under about six words with a second, invented utterance. Saying
    only what must NOT happen left a vacuum; the example fills it by asking for
    the silence explicitly, which is also better comedy.
    """
    return ('%s says EXACTLY these words and NOTHING else: "%s" '
            'Accurate lip sync, clean clearly articulated dialogue. '
            'Then a brief comedic silence — %s speaks no other words at any point in this '
            'shot, no second sentence, no muttering, no trailing off, no ad-libbed dialogue, '
            'and does not say anyone\'s name unless it is in that line. '
            'The score drops away under the line and stops on it.'
            % (who, words, who if who != "He" else "he"))

# ------------------------------------------------------------------ cast
MOONEY = ("MOONEY is a very overweight black-and-white tuxedo cat with a white chest, "
          "white paws, a white muzzle and large green eyes. He moves slowly and his "
          "expression is flat and unimpressed.")

RAICHU = ("RAICHU is a brown, black and grey Maine Coon tabby cat with a thick ruff, a long "
          "bushy tail, and LONG DRAMATIC LYNX-TIP EAR TUFTS - tall pointed tufts of fur "
          "standing straight up from the tips of both ears. His eyes are wide and green and "
          "his expression is intense and eager.")

GARY = ("GARY is a raccoon wearing small round reading glasses, sitting upright like a person. "
        "He is unfailingly calm, polite and reasonable, and never once raises his voice.")

GERALD = ("GERALD is an enormous herring gull - a large white seabird with grey wings, black "
          "wingtips, a heavy yellow bill with a red spot near the tip, and pale unblinking "
          "eyes. He is smug, still and completely unhurried.")

# Delivery, next to the line, the way the example does it. Never write "deep" for
# Mooney - that wording is what produced the too-deep voice in Episode 1 - and
# never "high-pitched squeak" for Raichu, which produced the garble.
V_MOONEY = "dryly, in a flat unimpressed drawl"
V_RAICHU = ("brightly and eagerly, at a normal speaking pitch, quick but CLEARLY ARTICULATED, "
            "every word crisp and easy to understand, not squeaky and not mumbled")
V_GARY = "kindly and reasonably, in an unhurried older male voice, never raising it"
V_GERALD = "flatly, in a calm low smug unhurried voice"

# ------------------------------------------------------------------ voices
# Locked 2026-09-13. Every character has one BEFORE a frame is generated, which is
# the whole lesson of Episode 1 — its voices were sorted out afterwards, one
# re-shoot and one revoice pass at a time. voice_change converts EVERY voice on a
# track, so a shot with two speakers can never be put on these: keep one speaker
# per shot and each line costs 1 credit to lock.
VOICE = {
    "MOONEY":  ("Cillian", "d8ba9f14-8a24-44db-932b-99e16c45bd32"),
    "RAICHU":  ("Miles",   "e18664a7-ee4f-5273-acf8-533eb24cd366"),
    "GARY":    ("Arthur",  "30fc8796-ceb6-4a66-b3a7-4a145ef7f346"),
    "GERALD":  ("Knox",    "195e386a-cb61-5c1b-a53b-0e2f0669c408"),
    "LYNDIE":  ("Delia",   "1550321e-7f5b-526e-b001-02328b03e9bc"),
    "MICHAEL": ("Ian",     "472a562a-4c33-5114-8210-d6ffa1e4e2c5"),
}

# ------------------------------------------------------------------ locations
LOUNGE = ("LOCATION: INTERIOR, INSIDE THE HOUSE - the living room of a Cape Cod cottage. "
          "A worn upholstered couch with soft cushions, a battered armchair, a side table "
          "with a lamp, a rug, a window with daylight coming through it. "
          "THIS SHOT IS ENTIRELY INDOORS: do not show deck boards, do not show grey shingle "
          "siding, do not show a garden, do not show sky or harbour.")

KITCHEN = ("LOCATION: INTERIOR, INSIDE THE HOUSE - the kitchen of a Cape Cod cottage. "
           "Painted shaker cabinets, a wooden countertop, tiled floor, a window over the sink, "
           "warm indoor light. THIS SHOT IS ENTIRELY INDOORS: do not show deck boards, do not "
           "show grey shingle siding, do not show a garden, do not show sky or harbour.")

HALL = ("LOCATION: INTERIOR, INSIDE THE HOUSE - a narrow hallway of a Cape Cod cottage, "
        "bare floorboards running away from camera, a door at the far end, coats on hooks. "
        "THIS SHOT IS ENTIRELY INDOORS: do not show a garden, do not show sky or harbour.")

GARDEN = ("LOCATION: EXTERIOR, the back garden of a Cape Cod cottage. A weathered grey wooden "
          "fence, mown green lawn, hydrangea bushes, soft overcast coastal light. "
          "THIS SHOT IS ENTIRELY OUTDOORS: do not show kitchen cabinets, do not show a tiled "
          "floor, do not show any interior room.")

FENCE_NIGHT = ("LOCATION: EXTERIOR at night seen from inside the house through a kitchen "
               "window - a weathered grey fence in a back garden under a full moon, cold blue "
               "moonlight, dark hydrangea bushes. Do not show daylight.")

DECK_SUNSET = ("LOCATION: EXTERIOR, the wooden deck of a Cape Cod cottage at sunset. Weathered "
               "grey deck boards, a simple wooden railing, warm golden-orange low sunlight, the "
               "harbour soft and out of focus behind. THIS SHOT IS ENTIRELY OUTDOORS ON THE "
               "DECK: do not show kitchen cabinets, do not show any interior room.")

KITCHEN_NIGHT = ("LOCATION: INTERIOR, INSIDE THE HOUSE - the kitchen of a Cape Cod cottage at "
                 "night. Painted shaker cabinets, a wooden countertop, tiled floor, a window over "
                 "the sink. The only light is cold blue moonlight through the window and a faint "
                 "glow from the refrigerator. THIS SHOT IS ENTIRELY INDOORS: do not show deck "
                 "boards, do not show a garden, do not show daylight.")

LOUNGE_DARK = ("LOCATION: INTERIOR, INSIDE THE HOUSE - the living room of a Cape Cod cottage with "
               "the light switched off. Almost total darkness, one thin band of moonlight through "
               "the window, the shapes of a couch and an armchair barely visible. "
               "THIS SHOT IS ENTIRELY INDOORS AND VERY DARK: no daylight, no lamplight.")

BOAT = ("LOCATION: EXTERIOR, a small wooden rowing boat on flat calm harbour water at dawn, "
        "moored fishing boats far behind, pale early light, mist on the water. "
        "THIS SHOT IS ENTIRELY OUTDOORS ON THE WATER: do not show any room, do not show a garden.")

FRONT_DOOR = ("LOCATION: EXTERIOR, the front door of a grey-shingled Cape Cod cottage in "
              "morning light, a cat flap set into the bottom of the door, hydrangeas either "
              "side. Do not show any interior room.")

# ------------------------------------------------------------------ staging
LOCKED_TWO = ("A STATIC LOCKED-OFF WIDE SHOT. BOTH ANIMALS REMAIN FULLY INSIDE THE FRAME FOR "
              "THE ENTIRE SHOT - neither leaves frame, neither is cropped at the edge.")

SILENT = ("THERE IS NO DIALOGUE IN THIS SHOT. Nobody speaks, nobody talks, no voice is heard, "
          "no words are spoken at any point.")

ONE_CAT = "EXACTLY ONE CAT. No humans, no bird, no other animals."

# ------------------------------------------------------------------ references
REF_CAST = "9d60de2f-0261-4a47-b0c8-da570ed6e38a"
REF_GARY = "cb6a617f-f917-4dea-b34b-ce1706bfe3bf"
REF_GERALD = "32f71a43-98f7-4f0f-88db-729ac34a90d8"
REF_LIVINGROOM = "3c223738-22f6-4de6-bfd6-6c62333be42c"
REF_MICHAEL = "0606324c-cfc1-4cbd-a45a-8bb2c5384b6b"
REF_LYNDIE = "36f7a2a3-7eae-4fac-bb93-d1924413fcf3"


# The example marks the transition OUT of a shot: "SMASH CUT", "slow dissolve",
# "quick flashback transition". Ours were all unmarked hard cuts. Only worth
# saying where it is a deliberate device - a smash cut into a cutaway, a dissolve
# into the sincere ending.
TRANSITION = {
    "smash":    "END THIS SHOT ON A HARD SMASH CUT - no fade, no dissolve, cut instantly on "
                "the last frame.",
    "dissolve": "END THIS SHOT ON A SLOW GENTLE DISSOLVE.",
    "hold":     "HOLD ON THE REACTION for a beat after the action finishes before the shot "
                "ends - the pause is the joke.",
}


def beats(*pairs):
    """Time-coded beat blocks, the example's structure for a multi-beat take.

        beats((0, 3, "Raichu tips the marbles, RATTLE."),
              (3, 7, "Gary strolls across them without looking down."))

    The example carries four beats in one 15-second generation this way and pins
    the audio to each. It buys reliability, not credits: cost is per second either
    way. What it removes is the risk of a trap and its payoff being generated as
    two takes that do not match, and it lets one shot hold a real comic rhythm.
    Seedance 2.0 tops out at 15s; 2.5 reaches 30s at 6.5 credits a second
    against 2.0's 4.5.
    """
    return " ".join("%d-%d sec: %s." % (a, b, t.rstrip(".")) for a, b, t in pairs)
