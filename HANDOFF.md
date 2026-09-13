# HANDOFF — The Adventures of Mooney & Raichu

Rewritten 2026-09-10, extended through 2026-09-12. Everything here is current and
verified; superseded advice is replaced rather than patched around. The rest of the
file is reference — read it before generating anything. This first block is where to
begin.

---

## START HERE — state at the end of 2026-09-12

**Three things exist. Two of them are waiting on your ears, and nothing is blocked
on me.**

| | What | Where | Status |
|---|---|---|---|
| 1 | **Episode 1 "Chonk"** | `ep02-chonk/CHONK_EPISODE-1.mp4` | v8, 4:33.7, 69 segments. All twelve of the owner's notes are in it. **Sent for review; no verdict yet.** |
| 2 | **Channel trailer** | `series/TRAILER.mp4` | 34.6s. **Sent for review; no verdict yet.** |
| 3 | **Episode 2 "House Rules"** | `ep03-house-rules/` | Script only. 63 shots, 5:47, needs 1,458 credits. Nothing generated. |

**Balance: 16.2 credits** (measured 2026-09-13). That is below the cost of a single
shot — Seedance 2.0's four-second minimum is 18 credits — so **nothing at all can be
generated until a top-up**, not even a one-shot test. Episode 2 needs 1,458.

### The first move, in order

1. **Get the owner's verdict on the episode and the trailer.** Both were delivered
   without being heard end to end — everything in them was verified by measurement
   and by frames, never by ear. Until that verdict exists, do not start Episode 2:
   any note that comes back will change how its prompts get written.
2. **While waiting, spend nothing and do the free work:** regenerate the YouTube
   chapter timestamps (the cut is 4:33.7 now, the old ones are from 4:34), and write
   the trailer's own title, description and thumbnail — the channel-trailer slot is a
   separate upload from the episode.
3. **Choose Gary's and Gerald's voices** from `series/VOICES.html` — choosing is free,
   the page has inline previews. Applying them to Episode 1's six reachable shots
   (A-1 Lyndie, A-10 and C-11 Gary, C-4/C-6/C-8 Gerald) costs 6 credits and finishes
   its voice work; CO-1 and TZ-1 have two speakers each and can never be reached.
   It is the one Episode 1 mistake
   that is cheapest to avoid repeating — Gary carries seven lines in Episode 2 and is
   the antagonist.
4. **Then Episode 2**, once there are credits. Read the production notes in
   `ep03-house-rules/house-rules.html` before writing a single prompt; they carry every
   lesson from Episode 1 and the trailer, applied per shot.

### The audio technique, learned 2026-09-13

The owner's example prompt (`LL-BG-Cards/example-prompt.txt`) showed what our prompts
were missing. Episode 1 ended every prompt with an ingredient list — *"wind, one distant
gull, crickets."* — and left the balance to chance. The example **directs the mix**:

> *Audio professionally mixed for television: clear centered dialogue, subtle room
> ambience, cartoon Foley, precisely timed comedic SFX, original playful orchestral/jazz
> score that ducks under speech, musical stops around punchlines, no copyrighted music.*

*Clear centered dialogue* and *ducks under speech* go straight at the complaint that drove
the whole Episode 1 rework. It is now in `ep03-house-rules/prompts/blocks.py` as
`AUDIO_MIX`, appended verbatim to every prompt, along with four more things from the
same file:

- **The score has a state and the state changes.** One cue per act in `SCORE`, named by
  what the music is *doing*, stamped onto every prompt by `audio()`. Episode 1 had no
  score design at all.
- **"Brief comedic silence after the line"** — the positive half of our ad-lib cap, now
  in `only()`. Forbidding extra words left a vacuum; asking for the silence fills it.
- **Time-coded beat blocks** (`beats()`) — *0-4 sec:*, *4-8 sec:* — carry several gags in
  one take. Buys reliability and rhythm, not credits.
- **"Harmless slapstick only"** — a filter hedge on Act Two, which is nothing but
  pratfalls and is the most refusal-prone thing we have written.

`prompts/worked_examples.py` writes three shots out in full — one dialogue, one action,
one montage — so the shape is settled before the other sixty get written. **None of it is tested by me** — and at 16.2 credits none of it can be. But the owner
appears to have run the example prompt itself on 2026-09-13 (a single 67.5-credit
Seedance **2.0** charge, 15 seconds, the exact length the file asks for), so the
verdict may already exist by ear. **Ask before spending anything to re-derive it.**

Not taken: the example is a 2D hand-drawn show and negates 3D. Ours is established
3D Pixar-style across a finished episode and a trailer. Take the technique, never the look.

### Numbering, settled 2026-09-12

