# EPISODE BIBLE — The Adventures of Mooney & Raichu

**Read this before building any episode.** `HANDOFF.md` is session state — what is
half-finished, what is waiting, what the balance is. This file is the craft: what we
know about making this show work, and how each thing was learned.

Every rule here cost something. Where a rule has a price, it is written down.

---

## 1. The cast, and the one rule that governs everything

| Character | Voice | voice_id | type |
|---|---|---|---|
| **Mooney** | Cillian | `d8ba9f14-8a24-44db-932b-99e16c45bd32` | preset |
| **Raichu** | Miles | `e18664a7-ee4f-5273-acf8-533eb24cd366` | preset |
| **Gary** | Arthur | `30fc8796-ceb6-4a66-b3a7-4a145ef7f346` | preset |
| **Gerald** | Knox | `195e386a-cb61-5c1b-a53b-0e2f0669c408` | preset |
| **Lyndie** | Delia | `1550321e-7f5b-526e-b001-02328b03e9bc` | preset |
| **Michael** | Ian | `472a562a-4c33-5114-8210-d6ffa1e4e2c5` | preset |

Also in the workspace, unused: an `element` clone of Mooney's "I have never been hungry"
take, `e1f028f2-9e60-4659-9a86-07e6f285112f`. Cost 40 credits. A preset is better value.

> ### THE RULE: one speaker per shot.
>
> Seedance invents a new voice for every generation. You do not fix that at generation
> time — you fix it afterwards with `voice_change`, which replaces the spoken voice in a
> finished clip while keeping the timing, the lip-sync and the picture, for **1 credit**.
>
> **`voice_change` converts every voice on the track.** A shot where two characters speak
> can never be put on the locked voices. Episode 1 has four such shots — CO-5, A-12, TZ-1
> and CO-1 — and they are permanently stuck with whatever the generator produced. CO-2 had
> to be re-shot at 27 credits purely to remove one off-screen human line so a 1-credit
> revoice could reach it.
>
> **Write every exchange as alternating single-speaker shots.** It costs nothing extra —
> shots are priced by the second, not by the cut — and it keeps every line recoverable.

**Assign every character a voice before a single frame is generated.** Episode 1's voices
were sorted out afterwards, one re-shoot and one revoice pass at a time, and it was the
single most expensive mistake the show has made.

---

## 2. Series canon

- Cats speak English to each other and to the raccoon and the gull. **Humans hear only
  meowing.** No human ever answers a line or shows any sign of understanding one. Say so
  in the prompt whenever a person shares a frame with a talking animal, or Michael and
  Lyndie start reacting to dialogue they cannot hear.
- **Mooney** — black-and-white tuxedo, very overweight. Pronounced MOO-nee; write
  **"Moonie"** in any prompt where the name is spoken aloud. Dry, slow, food-motivated.
  His comedy is doing as little as possible.
- **Raichu** — brown/black/grey Maine Coon. Pronounced RYE-choo; write **"Rye-choo"**
  when spoken. **Long dramatic lynx-tip ear tufts, spelled out in full in every prompt,
  never "as established".** Hyperactive, mischievous, certain he is the cleverest thing
  alive.
- **Gerald** — herring gull, recurring antagonist, transactional, never loses.
- **Gary** — raccoon in reading glasses. Unfailingly reasonable, which is the weapon.
- **Michael and Lyndie** — the owners, cartooned from photographs.

Tone: Simpsons structure, Family Guy devices, South Park satirical spine, PG ceiling.

---

## 3. Anatomy of a shot prompt

In this order. `ep03-house-rules/prompts/blocks.py` is the working implementation.

1. **Style** — the look, plus its negatives. Ours is 3D Pixar-style. Never let an example
   prompt for a different show change it.
2. **On-model** — characters identical between shots; never change coat pattern,
   proportions, eye appearance or size relationship.
3. **Location** — **byte-identical for every shot in the same room, across the whole
   episode.** Name the wrong environment explicitly in the negatives; "indoors" alone is
   not enough.
4. **Character sheets** — full description every time.
5. **Action** — what happens, with the sound effects written **inline, in capitals, on
   the beat**: `MOONEY steps into the hall, WHOOP, goes straight up and SKKKRRT slides
   the length of the floor. CRASH.`
6. **Staging** — camera, eyelines, who is where. See §5.
7. **Head count** — shouted: `EXACTLY TWO CATS, EXACTLY ONE RACCOON, no bird, no humans,
   no other animals.`
8. **Dialogue** — delivery next to the line, then the cap (§4).
9. **Negatives** — no on-screen text; harmless slapstick where relevant.
10. **Audio** — Foley, then the score state, then the mix block (§6). Always last.

