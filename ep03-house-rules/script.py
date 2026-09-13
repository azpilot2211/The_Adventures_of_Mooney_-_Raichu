# -*- coding: utf-8 -*-
"""EPISODE 2 - "House Rules". The shot list, and the renderer for both scripts.

FOLDER NUMBERING: this is ep03-* because it is the third thing produced, and it
is EPISODE 2 on screen. ep02-chonk/ is Episode 1. The folder numbers are
production order; the episode numbers are broadcast order, and they stopped
matching when Fowl Play was shelved. Do not "fix" one to match the other.

The shot list lives here rather than in the HTML so the timecodes, the runtime
and the credit total are computed instead of typed. Ep1's HTML has them typed
by hand, which is fine until a shot length changes.

    python script.py        -> house-rules.html, house-rules.txt, shots.json

`shots.json` is what the prompt pass should read when this gets made: keys,
durations, speakers and the no-dialogue flag are all the prompt writer needs to
apply the right rules per shot.
"""
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

TITLE = "House Rules"
EPISODE = 2
SUBTITLE = "One box. One key. One raccoon who has done nothing wrong."
LOGLINE = ("Gary moves in properly, as promised. He brings a chore wheel, a laminated "
           "sense of fairness and a key nobody gave him. Mooney and Raichu declare war "
           "on a houseguest who wins every round without once raising his voice — and "
           "who is, at every point, completely within his rights.")

RATE = 4.5          # credits per second, measured 2026-09-11
DIVIDER = 0.8       # scene divider, built locally, free

# ---------------------------------------------------------------- shot list
# shot(code, dur, action, lines=[(who, said)], beat=<sfx line for silent shots>,
#      cutaway=bool, free=bool)
ACTS = []


def act(num, name, note, shots, divider_after=True):
    ACTS.append(dict(num=num, name=name, note=note, shots=shots,
                     divider_after=divider_after))


def s(code, dur, action, lines=None, beat=None, cutaway=False, free=False):
    return dict(code=code, dur=dur, action=action, lines=lines or [],
                beat=beat, cutaway=cutaway, free=free)


act("Cold open", "The Key",
    "Gary lets himself in. Nobody stops him, because nobody can think of the grounds. "
    "Five shots, no explanation offered, and the last line is the whole episode.", [

 s("CO-1", 5,
   "Exterior, the front door of the cottage, morning. Close on the cat flap at the bottom of "
   "the door. A raccoon paw comes through the flap from outside, feels its way up the inside of "
   "the door, and turns the deadbolt. CLUNK. The door swings open with a long CREEEAK. GARY walks in "
   "upright, carrying one cardboard box.",
   beat="no dialogue · tumbler click, hinge creak, one jaunty bassoon"),

 s("CO-2", 4,
   "Interior living room. Mooney is flat on the rug. He does not get up. He does not move at all.",
   [("Mooney", "He has a key.")]),

 s("CO-3", 4,
   "Raichu at the window, ear tufts straight up, thrilled by the wrong detail.",
   [("Raichu", "He has a <em>box.</em>")]),

 s("CO-4", 5,
   "Gary sets the box down on the rug, opens it, and lifts out one small framed photograph. He "
   "stands it on the side table and turns it a few degrees until it is straight, CLINK. The "
   "photograph is of the armchair.",
   beat="no dialogue · cardboard, a small glass clink, one sentimental harp"),

 s("CO-5", 5,
   "Mooney has still not moved.",
   [("Mooney", "That's a photograph of the chair he's sitting in.")]),
])

act("Titles", "Main Title reused",
    "The existing main title plate. Episode line composited in post: Episode 2 — \"House Rules\".", [
 s("TS-1", 10.6, "The existing main title, unchanged.", beat="reused plate · 0 credits", free=True),
], divider_after=False)

act("Act One", "The Wheel",
    "Gary institutionalises himself in about a minute. He is never rude, never loud and never "
    "wrong, which is what makes it unbearable. The act ends on the shortest declaration of war "
    "the series has managed.", [

 s("A-1", 5,
   "Gary in the armchair, reading glasses on, holding up a large cardboard disc with wedges "
   "scratched into it. He presents it the way a man presents a boat he has built.",
   [("Gary", "I've made a wheel.")]),

 s("A-2", 4, "Mooney, on the floor, at the far end of his patience already.",
   [("Mooney", "You've made a <em>what.</em>")]),

 s("A-3", 5,
   "Gary spins the wheel with one claw. TICK-TICK-TICK-TICK, it ratchets around like a game-show "
   "wheel, slowing. Tick. Tick. Tick.",
   beat="no dialogue · wheel ratchet, a tiny fanfare that gives up halfway through"),

 s("A-4", 4, "Gary reads the wedge it stopped on.", [("Gary", "Dishes.")]),

 s("A-5", 4, "Mooney does not blink.", [("Mooney", "We don't have hands.")]),

 s("A-6", 5, "Gary, kindly, not looking up.",
   [("Gary", "That's not on the wheel.")]),

 s("A-7", 5, "Raichu shoulders into frame, desperate to be included in his own oppression.",
   [("Raichu", "Do me. Do me.")]),

 s("A-8", 5, "Gary spins it again. It ticks. It stops.", [("Gary", "Also dishes.")]),

 s("A-9", 7,
   "<b>Cutaway.</b> The kitchen sink. Both cats up on their hind legs, one washing, one drying, "
   "in complete silence, wearing tiny aprons. Neither of them looks at the other. Hold on it far "
   "too long.",
   beat="no dialogue · running water, one squeaky plate, a clock", cutaway=True),

 s("A-10", 5, "Back to Mooney, who turns and addresses the camera directly, flat.",
   [("Mooney", "That went on for nine days.")]),

 s("A-11", 5, "Raichu, genuinely wounded.",
   [("Raichu", "I dropped a mug and he put me in the hall.")]),

 s("A-12", 4, "Mooney, without sympathy.", [("Mooney", "You <em>live</em> in the hall.")]),

 s("A-13", 6,
   "Mooney rolls upright. It is the first time he has stood up in two episodes and the camera "
   "should treat it as an event.",
   [("Mooney", "Get the string.")]),
])

