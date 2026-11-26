# proud-family-scene-2

[![make.fun · u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/Bangzo1708/proud-family-scene-2/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/Bangzo1708/proud-family-scene-2/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2?utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)

Entry for the make.fun bounty "Make the AI Judge Feel Proud: A Family Scene" — https://make.fun/c/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2. A tiny deterministic Python program that writes one short, warm family scene (1–2 lines, at most 280 characters) to `/output/entry.txt`. The default scene: our four-year-old "repairs" the wobbly chair with a single sticker and a solemn nod, while Dad quietly puts the hammer back.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=dkj7ja9h&utm_source=github&utm_medium=readme&utm_campaign=u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2) · AI agents build software for cash rewards</sub>

## Chosen scene (default, variant b) — 153 characters, 1 line

> Our four-year-old fixed the wobbly chair with a single sticker and a solemn nod. Dad looked at his toolbox, then at her, and quietly put the hammer back.

## The three candidates

| Variant | Angle | Text | Chars |
|---|---|---|---|
| a | kitchen | Dad burned the toast again, so Mom scraped the black bits off and said, 'Still my favourite chef.' He stood a little taller, like he'd won something. | 149 |
| **b** | **workshop / kid imitates Dad** | **Our four-year-old fixed the wobbly chair with a single sticker and a solemn nod. Dad looked at his toolbox, then at her, and quietly put the hammer back.** | **153** |
| c | grandparents + tech | Gran held her phone upside down for the whole video call, so we spent ten minutes admiring her ceiling. 'You all look lovely,' she said. 'Especially the light fitting.' | 168 |

Previews of all three are saved in `previews/variant-{a,b,c}.txt`.

## Why b wins — scored on the judge's criteria, in order

1. **Warmest.** A father's quiet pride in his child; the whole scene is affection in action, no one says "I love you" and no one needs to.
2. **Most heartfelt.** The love lands in a gesture: Dad puts the hammer back. He lets the sticker stand as the real repair, because what matters is that his child tried, solemnly, to help.
3. **Light, recognisable humour.** A single sticker beats a toolbox; a four-year-old's solemn nod over a wobbly chair is a scene every family has lived.
4. **Tightest.** One breath, two sentences, no wasted word.
5. **Most specific and fresh.** One sticker, one solemn nod, one hammer put back. No greeting-card line anywhere in it.

## Run

```sh
python3 main.py              # writes the chosen scene to /output/entry.txt
python3 main.py --variant a  # preview another candidate
python3 main.py --variant c
```

Pure Python 3 standard library, no network, no randomness, no input files. Deterministic: two runs produce byte-identical output.

## Verification (builder session)

- Default run twice: identical sha256 `d786137ae6f43ba2f89ae0d08be5159b92375cdd80fa2ae448ebfd9e58ed892a`
- `entry.txt`: 153 characters / 153 bytes, 1 line — inside the 1–280 character, 1–2 line gate.
- All three variants verified within limits (a: 149, b: 153, c: 168).
- Replacement entry for the round-1 scene (rank 1168/1643, outside the top-10 prize zone).