Fowl Play was **discarded and has no number**. Chonk is **Episode 1**. House Rules is
**Episode 2**. The folder names are production order and no longer match — `ep02-chonk/`
holds Episode 1 and `ep03-house-rules/` holds Episode 2. That is deliberate; do not
"fix" one to match the other without renaming everything at once.

### Git

Branch **`claude/cartoon-changes-fixes-33c9dc`**, seven commits, pushed to origin.
**`main` has not been updated** — this project historically lives on main, so the work
is on GitHub but not where you would look for it. Fast-forward main when the owner is
happy. The main checkout's working tree shows those same files as modified; they are
byte-identical copies made so the scripts sit beside the media, and they resolve to
nothing once main catches up.

---

## What this is

A cartoon series for **CapeCoder**, generated on **Higgsfield** via MCP. Two talking
cats on Cape Cod.

- **Mooney** — black-and-white tuxedo, very overweight. Pronounced **MOO-nee**; write
  it phonetically as **"Moonie"** in any prompt where the name is spoken aloud.
  Sarcastic, laid back, food-motivated.
- **Raichu** — brown/black/grey Maine Coon tabby. Pronounced **RYE-choo**; write
  **"Rye-choo"** when spoken. High energy, mischievous. **Must have long dramatic
  lynx-tip ear tufts** — spell this out in full in every prompt, never "as established".
- **Gerald** — enormous herring gull, recurring antagonist. Smug, unhurried, never loses.
- **Gary** — raccoon in reading glasses who lives in the armchair and nobody has addressed it.
- **Michael and Lyndie** — the owners. Real people, cartoonised from their photos.

Cats speak English to each other. Tone: Simpsons structure, Family Guy devices,
South Park satirical spine, PG ceiling.

---

## Current state

### "Fowl Play" — DISCARDED (it was Episode 1 before the renumber; it has no number now)
`ep01-fowl-play/FOWL-PLAY_EPISODE-1.mp4` — 46 shots, 4:54
`ep01-fowl-play/FOWL-PLAY_EP1_TIGHT.mp4` — recut, 4:01

The owner's verdict: the jokes are weak. Not the pacing, the writing. Untouched this
session. **If it is ever revived, it needs the voice_change pass and the dead-air trim
described below — both problems are almost certainly in it too.**

### Episode 1 — "Chonk" — COMPLETE, v8  (renumbered from Ep2 on 2026-09-11)
`ep02-chonk/CHONK_EPISODE-1.mp4` — **69 segments, 4:33.7, 85.4 MB**
(folder is still named ep02-chonk; only the episode number changed)
`ep02-chonk/CHONK_EPISODE-1_preview.mp4` — 13.5 MB, 854x480, for sending

69 = 60 script shots + 8 scene dividers + the like/subscribe outro.
Title card reads Episode 1; the episode line is drawtext from text/episode.txt, free to change.
Script followed line for line from `ep02-chonk/chonk.html`.
Master: peak -1.6 dBFS, no clipping, zero dead-air spans.

**Nobody has listened to the final cut end to end with ears.** There is no
transcription key configured, so everything audio was verified by measurement
and by frames. The owner reviewed v1-v7 by ear and drove the fixes; v8 — seven
re-shot shots and Raichu's Miles voice — has not been heard yet. **Start there.**

### Episode 2 — "House Rules" — SCRIPT WRITTEN, nothing generated
`ep03-house-rules/` — **63 shots, 5:47, 1,458 credits of new footage.**
(folder is ep03 because it is the third production; it is Episode 2 on screen.
`ep02-chonk/` is Episode 1. Production order and broadcast order stopped matching
when Fowl Play was shelved — do not "fix" one to match the other.)

Gary moves in, which the Episode 1 teaser committed to. The cats set traps; every
trap lands on the cat who set it; Gary wins by being entirely within his rights.
Tom and Jerry in the middle, Family Guy at the edges, the South Park turn in Act Four.

`script.py` holds the shot list and renders `house-rules.html`, `house-rules.txt`
and `shots.json`, so timecodes, runtime and credits are computed rather than typed,
and the counts quoted in the production notes are asserted against the shot list on
every render. `shots.json` is what the prompt pass should read.

**Read the production notes in the HTML before writing a single prompt.** They carry
every lesson from Episode 1 and the trailer, applied per shot.

Two things to settle first, both free:
- **Gary and Gerald still have no assigned voice.** Gary has seven lines here and is
  the antagonist. Pick from `series/VOICES.html` and fill in the cast table above.
- **The inline-sound-effect wording is untested on this account.** It comes from the
  owner's Lucky Lots prompt (higgsfield.ai/s/kMh3mXz6BqY), which was generated on
  Seedance **2.5** — so the wording and the model are confounded. Shoot one trap shot
  both ways before committing Act Two.