act("Act Two", "The Traps",
    "The Tom and Jerry act. Nine of these fourteen shots have no dialogue at all — the comedy "
    "is entirely physical, every trap backfires onto the cat who set it, and Gary never once "
    "notices he is being attacked.", [

 s("B-1", 5,
   "Raichu has drawn a plan on the back of a cereal packet in claw scratches. It means nothing. "
   "He taps it with total authority.",
   [("Raichu", "Trap one.")]),

 s("B-2", 6,
   "<b>Trap one.</b> A metal bucket balanced on the top edge of the door frame above the "
   "armchair. A string runs from the bucket, across the ceiling, down the far wall, to Raichu, "
   "who is tiptoeing backwards holding the end of it and barely breathing. The string goes CREAK.",
   beat="no dialogue · string creak, tiptoe pizzicato, one long held note"),

 s("B-3", 7,
   "Gary walks in underneath the bucket. Nothing happens. He sits down in the armchair. He looks "
   "up at the bucket for a moment. Then he reaches up, unhooks it, CLUNK, sets it down neatly beside "
   "the chair, and sharpens his pencil into it, SCRITCH SCRITCH.",
   beat="no dialogue · a small clunk, pencil sharpening, a defeated trombone"),

 s("B-4", 4, "Mooney, from the doorway, deadpan.", [("Mooney", "He has a bin now.")]),

 s("B-5", 5,
   "<b>Trap two.</b> Raichu tips an entire jar of marbles across the hallway floor, a long skittering "
   "RATTLE, and flattens himself against the wall, delighted with his own genius.",
   beat="no dialogue · a long skittering pour, tense pizzicato"),

 s("B-6", 7,
   "Locked-off wide, straight down the hall. Gary strolls across the marbles without looking "
   "down, paws behind his back, entirely level, and exits. A beat of nothing. Then MOONEY steps "
   "into the hall, WHOOP, goes straight up into the air with all four legs out, and SKKKRRT, "
   "slides the whole length of the floor and out of frame. CRASH.",
   beat="no dialogue · marbles, a comic slide, a distant collapse of saucepans"),

 s("B-7", 5,
   "Mooney upside down against the far wall, legs folded over his head, perfectly calm about it.",
   [("Mooney", "Trap two.")]),

 s("B-8", 6,
   "<b>Trap three.</b> Raichu on the floor beside the armchair with a handsaw, cutting a neat "
   "circle in the floorboards around it, SHHK SHHK SHHK. He is sawing from inside the circle. The audience is "
   "ahead of him and should be allowed to enjoy that for a moment.",
   beat="no dialogue · rhythmic sawing, a slowly rising oboe of dramatic irony"),

 s("B-9", 5,
   "The circle gives way, CRACK. Raichu drops through it with a long descending WHEEEE and lands "
   "somewhere far below, THUD. The armchair and Gary do not move a millimetre. Gary turns a page.",
   beat="no dialogue · a crack, a long descending whistle, a distant thud"),

 s("B-10", 5, "Gary, still reading, mildly.", [("Gary", "Second one this week.")]),

 s("B-11", 8,
   "<b>Music scene.</b> A full orchestral chase cue and not one word. Fast cuts, a musical hit on "
   "every impact: a mousetrap the size of a door snaps shut on nothing, SNAP; a rope snare hoists "
   "MOONEY up by one back leg, SPROING; a desk fan and a burst bag of flour turn both cats "
   "completely white, FWOOMPH; RAICHU fires a grape from a slingshot, TWANG, and it comes "
   "straight back and hits him, BONK.",
   beat="no dialogue · full chase orchestra, whip crack, sproing, a cymbal on every impact"),

 s("B-12", 6,
   "The aftermath. Both cats hanging upside down in the doorway, flour-white, wound in the same "
   "length of rope, revolving slowly. Gary steps over them, reaches up, and turns off the light, CLICK.",
   beat="no dialogue · one light switch, a single sad clarinet"),

 s("B-13", 5, "Darkness. Two pairs of eyes.",
   [("Mooney", "This is worse than the boat.")]),

 s("B-14", 6,
   "<b>Cutaway.</b> A small rowing boat in the middle of the harbour at dawn. Both cats aboard. "
   "Raichu is rowing with one oar, so the boat is turning slowly in a circle. Mooney sits in the "
   "bow facing forward. Neither of them reacts. Never mentioned again.",
   beat="no dialogue · gulls, one oar, water, a resigned accordion", cutaway=True),
])