---

## 4. The failure modes, and the exact wording that fixes them

### Seedance pads a short line with invented speech
**The most expensive bug the show has hit.** A line under about six words comes back with
a second, unscripted utterance to fill the shot. Four of the owner's Episode 1 notes —
all of them "I can't understand what he's saying" — were this one bug, not the voice.
A-8 said "And?" and then something else 3.4s later; B-10 spoke its line at 1.4s then
muttered until 3.4s; D-4 had three utterances for one line; C-7 opened by calling the
seagull "Mooney". **Cost to fix: 129 credits of re-shoots.**

Cap every line, and ask for the silence as well as forbidding the words:

> He says EXACTLY these words and NOTHING else: "…" Accurate lip sync, clean clearly
> articulated dialogue. Then a brief comedic silence — he speaks no other words at any
> point in this shot, no second sentence, no muttering, no trailing off, no ad-libbed
> dialogue, and does not say anyone's name unless it is in that line. The score drops
> away under the line and stops on it.

Capping the line **exposes a silent tail** where the ad-lib used to be — A-8 held 3.3s of
nothing afterwards. Check onsets *and* offsets after any re-shoot and trim the tail.

### The prompt's adjectives drive the voice harder than any reference clip
"Deep, slow, gravelly" produced a voice so deep the owner rejected it. "Bright, fast,
high-pitched excitable squeak" produced the garble nobody could parse. **Describe
articulation, not pitch.** Now moot for anyone with a locked voice, but it still shapes
the delivery `voice_change` has to work with.

### Characters look at nothing
E-4 had Raichu against a wall looking up at empty air while objecting to Mooney, who sat
beside him. **Name the eyeline and negate the wrong one:** *turns his head sideways to
look directly at Mooney beside him — he does NOT look upward, there is nothing above him*
— and say what the other character is doing meanwhile.

### Characters walk out of a two-shot
`A STATIC LOCKED-OFF WIDE SHOT` + `BOTH REMAIN FULLY INSIDE THE FRAME FOR THE ENTIRE
SHOT` + name who is on which side. **Expect to trim an exit anyway** — the trailer's
kitchen chase left half a second of empty room after both cats had gone.

### The principals turn up in crowd shots
D-7 ("six cats gone feral") cast Mooney as one of them while he was indoors. Shout the
head count, and negate the principals by name in any crowd: `NO black-and-white tuxedo
cat, NO Maine Coon, NO cat with ear tufts.`

### Night drifts back to daylight
`IT IS DEEP NIGHT AND VERY DARK` plus `NO WARM LIGHT, NO GOLDEN LIGHT, NO LAMPLIGHT, NO
DAYLIGHT`, and pass the previous shot's final frame to pin it.

### Generated lettering is garbage
Negate all of it — *no on-screen text, no subtitles, no captions, no letters, no numbers,
no logos, no watermarks* — and composite real text in post with `drawtext` and
`textfile=`. Anything hand-made in frame (charts, banners, signs, a chore wheel) must be
scratches and marks, never letters.

### Posture resets
State it negatively when it must persist: `MOONEY IS SITTING UPRIGHT — he is NOT lying
down, NOT sprawled, NOT flat on the boards.`

### Never write "title sequence" or "text added later"
Describe the shot, never its purpose.

---

## 5. Audio — direct the mix, do not list ingredients

Episode 1 ended every prompt with `Audio: wind, one distant gull, crickets.` and left the
balance to chance. That is why four rounds of notes were about not being able to hear the
dialogue. The owner's own prompts (`LL-BG-Cards/`, 2026-09-13) showed the fix.

**The mix block, verbatim, last, on every prompt:**

> Audio professionally mixed for broadcast television: clear centered dialogue, realistic
> room tone underneath everything so it never feels artificially silent, Foley for paws
> and furniture and objects, exaggerated cartoon effects used SELECTIVELY for jokes only.
> Original score that ducks 6 to 10 dB under dialogue and comes back between lines, and
> stops dead on the punchline. DO NOT FILL EVERY SECOND WITH MUSIC OR EFFECTS — silence
> and reaction pauses are part of the comedy. No copyrighted music.

Three things in there matter more than the rest:

- **"Clear centered dialogue"** and the **6–10 dB duck** go straight at the show's
  longest-running complaint. The duck can *only* come from the prompt: Seedance returns
  one pre-mixed track per shot, score and Foley and dialogue baked together, with no
  stems for the assembler to duck.
- **"Do not fill every second."** Silence is the show's best joke delivery. Episode 1's
  B-9 and B-11 — six blank cat faces, total silence, held far too long, twice — are its
  best-timed shots.
