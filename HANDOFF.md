# HANDOFF — The Adventures of Mooney & Raichu

Updated 2026-09-10 (second pass). Read this first; it should let a fresh session resume without re-deriving anything.

---

## What this is

A cartoon series for **CapeCoder**, generated on **Higgsfield** via MCP. Two talking cats on Cape Cod.

- **Mooney** — black-and-white tuxedo. Pronounced **MOO-nee**. Write phonetically as **"Moonie"** in any prompt where the name is spoken aloud. Sarcastic, laid back, food-motivated.
- **Raichu** — brown/black/grey Maine Coon tabby. Pronounced **RYE-choo**. Write phonetically as **"Rye-choo"** when spoken. High energy, mischievous. **Must have long dramatic lynx-tip ear tufts** — spell this out in full in every prompt, never "as established."
- **Gerald** — enormous herring gull, recurring antagonist. Smug, unhurried, never loses. Speaks for the first time in Episode 2.
- **Gary** — raccoon in reading glasses who lives in the armchair and nobody has addressed it.
- **Michael and Lyndie** — the owners. Real people; cartoonised from their photos.

Cats speak English to each other. Tone: Simpsons structure, Family Guy devices, South Park satirical spine, PG ceiling.

---

## Current state

### Episode 1 — "Fowl Play" — COMPLETE but shelved
`ep01-fowl-play/FOWL-PLAY_EPISODE-1.mp4` — 46 shots, 4:54
`ep01-fowl-play/FOWL-PLAY_EP1_TIGHT.mp4` — recut, 4:01, dead air removed

**The owner's verdict: the jokes are weak.** Not the pacing — the writing. Shelved, not deleted. Untouched in this pass.

### Episode 2 — "Chonk" — COMPLETE
`ep02-chonk/CHONK_EPISODE-2.mp4` — **60 shots, 5:26, 99.1 MB**
`ep02-chonk/CHONK_EPISODE-2_preview.mp4` — 16.1 MB, 854x480, for sending

All 60 shots exist, in order, verified. Script followed line for line from `ep02-chonk/chonk.html`.
Main title carries the composited `Episode 2 — "Chonk"` line; teaser carries the STAY TUNED text.

**Second pass, 2026-09-10:** the owner watched it and caught two things frame-review
could not: characters re-staging between shots, and Mooney's voice changing. Both were
real. 15 shots were re-cut to fix them — see "Voice consistency" below. Nobody has
still *listened* with ears (no transcription key configured), but voice consistency is
now measured objectively per shot by `voicecheck.py`.

### Credits
**394.6 on Ultra.** Episode 2 cost 759.5 to build, plus 266 for the voice/staging
fix pass (15 shots re-cut).
**Ultra does NOT include free Seedance** — re-verified this session: `unlim: {available: false}`.
Every video second costs **3.5 credits**, flat and linear. A 5-minute episode is ~1,100 credits.

---

## Reference assets — pass these as `image_references`

| Asset | Media ID |
|---|---|
| Cast (both cats, correct ear tufts) | `9d60de2f-0261-4a47-b0c8-da570ed6e38a` |
| Living room interior (both cats) | `3c223738-22f6-4de6-bfd6-6c62333be42c` |
| **Gerald the gull** | `32f71a43-98f7-4f0f-88db-729ac34a90d8` (re-uploaded 2026-09-10) |
| Gary the raccoon | `cb6a617f-f917-4dea-b34b-ce1706bfe3bf` |
| Michael | `0606324c-cfc1-4cbd-a45a-8bb2c5384b6b` |
| Lyndie | `36f7a2a3-7eae-4fac-bb93-d1924413fcf3` |
| Six neighbourhood cats | `b809cefb-d684-441a-b2a0-0383085b7ded` |
| Sticker logo (for video) | `abad9a2e-9210-4638-aebb-de7a701f0eda` |

### Voice references — pass as `audio_references` (see below)

| Character | Media ID | Source clip | F0 |
|---|---|---|---|
| Mooney | `5b9c99cf-13b6-494c-894a-7cee5e61f56f` | B-6 | 84 Hz |
| Raichu | `d52f2999-456d-4943-8317-feb289f4f9a5` | B-7 | 296 Hz |
| Gary | `f4912f8f-2f7b-4473-9a15-f45e0a2b8db8` | C-11 | 94 Hz |
| Lyndie | `e95bf568-da1d-40e7-9d8a-2996ee6f3960` | CO-1 | 219 Hz |