act("Act Three", "Procurement",
    "Gerald returns with a second business. The transaction is played exactly as flat as the "
    "sandwich deal in Episode 1, and it costs Mooney the one thing he was fighting for.", [

 s("C-1", 6,
   "Night. The kitchen window. GERALD is on the moonlit fence outside. He has been there for some "
   "time and is in no hurry to say so.",
   beat="no dialogue · night crickets, one slow wingbeat, a low bass note"),

 s("C-2", 4, "Mooney at the glass.", [("Mooney", "I need something bigger.")]),

 s("C-3", 5, "Gerald does not blink.", [("Gerald", "How big.")]),

 s("C-4", 4, "Mooney.", [("Mooney", "Raccoon.")]),

 s("C-5", 7,
   "Gerald turns his head very slowly toward a tarpaulin further along the fence. He takes the "
   "corner of it in his bill and pulls, a long canvas SHHHHP. Underneath, gleaming in the "
   "moonlight, is a full-size wooden catapult.",
   beat="no dialogue · canvas sliding, one enormous orchestral reveal, crickets resuming"),

 s("C-6", 4, "Mooney, who has learned nothing.", [("Mooney", "What do you want.")]),

 s("C-7", 4, "Gerald.", [("Gerald", "The chair.")]),

 s("C-8", 5, "Mooney, without a flicker.", [("Mooney", "It's not my chair.")]),

 s("C-9", 5, "Gerald.", [("Gerald", "Then it isn't my catapult.")]),

 s("C-10", 4, "Mooney sells the thing the entire war is about.",
   [("Mooney", "Take the chair.")]),

 s("C-11", 7,
   "Exterior, the garden at dawn. Locked-off wide. Both cats hauling on the catapult's winch, "
   "straining, back paws slipping in the wet grass. The arm ratchets back, CLICK, CLICK, CLICK. Raichu wedges "
   "a stone under it, CLUNK.",
   beat="no dialogue · ratchet clicks, rope creak, two cats straining"),

 s("C-12", 5, "Raichu, radiant, one paw on the release.", [("Raichu", "Ready.")]),

 s("C-13", 8,
   "Locked-off wide of the whole garden. The rope is cut, TWANG. The arm swings the wrong way, WHUMP, and both cats are launched "
   "straight out of the top of frame, their howls dopplering away to nothing. The catapult, "
   "undamaged, rocks gently to a stop. Behind it, in the lit kitchen window, Gary does not look "
   "up. Two distant SPLASHES.",
   beat="no dialogue · whip crack, a doppler wail going away, two distant splashes"),
])

act("Act Four", "The Lease",
    "The South Park turn: the institution sides with the newcomer, and it is not even close. "
    "Everything the cats did was against a tenant in good standing.", [

 s("D-1", 6,
   "Interior living room. MICHAEL and LYNDIE stand over the armchair, delighted, photographing "
   "Gary in it. Gary looks at the camera. He does not smile, but somehow it reads as a smile.",
   beat="no dialogue · camera shutter, warm domestic music"),

 s("D-2", 6,
   "The doorway behind them. Both cats, soaked through, draped in seaweed, dripping onto the floorboards, "
   "drip, drip, SQUELCH. Nobody turns around.",
   beat="no dialogue · dripping, one long squelch, a single fly"),

 s("D-3", 4, "Lyndie, off-screen, warmly.", [("Lyndie", "He's so well behaved.")]),

 s("D-4", 5, "Mooney to camera, harbour water still running off his chin.",
   [("Mooney", "He pays rent.")]),

 s("D-5", 6,
   "<b>Cutaway.</b> The kitchen counter, close. Gary slides a single coin across it with one claw, a long CHINK. "
   "A human hand picks the coin up and pockets it. DING. Neither face is in frame.",
   beat="no dialogue · one coin on wood, a cash-register ding that is far too pleased with itself",
   cutaway=True),

 s("D-6", 6,
   "Raichu, devastated, ear tufts flat for the first time in the series.",
   [("Raichu", "But we <em>live</em> here.")]),

 s("D-7", 6, "Gary, kindly, still not looking up from the crossword.",
   [("Gary", "You live here too.")]),

 s("D-8", 5, "Mooney.", [("Mooney", "That's the worst part.")]),

 s("D-9", 5,
   "The chore wheel, spinning. TICK-TICK-TICK. It slows. It stops on exactly the same wedge, tick.",
   beat="no dialogue · wheel ratchet, one small doomed chime"),

 s("D-10", 5,
   "The sink. Both cats. Aprons. Washing and drying in silence — the identical shot from Act One, "
   "held identically too long.",
   beat="no dialogue · running water, one squeaky plate, a clock", cutaway=True),
])

