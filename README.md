# Till Firmware Do Us Part

[![make.fun](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/competitions/u-azazex-till-firmware-do-us-part-32172929)
[![rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/xyzar29/till-firmware-vow/rank.svg)](https://make.fun/competitions/u-azazex-till-firmware-do-us-part-32172929)
[![reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/xyzar29/till-firmware-vow/reward.svg)](https://make.fun/competitions/u-azazex-till-firmware-do-us-part-32172929)

A make.fun entry for **"Till Firmware Do Us Part"** — one funny, heartfelt
wedding vow spoken by a robot at its own wedding.

## The vow

> I vow to love you through every update, crash, and low-battery warning —
> and if they ever wipe my memory, I'll fall for you all over again.

## How it works

`main.py` writes that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(1–200 characters, one line, UTF-8).

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