Priced 2026-09-12: **Seedance 2.0 is 4.5 credits/second, 2.5 is 6.5** (36 vs 52 for
eight seconds). 2.5 reaches 30 seconds where 2.0 stops at 15 and can hold a multi-beat
sequence with an internal cut, which earns the premium only where one long take
replaces three shots that would each waste the four-second minimum. B-11's montage is
the only candidate in this script.

### Credits
**7.6 remaining on Ultra.** Effectively zero — nothing further can be generated
without a top-up. Everything local (assembly, dividers, outro, trims, SEO art) is free.

Costs, measured this session:
- video: **4.5 credits/second**, flat and linear. A 5-minute episode is ~1,400.
  It was 3.5 while `mode: fast` existed; the model catalog now offers only
  `mode: std` on this account, so budget 4.5 and re-check `models_explore` first.
- **`voice_change`: ~1 credit per shot.** Astonishingly cheap. Use it liberally.
- custom voice clone: **~40 credits**, one-off. Prefer a preset voice.
- **Rejected NSFW jobs are not charged.**
- Ultra does NOT include free Seedance: `unlim: {available: false}`, re-verified.

---

## THE MOST IMPORTANT THING: character voices

**Do not try to control voices at generation time. Fix them afterwards with
`voice_change`.**

Seedance generates a **new voice for every shot**. `audio_references` only nudges it,
prompt wording moves it a bit further, and pitch-shifting forces the number while
wrecking the audio. A whole session was burned learning this. Pitch (F0) is one
dimension of a voice — two clips can both sit at 107 Hz and still sound like two
different actors. The owner's words were "his voice is all over the place" and
"sounds robotic", and both were caused by chasing pitch.

**`voice_change`** replaces the spoken voice in a finished clip with one chosen voice,
keeping the original timing, lip-sync and visuals. Same voice on every shot = the
character has one voice, with zero processing.

### Cast voices — locked

| Character | Voice | voice_id | type |
|---|---|---|---|
| **Mooney** | Cillian (preset) | `d8ba9f14-8a24-44db-932b-99e16c45bd32` | `preset` |
| **Raichu** | **Miles (preset)** | `e18664a7-ee4f-5273-acf8-533eb24cd366` | `preset` |
|  | *chosen by the owner 2026-09-11 after auditioning all 113 presets in `series/VOICES.html`. Applied to all 17 Raichu-solo shots on 2026-09-11.* |  |  |
|  | *Still unconfirmed by ear: Miles was Mooney's original voice, rejected then as too deep. Mooney is Cillian now, so the open question is whether the two read as distinct characters when they talk to each other. Listen to Act One, which is nothing but the two of them.* |  |  |
| Gerald | not yet assigned (never drifted, 119-129 Hz) | — | — |
| Gary | not yet assigned | — | — |

Also available, unused: a clone of Mooney's A-12 "I have never been hungry" take,
`e1f028f2-9e60-4659-9a86-07e6f285112f`, voice_type `element`. Cost 40 credits. Kept in
case Mooney should ever *be* that take rather than Cillian.

### How to run the pass
1. Generate the shot normally, whatever voice comes out.
2. Upload the finished clip (`media_upload` -> PUT -> `media_confirm` type='video'),
   or reuse the generation `job_id` directly — `voice_change` accepts either.
3. `voice_change(video_id, voice_id, voice_type)`.
4. Feed it the **least processed** source available. Never a pitch-shifted clip.

### The one rule that constrains it
**Only revoice shots where that character is the ONLY speaker.** `voice_change`
converts every voice on the track. In Episode 2 these three keep their original audio
for that reason:

- `CO-2_carrier` — Michael speaks off-screen
- `CO-5_the-portion` — Lyndie speaks
- `A-12_never-been-hungry` — Raichu answers mid-shot

A-12 is the take the owner singled out as Mooney's ideal voice, so leaving it is no loss.

**Residual pitch spread after revoicing (Mooney is 90-137 Hz) is normal prosody from a
single actor. Do not "correct" it.** That mistake is what started the whole problem.

**For Episode 2 "House Rules": assign a preset voice per character up front, record it in the table
above, and run voice_change as a finishing pass on every dialogue shot.** Budget about
1 credit per shot. Do not fight the generator.

`ep02-chonk/voicecheck.py` measures median F0 per speaking shot and flags outliers.
Useful for spotting a shot that was missed by the pass — **not** as a quality target.

---

## Pacing: Seedance front-loads dead air

Measured across Episode 2: **30 of 41 dialogue shots waited over 1.2s before the
character spoke — about 61 seconds of dead air** in a 5:30 cut. The character stands
there, then talks. This is very likely why Episode 1 felt slow and got recut.

`ep02-chonk/pacing.py` measures **voiced onset** — the first sustained run of frames
with a detectable fundamental in that character's range. This matters: a plain
loudness gate gets it wrong, because several shots open with a foley hit or a quiet
decaying tail before a long gap and then the real line. A-6 "Name one" measured 0.03s
by loudness and **3.07s** by voiced onset. The second number is the true one.