act("Resolution", "The Wrong Moral",
    "Played completely straight — sunset, warm strings, the full apparatus of a sincere ending — "
    "and attached to a conclusion that is worse than the one in Episode 1.", [

 s("E-1", 6,
   "The deck at sunset. The two cats side by side at the rail, still damp, one strand of seaweed "
   "on Raichu's ear. Warm golden light. Neither looks at the other.",
   [("Raichu", "Maybe he's not so bad.")]),

 s("E-2", 5, "A long, warm, sincere pause. Strings underneath.",
   [("Mooney", "He is.")]),

 s("E-3", 8,
   "Mooney turns to face the camera. Total sincerity, fully earnest music, no wink anywhere.",
   [("Mooney", "You know, I learned something today. I learned that when somebody moves into your "
               "house and makes it cleaner, kinder and better run than you ever did — the only "
               "decent thing left to do is get a bigger catapult.")]),

 s("E-4", 5,
   "A beat. GARY walks into frame, sits down on the deck between them, and opens his crossword. "
   "Nobody says anything. The strings continue warmly, entirely undisturbed.",
   beat="no dialogue · deck creak, pencil scratch, warm strings continuing"),

 s("E-5", 6, "Mooney does not look at him.", [("Mooney", "It's already ordered.")]),
])

act("End card", "& Teaser",
    "The existing sunset end plate, unchanged. Teaser text composited in post.", [
 s("EC-1", 8.1, "The existing end plate. Logo and copyright composited in post.",
   beat="reused plate · 0 credits", free=True),
 s("TZ-1", 5,
   "The armchair. Gary, glasses on, crossword in paw. Sitting beside him, in an identical pair of "
   "small round reading glasses, is a SECOND raccoon.",
   [("Gary", "This is Denise."), ("Mooney (off)", "No.")]),
], divider_after=False)


# ---------------------------------------------------------------- rendering
def flatten():
    rows, t = [], 0.0
    for a in ACTS:
        for sh in a["shots"]:
            rows.append((t, a, sh))
            t += sh["dur"]
        if a["divider_after"]:
            t += DIVIDER
    return rows, t


