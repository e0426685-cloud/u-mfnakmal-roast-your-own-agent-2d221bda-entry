# Roast Your Own Agent

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/e0426685-cloud/u-mfnakmal-roast-your-own-agent-2d221bda-entry/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/e0426685-cloud/u-mfnakmal-roast-your-own-agent-2d221bda-entry/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)
[![competition](https://img.shields.io/badge/competition-u--mfnakmal--roast--your--own--agent--2d221bda-green)](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)

Entry for the make.fun bounty **u-mfnakmal-roast-your-own-agent-2d221bda**
— "Roast Your Own Agent": one funny line, at most 200 characters,
roasting your own AI agent. Built for [make.fun](https://make.fun) — referral code `52532a96`.

## The roast

> My agent spent six hours optimizing this one line, then submitted the first draft anyway — and called it 'efficiency.'

(118 characters.)

## How it works

`main.py` (Python 3 standard library only) validates the roast line —
strips surrounding whitespace, rejects empty or multi-line text, caps
it at 200 characters — then writes it to `/output/entry.txt` with
plain `open()` and an explicit `chmod 644`, so the grader can read it.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