`assemble.py` holds a `TRIM` table (28 shots, 56s removed) that cuts each shot's head
so the line lands ~0.6s in. Shots whose opening carries a visual beat keep a longer
lead-in — the laser reveal, the "that's the portion" beat, Gerald's stillness, Gary
noticing the camera.

**Set `TRIM` to an empty dict to restore untrimmed pacing.** Regenerate the table any
time clips change — onsets move.

Adding `HE STARTS TALKING IMMEDIATELY - the line begins in the first half second` to a
prompt sometimes works (A-12 came back starting at 0.03s), but not reliably. Trim anyway.

---

## Audio: the clips have no room tone

Nine of the 60 shots drop to **absolute digital silence** for 16.2s in total; D-2 was
silent for 3.6s of its 5.1s. Played back, the sound simply cuts out mid-scene.
Loudness also ranged **-51 to -20 LUFS** shot to shot.

`ep02-chonk/assemble.py` fixes all of it and House Rules should copy it, not Fowl Play's:

- per-clip loudness matching to -23 LUFS, gain clamped to [-8, +14] dB. **The clamp
  matters** — it stops near-silent ambience shots (B-9/B-11 blank faces, D-8) from
  being boosted to dialogue level and turning wind into a roar.
- a true-peak guard per clip, then an `alimiter` at -1 dBFS on the master. Without the
  limiter the concatenated master clipped at 0.0 dBFS.
- a pink-noise room-tone floor (~-52 dBFS) under the whole episode so audio never
  falls to digital silence. Tune with `BED_GAIN`.

**rubberband can overshoot into clipping.** If it is ever used again: pre-attenuate
9 dB, process, then peak-match to the source. Three clips were silently destroyed
before this was caught.

---

## Prompt rules — do not relax them

Full working blocks in `ep02-chonk/prompts/blocks.py`; all 36 shot prompts in
`prompts/shots.py`, rendered to `shots.json`. **Copy that structure for House Rules.**

1. **Byte-identical location block per room, every shot.** Name the wrong environment
   explicitly in the negatives — "indoors" alone is not enough.
2. **Explicit character counts.** `EXACTLY TWO CATS. No humans, no bird, no other animals.`
3. **Negate props the dialogue implies** ("I've been reading" -> `no books, no printed matter`).
4. **Do NOT write "deep" in a voice description.** Rule 4 used to mandate
   "deep, slow, gravelly, half-asleep drawl" for Mooney — that wording was itself
   instructing the too-deep voice. Removing it and asking for a MID-PITCHED register
   moved a shot from 86 to 107 Hz in natural audio. Now moot for Mooney since
   voice_change handles it, but the lesson generalises: **the prompt's adjectives
   drive the voice harder than any reference clip.**
5. **`Audio:` as a terse comma-separated list, always last.**
6. **"Only his mouth moves"** on deadpan shots.
7. **Never say "title sequence" / "text added later."** Describe the shot, never its purpose.
8. **For real on-screen text, composite in post** with `drawtext` + `textfile=`.
9. **Negate the principals by name in crowd shots.** D-7 ("six cats gone feral") cast
   Mooney as one of them while he was indoors. `NO black-and-white tuxedo cat, NO
   Maine Coon, NO cat with ear tufts` fixed it.
10. **Night shots drift back to daylight.** Use `IT IS DEEP NIGHT AND VERY DARK` plus
    `NO WARM LIGHT, NO GOLDEN LIGHT, NO LAMPLIGHT, NO DAYLIGHT`, and pass the previous
    shot's final frame to pin the look.
11. **Lock two-shots explicitly or a character walks out of frame.** `A STATIC
    LOCKED-OFF WIDE TWO-SHOT` + `BOTH CATS REMAIN FULLY INSIDE THE FRAME FOR THE
    ENTIRE SHOT` + naming who sits left and right.
12. **Keep the scene's geography and name the eye-line.** E-4 had Raichu standing
    against a wall looking UP at empty air while objecting to Mooney, who was not in
    frame — in a scene where they sit side by side. Fixed with `RAICHU TURNS HIS HEAD
    SIDEWAYS TO LOOK DIRECTLY AT MOONEY BESIDE HIM - he does NOT look upward, there is
    nothing above him`, plus saying what the other character does meanwhile.
13. **State posture negatively when it must persist:** `MOONEY IS SITTING UPRIGHT - he
    is NOT lying down, NOT sprawled, NOT flat on the boards.`