- **Effects "SELECTIVELY, for jokes only"**, or every second gets a cartoon noise.

**The score has a state, and the state changes.** Name what the music is *doing*, not
which instrument is playing, and design one cue per act so the episode has a through-line.
Write the transitions into the shot where they happen: *"…the chase music begins"*,
*"the music stops dead"*. Episode 1 had no score design at all.

**Sound effects go inline, in capitals, on the beat** — not only in the trailing list.

---

## 6. The edit

`ep02-chonk/assemble.py` is the reference implementation for the audio spine. Copy it,
never ep01's.

- **Per-clip loudness matching to −23 LUFS, gain clamped to [−8, +14] dB.** The clamp
  matters: without it, near-silent ambience shots get boosted to dialogue level and the
  wind becomes a roar.
- **A true-peak guard per clip, then a limiter at −1 dBFS on the master.** Without the
  limiter the concatenated master clips at 0.0.
- **A pink-noise room-tone floor (~−52 dBFS) under the whole episode.** The raw clips
  have no room tone — nine of Episode 1's sixty dropped to *absolute digital silence*,
  16.2s in total, which plays as the sound cutting out mid-scene.
- **Mixing a separate narration or music layer over the shot audio will clip**, even with
  the limiter, because two near-full-scale layers sum and a 5 ms attack lets the transient
  through. Pre-attenuate 3 dB and use a 1 ms attack.
- **Head AND tail trims.** Seedance front-loads dead air: 30 of Episode 1's 41 dialogue
  shots waited over 1.2s before anyone spoke — 61 seconds of nothing in a 5:30 cut.
  Measure **voiced onset**, not loudness: A-6 measured 0.03s by loudness and 3.07s by
  voiced onset, and the second number is the true one.
- **A trailer cuts on the beat**; give every shot an explicit IN and OUT rather than a
  head trim only. See `series/trailer/assemble.py`.