def tc(x):
    return "%d:%02d" % (int(x) // 60, int(x) % 60)


def act_seconds(a):
    return sum(sh["dur"] for sh in a["shots"])


def act_credits(a):
    return sum(sh["dur"] for sh in a["shots"] if not sh["free"]) * RATE


def main():
    rows, total = flatten()
    shots = [sh for _, _, sh in rows]
    new_secs = sum(sh["dur"] for sh in shots if not sh["free"])
    credits = new_secs * RATE
    dividers = sum(1 for a in ACTS if a["divider_after"])
    silent = sum(1 for sh in shots if not sh["lines"])
    cutaways = sum(1 for sh in shots if sh["cutaway"])
    speakers = {}
    for sh in shots:
        for who, _ in sh["lines"]:
            speakers[who] = speakers.get(who, 0) + 1

    # ---- json for the prompt pass
    json.dump([dict(key=sh["code"], dur=sh["dur"], cutaway=sh["cutaway"], free=sh["free"],
                    silent=not sh["lines"],
                    speakers=[w for w, _ in sh["lines"]],
                    lines=[[w, l] for w, l in sh["lines"]])
               for sh in shots],
              open("shots.json", "w", encoding="utf-8"), indent=1)

    # ---- plain text
    out = ["%s" % TITLE,
           "The Adventures of Mooney & Raichu · Episode %d · Shooting Script" % EPISODE,
           SUBTITLE, "", LOGLINE, "",
           "Runtime %s   Shots %d   Avg shot %.1fs   Silent shots %d   Cutaways %d   Dividers %d"
           % (tc(total), len(shots), new_secs / max(1, len(shots) - 2), silent, cutaways, dividers),
           "New footage %.0f credits at %.1f/second" % (credits, RATE), ""]
    for a in ACTS:
        out += ["", "=" * 72,
                "%s — %s   (%ds · %.0f cr)" % (a["num"].upper(), a["name"],
                                               act_seconds(a), act_credits(a)),
                a["note"], ""]
        for t0, aa, sh in rows:
            if aa is not a:
                continue
            head = "  %s  %-5s %ss" % (tc(t0), sh["code"], sh["dur"])
            out.append(head)
            out.append("    " + sh["action"].replace("<b>", "").replace("</b>", "")
                                            .replace("<em>", "").replace("</em>", ""))
            for who, said in sh["lines"]:
                out.append("    %-14s %s" % (who.upper(),
                                             said.replace("<em>", "").replace("</em>", "")))
            if sh["beat"]:
                out.append("    (%s)" % sh["beat"])
            out.append("")
        if a["divider_after"]:
            out.append("  --- SCENE DIVIDER (0.8s, built locally, free) ---\n")
    open("house-rules.txt", "w", encoding="utf-8").write("\n".join(out))

    # ---- html
    h = [HEAD % dict(title=TITLE, ep=EPISODE, subtitle=SUBTITLE, logline=LOGLINE)]
    h.append('<dl class="stats">')
    for k, v in [("Runtime", tc(total)), ("Shots", len(shots)),
                 ("Silent shots", silent), ("Cutaways", cutaways),
                 ("Dividers", dividers), ("New footage", "%.0f cr" % credits)]:
        h.append('<div class="stat"><dt>%s</dt><dd>%s</dd></div>' % (k, v))
    h.append('</dl></header>')

    for a in ACTS:
        h.append('<section class="act">')
        h.append('<div class="act-head"><span class="act-num">%s</span>'
                 '<h2 class="act-name">%s</h2>'
                 '<span class="act-meta">%ds · %.0f cr</span></div>'
                 % (a["num"], a["name"], act_seconds(a), act_credits(a)))
        h.append('<p class="act-note">%s</p>' % a["note"])
        for t0, aa, sh in rows:
            if aa is not a:
                continue
            h.append('<div class="shot"><div class="rail"><span class="tc">%s</span>'
                     '<span class="code">%s</span><span class="dur">%ss</span></div><div>'
                     % (tc(t0), sh["code"], sh["dur"]))
            tag = '<span class="tag cutaway">cutaway</span>' if sh["cutaway"] else ''
            h.append('<p class="action">%s%s</p>' % (sh["action"], tag))
            for who, said in sh["lines"]:
                h.append('<div class="line"><span class="who">%s</span>'
                         '<p class="said">%s</p></div>' % (who, said))
            if sh["beat"]:
                h.append('<p class="beat">%s</p>' % sh["beat"])
            h.append('</div></div>')
        if a["divider_after"]:
            h.append('<p class="divider-rule">scene divider · 0.8s · built locally, free</p>')
        h.append('</section>')

    h.append(NOTES)
    h.append('<table class="ledger"><thead><tr><th>Segment</th><th>Shots</th>'
             '<th>Runtime</th><th>Credits</th></tr></thead><tbody>')
    for a in ACTS:
        h.append('<tr><td>%s — %s</td><td>%d</td><td>%s</td><td>%.0f</td></tr>'
                 % (a["num"], a["name"], len(a["shots"]), tc(act_seconds(a)), act_credits(a)))
    h.append('<tr class="tot"><td>Episode %d total</td><td>%d</td><td>%s</td><td>%.0f</td></tr>'
             % (EPISODE, len(shots), tc(total), credits))
    h.append('</tbody></table>')
    h.append('</div></body>')
    open("house-rules.html", "w", encoding="utf-8").write("\n".join(h))

    print('"%s" — Episode %d' % (TITLE, EPISODE))
    print("%d shots | %s | avg %.1fs | %d silent | %d cutaways | %d dividers"
          % (len(shots), tc(total), new_secs / max(1, len(shots) - 2), silent, cutaways, dividers))
    print("new footage %.0fs = %.0f credits at %.1f/s" % (new_secs, credits, RATE))
    print("lines per character: " + ", ".join("%s %d" % (k, v)
          for k, v in sorted(speakers.items(), key=lambda x: -x[1])))
    multi = [sh["code"] for sh in shots if len({w for w, _ in sh["lines"]}) > 1]
    print("shots with more than one speaker (cannot be revoiced): %s" % (multi or "none"))
    check(shots, silent, cutaways, speakers)


def check(shots, silent, cutaways, speakers):
    """The production notes quote counts at the reader. Numbers in prose drift the
    moment a shot changes, and a note that lies is worse than no note, so the
    claims are asserted against the shot list every time this renders."""
    b = [sh for sh in shots if sh["code"].startswith("B-")]
    claims = [
        (len(shots), 63, "total shots"),
        (silent, 25, "silent shots"),
        (cutaways, 4, "cutaways"),
        (sum(1 for sh in b if not sh["lines"]), 9, "silent shots in Act Two"),
        (len(b), 14, "shots in Act Two"),
        (speakers.get("Gary", 0), 7, "Gary's lines"),
        (speakers.get("Gerald", 0), 3, "Gerald's lines"),
    ]
    bad = ["%s: notes say %d, shot list has %d" % (what, claimed, actual)
           for actual, claimed, what in claims if actual != claimed]
    if bad:
        raise SystemExit("PRODUCTION NOTES OUT OF DATE:\n  " + "\n  ".join(bad))
    print("production-note counts agree with the shot list")


HEAD = """<title>%(title)s</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
  :root{
    --fog:#EDF0F3; --surface:#E2E7EB; --card:#F6F8F9;
    --ink:#16202B; --ink-2:#3A4854; --shingle:#6F7C88; --rule:#CBD4DB;
    --hydrangea:#4F63B8; --hydrangea-soft:#DDE2F4;
    --buoy:#B14E33; --seaglass:#37796B;
  }
  @media (prefers-color-scheme:dark){
    :root:not([data-theme="light"]){
      --fog:#121A22; --surface:#1B252F; --card:#1E2A35;
      --ink:#E6EDF2; --ink-2:#B4C2CE; --shingle:#8797A4; --rule:#2E3D4A;
      --hydrangea:#93A4EA; --hydrangea-soft:#26314C;
      --buoy:#E08D6E; --seaglass:#6FB6A4;
    }
  }
  :root[data-theme="dark"]{
      --fog:#121A22; --surface:#1B252F; --card:#1E2A35;
      --ink:#E6EDF2; --ink-2:#B4C2CE; --shingle:#8797A4; --rule:#2E3D4A;
      --hydrangea:#93A4EA; --hydrangea-soft:#26314C;
      --buoy:#E08D6E; --seaglass:#6FB6A4;
  }
  *{box-sizing:border-box}
  body{background:var(--fog);color:var(--ink);font-family:"Newsreader",Georgia,serif;
       font-size:17px;line-height:1.6;margin:0;padding:0 20px 96px}
  .wrap{max-width:980px;margin:0 auto}
  .mast{padding:56px 0 30px;border-bottom:2px solid var(--ink)}
  .eyebrow{font-family:"IBM Plex Mono",monospace;font-size:11.5px;letter-spacing:.16em;
           text-transform:uppercase;color:var(--shingle);margin:0 0 18px}
  h1{font-family:"Bricolage Grotesque",Arial,sans-serif;font-weight:800;
     font-size:clamp(50px,10vw,96px);line-height:.92;letter-spacing:-.03em;margin:0}
  .subtitle{font-family:"Bricolage Grotesque",Arial,sans-serif;font-weight:600;
            font-size:clamp(19px,2.6vw,25px);color:var(--ink-2);margin:14px 0 0;letter-spacing:-.01em}
  .logline{max-width:62ch;color:var(--ink-2);margin:20px 0 0;font-size:18px}
  .stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(128px,1fr));gap:1px;
         background:var(--rule);border:1px solid var(--rule);margin:34px 0 0}
  .stat{background:var(--fog);padding:15px 16px}
  .stat dt{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.13em;
           text-transform:uppercase;color:var(--shingle);margin:0 0 6px}
  .stat dd{font-family:"Bricolage Grotesque",Arial,sans-serif;font-weight:800;
           font-size:23px;margin:0;letter-spacing:-.02em}
  .act{margin:64px 0 0}
  .act-head{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;
            border-bottom:1px solid var(--ink);padding-bottom:10px}
  .act-num{font-family:"IBM Plex Mono",monospace;font-size:11px;letter-spacing:.16em;
           text-transform:uppercase;color:var(--buoy);font-weight:600}
  .act-name{font-family:"Bricolage Grotesque",Arial,sans-serif;font-weight:800;
            font-size:34px;letter-spacing:-.025em;margin:0;flex:1}
  .act-meta{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--shingle)}
  .act-note{color:var(--ink-2);font-size:16.5px;max-width:70ch;margin:14px 0 26px;font-style:italic}
  .shot{display:grid;grid-template-columns:104px 1fr;gap:22px;padding:17px 0;
        border-bottom:1px solid var(--rule)}
  .rail{display:flex;flex-direction:column;gap:3px;font-family:"IBM Plex Mono",monospace;
        padding-top:2px}
  .tc{font-size:12px;color:var(--shingle)}
  .code{font-size:14px;font-weight:600;color:var(--hydrangea)}
  .dur{font-size:11.5px;color:var(--shingle)}
  .action{margin:0;font-size:16.5px}
  .beat{font-family:"IBM Plex Mono",monospace;font-size:12.5px;color:var(--seaglass);
        margin:9px 0 0;letter-spacing:.01em}
  .line{display:grid;grid-template-columns:132px 1fr;gap:14px;margin:12px 0 0;align-items:baseline}
  .who{font-family:"IBM Plex Mono",monospace;font-size:11.5px;letter-spacing:.13em;
       text-transform:uppercase;color:var(--buoy);font-weight:600}
  .said{margin:0;font-size:19px;font-weight:500;line-height:1.42}
  .tag{font-family:"IBM Plex Mono",monospace;font-size:10px;letter-spacing:.11em;
       text-transform:uppercase;padding:2px 7px;margin-left:9px;border-radius:2px;
       background:var(--hydrangea-soft);color:var(--hydrangea);white-space:nowrap}
  .divider-rule{font-family:"IBM Plex Mono",monospace;font-size:11.5px;letter-spacing:.13em;
       text-transform:uppercase;color:var(--seaglass);text-align:center;margin:20px 0 0;
       padding:9px;border:1px dashed var(--rule)}
  .notes{margin:74px 0 0;border-top:2px solid var(--ink);padding-top:34px}
  .note-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(292px,1fr));gap:26px;margin-top:26px}
  .note h3{font-family:"Bricolage Grotesque",Arial,sans-serif;font-weight:800;font-size:18px;
           letter-spacing:-.015em;margin:0 0 7px}
  .note p{margin:0;color:var(--ink-2);font-size:16px}
  .ledger{width:100%%;border-collapse:collapse;margin:44px 0 0;font-size:15px}
  .ledger th{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.13em;
             text-transform:uppercase;color:var(--shingle);text-align:left;
             border-bottom:1px solid var(--ink);padding:8px 10px}
  .ledger td{padding:8px 10px;border-bottom:1px solid var(--rule)}
  .ledger td:nth-child(n+2){font-family:"IBM Plex Mono",monospace;font-size:13.5px}
  .ledger .tot td{font-weight:700;border-bottom:2px solid var(--ink)}
</style>
<body><div class="wrap">
<header class="mast">
  <p class="eyebrow">The Adventures of Mooney &amp; Raichu · Episode %(ep)d · Shooting script</p>
  <h1>%(title)s</h1>
  <p class="subtitle">%(subtitle)s</p>
  <p class="logline">%(logline)s</p>
"""

NOTES = """
<section class="notes">
<h2 class="act-name">Production notes</h2>
<div class="note-grid">

<div class="note"><h3>The episode has a score, designed once</h3>
<p>Episode 1 had none: each shot named an instrument and the finished cut had no through-line.
<code>prompts/blocks.py</code> now holds one cue state per act, named by what the music is
<em>doing</em>, and <code>audio()</code> stamps the right one onto every prompt automatically —
cold open <em>light playful pizzicato, unsuspecting</em>; Act One <em>a small self-important
bureaucratic march</em>; Act Two <em>scheming tiptoe pizzicato building into a full
Tom-and-Jerry chase orchestra</em>; Act Three <em>low noir bass, a deal being done in the
dark</em>; Act Four <em>warm domestic music entirely on Gary's side, which is the joke</em>;
resolution <em>fully earnest strings</em>. Transitions — "…music begins", "the music stops
dead" — go in the shot where they happen.</p></div>

<div class="note"><h3>Direct the mix, not just the ingredients</h3>
<p>From the owner's example prompt of 2026-09-13. Episode 1 ended every prompt with a list
— <em>"wind, one distant gull, crickets."</em> — and left the balance to chance. Every prompt
now ends with the mix itself: <em>clear centered dialogue, subtle room ambience, cartoon Foley,
precisely timed comedic SFX, original orchestral score that ducks under speech and stops dead
on the punchline, no copyrighted music.</em> "Clear centered dialogue" and "ducks under speech"
go straight at the complaint that drove the whole Episode 1 rework.</p></div>

<div class="note"><h3>Ask for the silence, not just the absence of words</h3>
<p>The same prompt says <em>"brief comedic silence after Mooney's line"</em>. Episode 1's cap
only forbade extra speech, which left a vacuum the model filled anyway. <code>only()</code> now
asks for the silence by name and tells the score to stop on the line. Better comedy and a
tighter cap in one.</p></div>

<div class="note"><h3>Time-code the beats in an action take</h3>
<p>The example carries four gags in one fifteen-second generation by writing
<em>0–4 sec:</em>, <em>4–8 sec:</em> and pinning the audio to each. <code>beats()</code> does
that; B-11's montage is written this way in <code>prompts/worked_examples.py</code>. It buys
reliability and rhythm rather than credits — cost is per second either way — but a trap and its
payoff can no longer come back as two takes that fail to match.</p></div>

<div class="note"><h3>"Harmless slapstick only"</h3>
<p>Also lifted from that prompt, and Act Two is nothing but pratfalls. The filter refused two of
fourteen trailer shots over wording that was in no way unsafe, so every trap shot carries
<em>nobody is hurt, nobody is injured, everyone is fine immediately afterwards</em>. Free
insurance on the most exposed act in the episode.</p></div>

<div class="note"><h3>Write the sound effect into the action, in capitals, on the beat</h3>
<p>Taken from the owner's Lucky Lots prompt (higgsfield.ai/s/kMh3mXz6BqY), which reads
<em>"WHOOSH, a second rocket launches upward … a split second before BOOM, an enormous colorful
cartoon explosion"</em>. The onomatopoeia sits inline at the exact moment it lands, and the terse
<code>Audio:</code> list still goes last. Every action line in this script is written that way
already — CLUNK, SKKKRRT, SPROING, FWOOMPH — so it transfers into the prompt verbatim.
<b>Unverified:</b> that sample was generated on Seedance 2.5, so its sound design may owe as much
to the model as to the wording. Shoot one trap shot both ways before committing the act.</p></div>

<div class="note"><h3>Also from that prompt: the negative, and the delivery</h3>
<p>It carries <em>"NO on-screen text, no subtitles, no captions, no logos, no watermarks"</em> as
one blunt line — stronger than this project's current wording, and worth adopting wholesale. It
also puts the delivery next to the line rather than in a separate voice block:
<em>says warmly in a strong New York accent: "…"</em>. Same shape this project already uses for
Mooney and Raichu.</p></div>

<div class="note"><h3>Stay on Seedance 2.0 unless a shot needs the length</h3>
<p>Priced 2026-09-12: <b>2.0 is 4.5 credits a second, 2.5 is 6.5</b> (36 versus 52 for eight
seconds). 2.5 goes to 30 seconds where 2.0 stops at 15, and the Lucky Lots prompt shows it holding
a multi-beat sequence with an internal <em>quick cut to close-up</em>. That earns its 44% premium
only where one long take replaces three shots that would each waste the four-second minimum —
B-11's montage is the one candidate here. Everything else is cheaper on 2.0.</p></div>

<div class="note"><h3>Every dialogue shot is single-speaker</h3>
<p>Only TZ-1 has two. <code>voice_change</code> converts every voice on a track, so a shot where
both cats speak can never be put on the locked voices — that is why Episode 1's CO-2 had to be
re-shot. Mooney is Cillian, Raichu is Miles. Keep it that way and each line costs 1 credit to
lock.</p></div>

<div class="note"><h3>Cap every line in the prompt</h3>
<p>Seedance pads a line under about six words with a second, invented utterance. Four of the
owner's Episode 1 notes were this and nothing else. Use the <code>only()</code> wording from
<code>ep02-chonk/prompts/refix.py</code> on every line here — this script has a lot of very short
ones, which is exactly the failure case.</p></div>

<div class="note"><h3>Silent shots are the reliable ones</h3>
<p>Twenty-five of these sixty-three shots have no dialogue at all. That is deliberate: a shot with no
speech cannot be padded, cannot be mumbled and never needs revoicing. It is also what Tom and Jerry
actually is. State it explicitly — <em>there is no dialogue in this shot, nobody speaks</em> — or
the model will add some.</p></div>

<div class="note"><h3>Over-generate the action, then trim</h3>
<p>Measured on the trailer: physical action lands somewhere unpredictable inside the shot, and both
two-cat shots left dead frame at one end. Generate action a second or two long and cut IN and OUT
per shot the way <code>series/trailer/assemble.py</code> does, rather than head-trimming only.</p></div>

<div class="note"><h3>Lock every two-cat frame</h3>
<p>B-6, B-11, B-12, C-11, C-13 and D-2 all have both cats moving at once, the hardest thing this
pipeline does. Static locked-off wide, both cats named with their side of frame, and
<em>both cats remain fully inside the frame for the entire shot</em> — and expect to trim an exit
anyway.</p></div>

<div class="note"><h3>Budget one refusal in seven</h3>
<p>The content filter rejected two of fourteen trailer shots, twice each, over wording that was in
no way unsafe. Slapstick is more exposed than dialogue, so for every trap shot decide the free
fallback <em>before</em> generating: B-3 can be a still of the bucket, B-9 can hold on Gary, and
the whole of B-11 can be built from the other traps' offcuts. Rejected jobs are not charged.</p></div>

<div class="note"><h3>The music scene is one shot, not a sequence</h3>
<p>B-11 asks for the montage inside a single 8-second generation, because cutting four separate
4-second minimums together would cost 72 credits for four seconds of usable footage. If it comes
back weak, build the montage locally from the trap shots already in the can and score it with a
synthesised cue — <code>divider.py</code> and <code>outro.py</code> already synthesise audio with
numpy, for nothing.</p></div>

<div class="note"><h3>Dividers and cards are free</h3>
<p>Five dividers at the act breaks, from the four designs in <code>ep02-chonk/divider.py</code>,
cycling so no two adjacent match. Main title and end plate are reused. The episode line and the
teaser text composite in post with <code>drawtext</code>. None of it costs anything.</p></div>

<div class="note"><h3>Narration and score go on afterwards</h3>
<p>There is no narrator in this episode, but the same lesson holds for the music: ask Seedance for
the sound design per shot in the <code>Audio:</code> line, then do the wide musical decisions in the
assembler. <code>seed_audio</code> is 0.1 credits a line if anything needs speaking.</p></div>

<div class="note"><h3>Gary needs a voice before a frame is shot</h3>
<p>He carries seven lines here against three in Episode 1, and he is the antagonist. Pick his preset
from <code>series/VOICES.html</code> and write it into the handoff table first. Gerald needs one
too — three lines. Assigning them up front is the whole lesson of Episode 1.</p></div>

<div class="note"><h3>Cutaways still solve continuity</h3>
<p>Four hard jumps to unrelated scenes — A-9, B-14, D-5, D-10 — where the discontinuity is the
joke. Do not chain a reference frame into them. Everywhere else, pass the previous shot's final
frame, and check the last frame of each shot against the first of the next.</p></div>

<div class="note"><h3>Nothing readable in frame</h3>
<p>The chore wheel, Raichu's plan on the cereal packet and Gary's crossword must all be scratches
and marks, never letters. Ask for it explicitly on A-1, A-3, B-1, D-9 and every Gary shot. Real
text composites in post.</p></div>

</div></section>
"""

if __name__ == "__main__":
    main()