14. **Ask for "no readable text" on anything hand-made** — charts, banners, signs.
15. **The NSFW filter throws false positives.** B-12 ("something enormous has just
    occurred to him") was rejected; rewording passed. **E-5 "And I'd do it again"
    was rejected three times across three rewordings and could never be regenerated.**
    Rejected jobs are not charged.

---

## Continuity

**Proven fix:** pass the previous shot's final frame as an `image_reference`.

```bash
ffmpeg -y -sseof -0.4 -i clips/PREV.mp4 -update 1 -frames:v 1 lastframe.png
# then media_upload -> curl PUT -> media_confirm -> pass as image_references
```

Note `-sseof`, **not** `-ss duration-0.1` — the latter silently produces no file.

**Do not chain blindly.** D-8 ("Raichu alone in the wreckage") must not chain from D-7
("six cats gone feral") or the cats come with it. Chain only when staging genuinely
continues.

**Frame-sampling does not catch continuity.** One frame per shot proves order and
content and nothing else. To find re-staging, compare the **last frame of each shot
against the first frame of the next** within a continuous scene — that is what the
audience sees at the cut. This is how the E-run posture break was found, and it is the
check that would have caught what the owner caught by watching.

**Known and accepted:** kitchen cabinets drift between sage-green and cream across the
episode. Inherent to per-shot generation; not worth 22 regenerations.

---

## Reference assets — pass as `image_references`

| Asset | Media ID |
|---|---|
| Cast (both cats, correct ear tufts) | `9d60de2f-0261-4a47-b0c8-da570ed6e38a` |
| Living room interior | `3c223738-22f6-4de6-bfd6-6c62333be42c` |
| **Gerald the gull** | `32f71a43-98f7-4f0f-88db-729ac34a90d8` |
| Gary the raccoon | `cb6a617f-f917-4dea-b34b-ce1706bfe3bf` |
| Michael | `0606324c-cfc1-4cbd-a45a-8bb2c5384b6b` |
| Lyndie | `36f7a2a3-7eae-4fac-bb93-d1924413fcf3` |
| Six neighbourhood cats | `b809cefb-d684-441a-b2a0-0383085b7ded` |
| Sticker logo | `abad9a2e-9210-4638-aebb-de7a701f0eda` |

Media IDs are durable; the presigned **upload** URLs expire after 24h.

### Reusable, free forever
- `series/reusable/MAIN-TITLE.mp4` — 10.58s. Logo appears ~9.5s in.
- `series/reusable/END-CARD.mp4` — 8.1s, copyright text already baked in.
- `series/character-refs/logo-sticker.png` — transparent PNG.

---

## Generation settings that work

```
model: seedance_2_0
mode: (omit)                  <-- 'fast' is gone; the catalog offers only 'std'
resolution: 720p
aspect_ratio: 16:9
genre: comedy
generate_audio: true          <-- CRITICAL
use_unlim: false              <-- avoids an unlim prompt that stalls the batch
declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612
duration: 4-15 supported
```

Submit with `generate_video_batch` (max 12/call, keep ~8 in flight), poll with
`jobs_wait`, download `result_url` with curl. Never `show_generations`.
Image references go in `medias` with role **`image_references`**; check the roles
with `models_explore action=get model_id=seedance_2_0` before a batch, and check
the price there too — the per-second rate changed under this account without notice.

---

## Brand elements (all built locally, no credits)

- `ep02-chonk/divider.py` — 0.8s scene divider. Navy card in the logo palette
  (navy `#000048` / cream `#f0f0f0` / gold `#f0d878`) with a diagonal sticker band
  carrying a paw print. Two variants, L and R, alternated. **Placed at the six genuine
  location/time changes only — deliberately NOT at the cutaways**, where the script says
  the unexplained hard jump is the joke. An early version swept the band over black and
  read as a dropout; the card must cover the full frame throughout.
- `ep02-chonk/outro.py` — 5s like/subscribe outro, a paw presses both buttons, bell
  rings, warm pad underneath.
- `YouTube_SEO/build_assets.py` — regenerates all channel art.

---

## Tooling notes

- **ffmpeg 7.1.1**, **PIL 12.2**, **numpy 2.4.6**. No scipy, no librosa, no whisper.
- **ffmpeg on Windows cannot escape drive-letter colons inside a filtergraph.** Run
  from the project directory and use relative paths.
- **This ffmpeg has no glob support.** Use numbered sequences
  (`-start_number 1 -i "frames/%02d.png"`) for contact sheets.
- **Measuring audio:** `ffmpeg -i X -af volumedetect -f null /dev/null 2>&1`. Piping
  without the full redirect silently yields nothing and looks like "no audio".
- **Seeking for measurement:** put `-ss`/`-t` **before** `-i`. After `-i` they were
  ignored and every span returned whole-file statistics.
- Parallel generation limit is **8 videos** on Ultra.
- A very large MCP tool result is written to a file instead of returned — read it with
  jq/python. `media_upload` with 16 files does this.

### Rollback points
`ep02-chonk/clips/superseded_*` hold every previous version of the clips:
`superseded_v1` (pre-fix), `superseded_deep` (pre-pitch-shift), `superseded_v3` / `v4`
(intermediate), **`superseded_prevoice` (immediately before the Cillian pass)**.

---

## YouTube

`YouTube_SEO/` holds `SEO_Text.txt`, `keywords.txt`, `build_assets.py` and 9 images:
avatar (800x800, legible to 48px), banner (2048x1152 with the wordmark inside the
**1235x338** safe band — size the logo by HEIGHT or phones crop it), three thumbnails,
a blank thumbnail template, a safe-area guide and a 150x150 watermark.

Every character count in the copy is script-verified against the live limits.
Chapters use real timestamps from the 4:34 cut — **regenerate them, the cut is now 4:38.**

Two settings that are easy to get wrong: **Made for Kids must be NO** (yes disables
comments, end screens and the subscribe element), and the synthetic-content disclosure
is a per-episode judgement.

Placeholders still to fill: `[YOUR EMAIL]`, `[LINK]`, `[PLAYLIST LINK]`.

---

## Repository

`github.com/azpilot2211/The_Adventures_of_Mooney_-_Raichu`, branch `main`, all pushed.

**Video is gitignored.** ~1.1 GB of mp4 and Episode 1's master is 113.8 MB, over
GitHub's hard 100 MB per-file limit. Committed instead: scripts, prompts, assembler,
episode HTML, SEO pack and character art — everything needed to rebuild. Putting the
rendered episodes on GitHub needs Git LFS, and 1.1 GB exceeds the 1 GB free quota.

---

## Next actions

1. **Watch `CHONK_EPISODE-1_preview.mp4` with sound.** Every item on the owner's
   2026-09-11 list is in it, and none of it has been heard. Listen for:
   Act One, where Mooney (Cillian) and Raichu (Miles) trade lines and could
   read as the same actor; the six re-shot lines, which should each be one
   clean sentence; and the two new divider designs.
2. **Gerald and Gary still have their generated voices.** ~5 credits fixes it,
   same method, single-speaker shots only.
3. Regenerate the YouTube chapter timestamps — the cut is 4:33.7 now.
   The trailer needs its own title, description and thumbnail too; the channel
   trailer slot is a separate upload from the episode.
4. **Watch `series/TRAILER.mp4`** too — 34.6s, also never heard. The narrator is
   Sterling, picked unheard; swapping him is a one-line change in
   `series/trailer/narration.py` and 0.1 credits a line to re-cut.
5. Then Episode 2, **"House Rules"** — the script is written and sitting in
   `ep03-house-rules/`, 1,458 credits at current rates. Assign Gary's and
   Gerald's voices before generating, run voice_change as a finishing pass, and
   cap every short line with the `only()` wording below.

**Balance: 16.2 credits** (measured 2026-09-13) — below the 18-credit cost of one
minimum-length shot.


---

## Session log 2026-09-11

### Free work, earlier in the day

- **Renumbered Chonk to Episode 1.** The episode line is composited with `drawtext`
  from `text/episode.txt` onto the clean plate in `series/reusable/MAIN-TITLE.mp4`,
  so renumbering costs nothing. Rebuilt `clips/TS-1_FINAL_main-title.mp4`.
- **Two dividers added** — before B-1 "I've been reading" and before B-4 "Where did
  you get lasers". Dividers are free; add more wherever a cut feels abrupt.
- **B-1 head trim relaxed** 2.92s -> 1.80s so Raichu has a beat before speaking.
- **Rebuilt**: `CHONK_EPISODE-1.mp4`, 69 segments, 4:41, master peak -1.5 dBFS.
- **Built `series/VOICES.html`** — all 113 presets with inline players, gender filter,
  search, click-to-copy IDs. Regenerate with `series/build_voice_browser.py`.
  Must stay a local file; artifacts cannot load external audio.

### The owner's change list of 2026-09-11 — all 12 items done

Source: `LL-BG-Cards/changes-cartoon-1.txt`. **179 credits spent, 328.6 left.**

| # | Owner's note | Shot | What was done | Cost |
|---|---|---|---|---|
| 1 | "Raichu will use Miles voice" | 17 shots | `voice_change` to Miles | 17 |
| 2 | Mooney's counter line is messed up and cuts off | CO-2 | re-shot 6s without Michael's off-screen line, then revoiced to Cillian | 27+1 |
| 3/4 | can't tell what Raichu says after "watch the door" | A-8 | re-shot: the clip held a second, unscripted utterance | 18+1 |
| 5 | "Gary's fine" punctuation, make it flow | A-11 | script -> "Look, Gary's fine."; re-shot in one breath | 18+1 |
| 6 | divider before "Where did you get lasers" | — | already in place from the previous session | 0 |
| 7 | can't tell what he says after "healthy weight" | B-10 | re-shot; the old clip muttered for 1.2s after its line | 18+1 |
| 8 | dialogue after "where's your bowl" unclear | D-4 | re-shot; three utterances where the script has one | 22.5+1 |
| 9 | Raichu cut off before "I'd do it again" | E-4 | said "Racy?"; re-shot as "That's not the lesson." — E-5 now interrupts him in the edit | 27+1 |
| 10 | Mooney calls the seagull "Mooney" | C-7 | **free**: the stray name sits in its own voiced group with 0.28s of silence after it, so the head trim (1.10 -> 2.55) removes it and lip-sync is untouched | 0 |
| 11 | Raichu looking at the sky | E-1 | re-shot against E-2's own frame; it was also the only E-run shot staged at the wall instead of the rail | 31.5+1 |
| 12 | "a few different scene dividers" | — | two new designs, P and S; the eight placements now cycle L P R S P S L R | 0 |
| | divider before "I've been reading" + a beat | B-1 | already in place | 0 |

### The one thing this session learned: Seedance pads short lines

**Rule 16. A line under about six words comes back with an invented second
utterance to fill the shot.** That single failure mode caused four of the
owner's "I don't understand what he's saying" notes — it was never the voice.
A-8 spoke "And?" and then something else 3.4s later. B-10 said its line at 1.4s
and muttered until 3.4s. D-4 had three utterances. C-7 opened by calling the
seagull "Mooney".

The fix, in every re-shot prompt (`prompts/refix.py`, `only()`):

```
He says EXACTLY these words and NOTHING else: "..."
He speaks no other words at any point in this shot. No second sentence,
no muttering, no whispering, no trailing off, no ad-libbed dialogue,
and he does not say anyone's name.
Before and after that one line he is completely silent.
```

It worked on all six. **Use it on every short line in House Rules.**

Two consequences worth knowing:

- **Capping the line exposes a silent tail.** The ad-lib was filling the back
  half of the shot; without it A-8 held 3.3s of nothing. `assemble.py` grew a
  `TAIL` table alongside `TRIM` for exactly this. Check onsets *and* offsets
  after any re-shoot.
- **Do not write "high-pitched excitable squeak"** in Raichu's voice line
  (`blocks.py` V_RAICHU still does). That wording produced the squeaky garble.
  The re-shoots use `V_RAICHU_CLEAR` in `refix.py`, which asks for articulation
  and says nothing about pitch. Same lesson as rule 4, different character.

### How to tell what a clip actually says without ears

There is still no transcription key. `qa/speech_map.py` (scratch, worth keeping)
prints a voiced/unvoiced timeline per clip and lists the spans. Word groups are
visible: A-2 "I will die before you eat again" shows six spans. That is how
every item above was diagnosed and verified before a credit was spent.

Two traps in it:
- **Engine rumble and gull cries register as voiced.** CO-2 looked like it still
  had four utterances until the same measurement was re-run through a
  300-3400 Hz speech band, which showed one line ending 3s before the clip.
- **F0 after `voice_change` is noisy on short clips.** A-8 reads *higher* after
  revoicing. Cross-correlating the old and new audio (all 17 came back at
  |r| < 0.11) proves the voice was replaced; the pitch number does not.

### Which shots are NOT on a locked voice, and why

Audit it any time with the SPEAKER map in `voicecheck.py` against
`voicechange/media_ids.json` (Cillian) and `voicechange/miles_jobs.json` (Miles).
All 16 Raichu shots and all but three Mooney shots are locked. The rest:

| Shot | Speaker | Why it still has the generated voice |
|---|---|---|
| CO-5_the-portion | Mooney | Lyndie speaks in it |
| A-12_never-been-hungry | Mooney | Raichu answers mid-shot; also the owner's favourite take |
| TZ-1_gary-moves-in | Gary + Mooney | two speakers |
| CO-1, A-1 | Lyndie | no voice assigned |
| A-10, C-11 | Gary | no voice assigned |
| C-4, C-6, C-8 | Gerald | no voice assigned |

`voice_change` converts EVERY voice on a track, so a shot with two speakers can
only be reached by re-shooting it single-speaker first. That is what was done to
CO-2.

**A-9 was not on that list — it was simply missed** by the earlier Cillian pass,
and Mooney changed voice mid-Act-One as a result. Fixed 2026-09-11 for 1 credit.
Run the audit before calling a voice pass done.

### Still not done

- **Gerald, Gary and Lyndie have no assigned voice.** ~7 credits, same method.
- **Nobody has heard v8 end to end.** Everything above was verified by
  measurement and by frames.
- **YouTube chapter timestamps** are still from the 4:34 cut. It is now 4:33.7,
  and every act boundary moved. Regenerate before publishing.
- **E-5 warning stands:** "And I'd do it again" was rejected three times by the
  content filter and could not be regenerated. Do not re-shoot E-5.
- Known and accepted: D-4's kitchen cabinets came back cream where D-3's are
  sage. Same drift the handoff already accepts elsewhere.

### Channel trailer — built 2026-09-11, `series/trailer/`

`series/TRAILER.mp4` — **34.6s, 8.4 MB, 14 segments, peak -3.1 dBFS.**

The 45-second script in `LL-BG-Cards/trailer.txt` prices at ~439 credits at the
new 4.5/second rate, so it was cut to 30 seconds by dropping the "bigger
adventures" tease block — the weakest section with only one episode in the can.
**239 credits of footage, 4 to revoice, 0.7 for narration.**

| file | what it is |
|---|---|
| `prompts.py` | the 14 shot prompts; run it to re-render `trailer.json` |
| `assemble.py` | IN/OUT per shot, not just head trims — a trailer cuts on the beat |
| `card.py` | the reveal card, built locally from the logo sticker. Free |
| `narration.py` | places the narrator's seven lines on their cues |
| `clips/`, `narr/`, `prevoice/` | footage, narration, pre-revoice sources |

Three things worth keeping:

- **Narration is generated separately and mixed in post** (`seed_audio`,
  **0.1 credits a line** — use `get_cost:true` to preflight anything new).
  That means ten of the fourteen shots ask for NO dialogue at all, which is the
  most reliable thing this model does, and the narrator is one voice throughout
  instead of a new one per shot. Narrator is **Sterling**
  `dc382508-c8bd-443c-8cb2-46e57b8d2e6f`, chosen unheard — swap the id in
  `narration.py` and re-run to change it.
- **Every dialogue shot is single-speaker**, so all four could be revoiced to
  Cillian and Miles for 1 credit each. Do not write a two-hander.
- **Mixing narration over the shot audio clipped the master at 0.0 dBFS** even
  with the limiter. Two near-full-scale layers overshoot and a 5ms attack lets
  the transient through. `assemble.py` now pre-attenuates 3 dB and limits with
  a 1ms attack.

**The content filter rejected two shots twice each** and they were dropped
rather than attempted a third time (E-5's lesson):
- T-4, Raichu peering round a doorway at something off-screen. Raichu is
  introduced by the crouch instead, which is the better shot anyway.
- T-12, Mooney settling back onto the couch. The trailer **reuses T-1** for
  that beat, so it returns to the exact frame it opened on before Raichu ruins
  it — free, and a stronger edit than the shot that was refused.

Neither rewording was obviously unsafe, and both shots are innocuous. Assume
one shot in seven will be refused and keep a free fallback in mind for each.

**Known flaw: Mooney reads as a normal-sized cat in the trailer**, not the
chonk he is in the episode, despite the same character block. Re-shooting the
worst offenders is ~90 credits and was out of budget.

### NEVER copy files over the main checkout

**2026-09-13: an owner edit to HANDOFF.md was destroyed this way.** The session was
working in a git worktree, and every push was followed by `cp HANDOFF.md ../../../` to
keep the main checkout current. The owner had added Gary's and Gerald's voices to the
cast table in the meantime; the copy overwrote them with no warning, the edit had never
been committed, and it was unrecoverable.

The copying only existed because the local `main` branch was stale while the remote had
moved. That is fixed — the main checkout is a clean checkout of `origin/main`. From here:

**Sync with `git -C <main checkout> merge --ff-only origin/main`, never with `cp`.**
A merge refuses when local edits are in the way. A copy destroys them silently. If a
merge ever does refuse, read what it is protecting before clearing it — do not blanket
`checkout --` a file you have not diffed.

### The trap that cost a review cycle

This session ran in a git worktree under `.claude/worktrees/`. `clips/`, `qa/`,
`fixes*/` and `series/reusable` were junctioned back to the main checkout, but
**the episode renders to `ep02-chonk/` inside the worktree**, which is a
different directory from the main checkout's. The owner was sent the main
checkout's file and reviewed the previous version, reporting bugs that had
already been fixed. Whenever you build from a worktree, copy
`CHONK_EPISODE-1.mp4` and its preview to the main checkout before sending, and
check the file size and duration against what you just built.
`ep02-chonk/superseded_v7/` holds the version that was mistakenly sent.

### Rollback points added this session

- `clips/superseded_prefix5/` — the seven shots as they were before the re-shoot.
- `clips/superseded_premiles/` — all 17 as they were before the voice pass.
- `fixes5/` — the raw re-shoots, before revoicing.
- `voicechange/miles/` — the revoiced clips as downloaded.
- `voicechange/miles_jobs.json` — shot -> voice_change job id.