Local copies in `ep02-chonk/voiceref/`. Gerald has no reference — his three shots were
generated in one batch and are already consistent (119-129 Hz).

**The previous handoff's Gerald row was wrong** — it listed Gary's ID. Fixed above.
Uploaded media IDs are durable; the presigned upload URLs are not (24h).

### Reusable, already built, free forever
- `series/reusable/MAIN-TITLE.mp4` — 10.58s, sticker logo, cartoon theme
- `series/reusable/END-CARD.mp4` — 8.1s, sunset plate + logo + © 2026 CapeCoder + by CapeCoder (text already baked in)
- `series/character-refs/logo-sticker.png` — transparent PNG, correct spelling

---

## Generation settings that work

```
model: seedance_2_0
mode: fast
resolution: 720p
aspect_ratio: 16:9
genre: comedy
generate_audio: true          <-- CRITICAL
use_unlim: false              <-- avoids an unlim prompt that stalls the batch
declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612
duration: 4-15 supported (verified against models_explore)
```

Submit with `generate_video_batch` (max 12/call, keep ~8 in flight), poll with
`jobs_wait`, then download `result_url` with curl. Do not use `show_generations`.

---

## Prompt rules — do not relax them

The eight rules from the first pass all held up. Full working prompt blocks live in
`ep02-chonk/prompts/blocks.py`; all 36 new shot prompts are in `ep02-chonk/prompts/shots.py`
and rendered to `shots.json`. **Copy that structure for Episode 3.**

1. **Byte-identical location block per room, every shot.** Name the wrong environment
   explicitly in the negatives — "indoors" alone is not enough.
2. **Explicit character counts.** `EXACTLY TWO CATS. No humans, no bird, no other animals.`
3. **Negate props the dialogue implies** ("I've been reading" → `no books, no printed matter`).
4. **Voice delivery inline, identical wording every time.** Gerald's, new this episode:
   `in a calm, low, smug, unhurried voice`.
5. **`Audio:` as a terse comma-separated list, always last.**
6. **"Only his mouth moves"** on deadpan shots.
7. **Never say "title sequence"/"text added later."** Describe the shot, never its purpose.
8. **For real on-screen text, composite in post** with `drawtext` + `textfile=`.

### New rules learned this pass

9. **Negate the principals by name in crowd shots.** D-7 ("six cats gone feral") put a
   black-and-white tuxedo cat in the road — Mooney, who was indoors at the time. Adding
   `NO black-and-white tuxedo cat, NO Maine Coon, NO cat with ear tufts` fixed it.
   A shot that says "six cats" will happily cast your leads as two of them.
10. **Night shots drift back to daylight.** C-5 rendered warm and golden in the middle of
    the night-time black-market scene. The fix that worked: `IT IS DEEP NIGHT AND VERY DARK`
    plus `NO WARM LIGHT, NO GOLDEN LIGHT, NO LAMPLIGHT, NO DAYLIGHT, NO SUNSET`, and passing
    the previous shot's final frame as a reference to pin the look.
11. **Lock two-shots explicitly or a character walks out of frame.** E-1's first take let
    Mooney drift out of the sincere sunset two-shot. `A STATIC LOCKED-OFF WIDE TWO-SHOT` +
    `BOTH CATS REMAIN FULLY INSIDE THE FRAME FOR THE ENTIRE SHOT` + naming who sits left and
    right fixed it, and E-2 then matched E-1 exactly using the same wording.