**Still to build** (from the owner's editing master prompt, both free in ffmpeg):
J-cuts and L-cuts so audio carries across a cut, and 2–3 frame visual impact accents on
major crashes. Also asked for and already covered by the trim tables: reaction shots kept
after punchlines, no cut immediately after every spoken sentence, 0.5–1.5s of silence
around important jokes.

The line to keep above the edit bay: *the finished cartoon must feel intentionally
storyboarded rather than a collection of unrelated AI video clips.*

---

## 7. Measuring without ears

There is no transcription key. Everything audio has been verified by measurement.

- **`ep02-chonk/speech_map.py`** prints a voiced/unvoiced timeline per clip and lists the
  utterances. Word groups are visible — "I will die before you eat again" shows six spans.
  This is how every dialogue bug in Episode 1 was found and confirmed fixed.
- **Engine rumble, gulls, music and strings register as voiced.** Re-run through the
  300–3400 Hz speech band (`--speech`) before concluding a clip has extra dialogue in it.
  CO-2 looked like four utterances until it was measured that way; it was one line.
- **F0 after `voice_change` is noisy on short clips** — some read *higher* after
  revoicing. To prove a voice was actually replaced, cross-correlate old against new;
  all seventeen of Episode 1's came back at |r| < 0.11.
- **`pacing.py`** measures voiced onset for the trim table. **`voicecheck.py`** measures
  median F0 per speaking shot. Residual pitch spread after revoicing is normal prosody
  from one actor — **do not "correct" it.** Chasing that number is what wrecked the audio
  the first time.
- Frame-sampling does not catch continuity. To find re-staging, compare the **last frame
  of each shot against the first frame of the next** — that is what the audience sees.

---

## 8. Economics

Re-check with `models_explore` and `get_cost` before budgeting; both the rate and the
available modes have changed without notice.

| | Cost | Note |
|---|---|---|
| Seedance 2.0 video | **4.5 credits/second** | 4–15s. `mode: fast` no longer exists |
| Seedance 2.5 video | **6.5 credits/second** | 4–30s, holds multi-beat takes with internal cuts |
| `voice_change` | **1 credit** per shot | flat, regardless of length |
| `seed_audio` TTS | **0.1 credits** per line | for narration and any non-diegetic voice |
| Custom voice clone | ~40 credits | a preset is almost always better value |
| Rejected jobs | **free** | |

**The four-second minimum is the real cost driver.** A one-second beat still costs 18
credits. Group short beats into one longer take with time-coded blocks — *0–3 sec:*,
*3–6 sec:* — which also stops a trap and its payoff coming back as two takes that do not
match. A five-minute episode is about 1,450 credits.

**Free forever:** scene dividers, the main title and end plates, all composited text, the
whole assembly and mix, contact sheets, and every measurement script.

**Generation settings that work:** `seedance_2_0`, 720p, 16:9, `genre: comedy`,
`generate_audio: true` (critical), `use_unlim: false`, image references under role
`image_references`. Submit with `generate_video_batch` (max 12, ~8 in flight), poll with
`jobs_wait`, download `result_url` with curl. Never `show_generations`.

---

## 9. The content filter

**Budget one refusal in seven.** It rejected two of fourteen trailer shots, twice each,
over wording that was in no way unsafe — a cat peering round a doorway, a cat settling
onto a couch. Episode 1's E-5 was refused three times across three rewordings and could
never be generated.

- **Rejected jobs are not charged**, so a retry costs only time.
- **Do not attempt a third rewording.** Two failures means design around it.
- **Decide the free fallback before generating** anything slapstick-heavy. When Raichu's
  reveal was refused for the trailer, the crouch shot introduced him instead — and was
  better. When Mooney settling on the couch was refused, reusing the opening shot made
  the trailer return to the exact frame it began on, which was better still.
- Carry `Harmless cartoon slapstick only — nobody is hurt, nobody is injured, everyone is
  fine immediately afterwards` on every pratfall.

---

## 10. Order of work for a new episode

1. **Write the script** as alternating single-speaker shots. Cutaways are free continuity
   — the hard jump is the joke — so use them where staging would otherwise have to match.
2. **Assign every voice** and put them in §1 before generating anything.
3. **Write the prompts** from the script rather than beside it, so they cannot drift.
   Validate that every one carries the mix block, a score cue, a head count and the text
   negative; a missing one is invisible until the footage is wrong.
4. **Shoot one shot of each kind first** — one dialogue, one action — and listen before
   committing an act.
5. **Generate**, in batches of ~8, with the free fallback decided for the risky ones.
6. **Revoice** every single-speaker dialogue shot, 1 credit each.
7. **Measure** onsets and offsets, build the trim tables, assemble, check the master for
   clipping and dead air.
8. **Watch it end to end with sound** before calling it finished. Nothing in this file
   substitutes for that, and it is the step that has been skipped most often.

---

## 11. Reference assets

| Asset | Media ID |
|---|---|
| Cast, both cats, correct ear tufts | `9d60de2f-0261-4a47-b0c8-da570ed6e38a` |
| Living room interior | `3c223738-22f6-4de6-bfd6-6c62333be42c` |
| Gerald the gull | `32f71a43-98f7-4f0f-88db-729ac34a90d8` |
| Gary the raccoon | `cb6a617f-f917-4dea-b34b-ce1706bfe3bf` |
| Michael | `0606324c-cfc1-4cbd-a45a-8bb2c5384b6b` |
| Lyndie | `36f7a2a3-7eae-4fac-bb93-d1924413fcf3` |
| Six neighbourhood cats | `b809cefb-d684-441a-b2a0-0383085b7ded` |
| Sticker logo | `abad9a2e-9210-4638-aebb-de7a701f0eda` |

Media IDs are durable; presigned **upload** URLs expire after 24h.
Reusable and free: `series/reusable/MAIN-TITLE.mp4` (10.58s),
`series/reusable/END-CARD.mp4` (8.1s), `series/character-refs/logo-sticker.png`,
and the four scene dividers in `ep02-chonk/divider.py`.

**Continuity:** pass the previous shot's final frame as an `image_reference`.

```bash
ffmpeg -y -sseof -0.4 -i clips/PREV.mp4 -update 1 -frames:v 1 lastframe.png
```

`-sseof`, not `-ss duration-0.1` — the latter silently produces no file. Do not chain
into a cutaway; the discontinuity is the point.

---

## 12. Tooling gotchas

- **ffmpeg on Windows cannot escape drive-letter colons inside a filtergraph.** Run from
  the project directory and use relative paths.
- This ffmpeg has **no glob support** — use numbered sequences for contact sheets.
- **Measuring audio:** `ffmpeg -i X -af volumedetect -f null NUL 2>&1`. Without the full
  redirect it silently yields nothing and looks like "no audio".
- **Put `-ss`/`-t` before `-i`.** After `-i` they are ignored and every measurement
  returns whole-file statistics.
- Parallel generation limit is **8**.
- A very large MCP result is written to a file instead of returned — read it with jq or
  python.
- **Never `cp` over the main checkout.** Sync with `git merge --ff-only`, which refuses
  when local edits are in the way. A copy destroyed an owner's edit on 2026-09-13.