12. **The NSFW filter throws false positives on innocuous wording.** B-12 ("Raichu
    straightens up... something enormous has just occurred to him") was rejected as `nsfw`.
    Rewording to "sits up tall... a big idea has just arrived" passed. **Rejected jobs are
    not charged.** Just reword and resubmit.
13. **Ask for "no readable text" on anything hand-made.** Charts, banners and signs
    otherwise come back covered in garbled lettering.
14. **Posture drifts across cuts inside one scene.** Mooney sat upright in E-1/E-2 then
    was lying down in E-3/E-5; Raichu flipped between lying beside Mooney and sitting
    alone across A-6/A-7/A-8. Fix by passing the previous shot's final frame AND stating
    the posture negatively: `MOONEY IS SITTING UPRIGHT - he is NOT lying down, NOT
    sprawled, NOT flat on the boards.` Verified working on E-3 and E-5.
15. **Keep the scene's geography.** E-4 had Raichu standing against a wall looking UP at
    empty air while objecting to Mooney, who was not in frame — in a scene where the two of
    them sit side by side at the same level. It read as a different scene. Fixed by making
    it a two-shot and stating the eye-line explicitly: `RAICHU TURNS HIS HEAD SIDEWAYS TO
    LOOK DIRECTLY AT MOONEY BESIDE HIM - he does NOT look upward, there is nothing above
    him`, plus `MOONEY does not react and keeps facing the sunset`. Naming what a character
    is looking AT, and what the other one is doing meanwhile, is what makes a reaction beat
    legible.
16. **Frame-sampling does not catch continuity.** Reviewing one frame per shot proves
    order and content, and nothing else. To find re-staging, compare the LAST frame of
    each shot against the FIRST frame of the next within a continuous scene — that is
    what the audience actually sees at the cut. There is a builder for these strips in
    the qa/ workflow.

---

## Voice consistency — THE most important finding

**The first handoff was wrong: Seedance DOES have a voice-ID mechanism.** `seedance_2_0`
accepts an `audio_references` media role. Passing a clip of the character's correct voice,
plus a line in the prompt saying *"X speaks with the EXACT SAME VOICE as the provided audio
reference - the same pitch, texture and cadence. Match that voice precisely"*, reliably pulls
the generated voice onto the reference.

Measured, on 15 re-cut shots:

| Shot | Before | After | Target |
|---|---|---|---|
| D-3 Mooney | 174 Hz | 100 Hz | 84 |
| A-9 Mooney | 147 Hz | 87 Hz | 84 |
| B-4 Mooney | 138 Hz | 86 Hz | 84 |
| A-7 Mooney | 129 Hz | 78 Hz | 84 |
| E-2 Mooney | 117 Hz | 89 Hz | 84 |
| **A-10 Gary** | **262 Hz** | **91 Hz** | 94 |
| E-1 Raichu | 118 Hz | 327 Hz | 296 |
| A-8 Raichu | 146 Hz | 294 Hz | 296 |

Per-character spread across the whole episode, before -> after:

```
MOONEY   84-174 Hz (90 spread)  ->  78-113 Hz (35 spread)
RAICHU  118-356 Hz (238)        -> 258-377 Hz (118)
GARY     94-262 Hz (168)        ->  91- 94 Hz (3)
GERALD  119-129 Hz (11)         -> unchanged, never drifted
LYNDIE  144-219 Hz (75)         -> unchanged, FIX FAILED
```

**Gary was two entirely different characters** — 262 Hz in A-10, 94 Hz in C-11, nearly
1.5 octaves apart. That is fixed.

**Mooney's target is 112 Hz, NOT his deepest take.** The first fix pass anchored him to
B-6 at 84 Hz because the script says "deep, slow, gravelly" — that was an over-correction and
the owner flagged it as too low. His natural median across the original episode was 110 Hz.
Corrected in post with `rubberband=pitch=<ratio>:formant=preserved`, per shot, to land each
on 112 Hz. Formant preservation is what makes this work: the spectral centroid barely moves
(554 -> 578 Hz on a 1.33x shift), so it is a genuine pitch lift and not a chipmunk effect.
Duration is preserved to within 20 ms and the ~2 dB level drop is absorbed by the loudness
pass in assemble.py. Final: **median 111 Hz, range 93-124**. Originals in
`clips/superseded_deep/`. TZ-1 was deliberately excluded — Gary shares that track and
shifting it would undo his fix.

**Lyndie is the one failure.** A-1 did not move (148 -> 144 Hz) even with a clean 219 Hz
reference. Unknown why; the reference was verified uncontaminated. She has only two short
lines in separate scenes, so it was left. If Episode 3 gives her more to say, solve this first.

**Why Gerald never drifted:** his three shots were generated in a single batch. Identical
delivery wording is NOT enough on its own — Seedance re-rolls the voice per generation.
**For Episode 3, build the reference clips FIRST and pass `audio_references` on every
single dialogue shot.** It is the difference between a cast and a lottery.

`ep02-chonk/voicecheck.py` measures median F0 per speaking shot by autocorrelation and
flags outliers. Run it after any batch. It needs numpy only.

---

## Audio — the defect nobody had measured

**Raw Seedance clips carry no continuous room tone.** Across Episode 2's 60 shots, 9 of them
drop to *absolute digital silence* for **16.2 seconds in total** — D-2 alone is silent for
3.6s of its 5.1s. Played back, the sound simply cuts out mid-scene. This is very likely a
real part of why Episode 1 felt like it had dead air.

Levels are also wildly inconsistent: integrated loudness ranges **-51 to -20 LUFS**
(median -29.4) shot to shot.

`ep02-chonk/assemble.py` now fixes both, and Episode 3 should copy it rather than ep01's:

- **Per-clip loudness matching** toward -23 LUFS, gain clamped to [-8, +14] dB. The clamp
  matters: it stops near-silent ambience shots (B-9/B-11 blank faces, D-8) from being
  boosted up to dialogue level and turning wind into a roar. They stay quieter, as intended.
- **A true-peak guard** per clip, then an `alimiter` at -1 dBFS on the master. Without the
  limiter the concatenated master clipped at 0.0 dBFS.
- **A pink-noise room-tone floor** (~-52 dBFS, high/low-passed) under the whole episode, so
  the audio never falls to digital silence. Tune with `BED_GAIN`.

Verified on the final master: peak **-0.7 dBFS**, mean -27.0 dB, **zero dead-air spans**
≥0.8s below -58 dB.

---

## Continuity

**Proven fix, used again this pass:** extract the previous shot's final frame and pass it as
an `image_reference`. Used for B-11 (must match B-9 exactly — the repeated blank-faces gag)
and to pin C-5's night lighting to C-3. Both worked.

```bash
ffmpeg -y -sseof -0.4 -i clips/PREV.mp4 -update 1 -frames:v 1 lastframe.png
# then media_upload -> curl PUT -> media_confirm -> pass as image_references
```

Note `-sseof`, not `-ss duration-0.1` — the latter silently produces no file.

**Do NOT chain blindly.** D-8 ("Raichu alone in the wreckage") must *not* chain from D-7
("six cats gone feral") or the cats come with it. Chain only when the staging genuinely
continues.

**Known, accepted:** kitchen cabinets drift between sage-green and cream across the episode.
Inherent to per-shot generation; not worth 22 regenerations. Cutaways hide most of it.

---

## Tooling notes

- **ffmpeg 7.1.1** on PATH. **PIL 12.2** available and the right tool for text/mask work.
- **ffmpeg on Windows cannot escape drive-letter colons inside a filtergraph.** Run from the
  project directory and use relative paths (`font.ttf`, `text/*.txt`).
- **This build of ffmpeg has no glob support** — `-pattern_type glob` fails. Use numbered
  sequences (`-start_number 1 -i "frames/%02d.png"`) for contact sheets.
- **Measuring audio:** `ffmpeg -i X -af volumedetect -f null /dev/null 2>&1`. Piping without
  the full redirect silently yields nothing and looks like "no audio" — it is not.
- **Seeking for measurement:** put `-ss`/`-t` *before* `-i`. After `-i` they were ignored and
  every span returned whole-file statistics.
- Parallel generation limit is **8 videos** on Ultra.
- `ep02-chonk/assemble.py` is the current assembler. Copy it for Episode 3, not ep01's.

---

## Repository

A GitHub remote was added: `github.com/azpilot2211/The_Adventures_of_Mooney_-_Raichu`.

**Video and generated QA artifacts are gitignored.** The repo holds ~1.1 GB of mp4 and
`FOWL-PLAY_EPISODE-1.mp4` is 113.8 MB — over GitHub's hard 100 MB per-file limit, so a plain
push would be rejected. Committed instead: the scripts, prompt sources, assembler, episode
HTML and character reference art — everything needed to regenerate.

If the rendered episodes should live on GitHub, that needs **Git LFS**, and 1.1 GB exceeds
the 1 GB free LFS quota. Decide before enabling it.

---

## Next actions

1. **Watch `CHONK_EPISODE-2_preview.mp4` with sound** and confirm the re-cut voices land.
   Pitch is now consistent by measurement, but whether the *performance* is funny is a
   judgement no script can make.
2. Write Episode 3. Gary moves in properly — the teaser has committed to it.
3. **For Episode 3, generate the voice reference clips first** and pass `audio_references`
   on every dialogue shot from the start. Retro-fitting cost 266 credits on this episode;
   doing it up front costs nothing.
4. Superseded v1 clips are kept in `ep02-chonk/clips/superseded_v1/` if any re-cut turns
   out worse than the original.
