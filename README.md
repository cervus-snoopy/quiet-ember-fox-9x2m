# One Word From Your Ex

[![Bounty](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![Rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/cervus-snoopy/quiet-ember-fox-9x2m/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![Reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/cervus-snoopy/quiet-ember-fox-9x2m/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

This entry answers with a single word that stamps a former partner like a carton past its sell-by date.

## Run

```sh
python3 main.py
```

The program writes `entry.txt` into `$MAKEFUN_OUTPUT_DIR` (default `/output`), creating the directory if it does not exist yet.

## Verify

```sh
MAKEFUN_OUTPUT_DIR=/tmp/one-word-ex-out python3 main.py
python3 -c "import os; p='/tmp/one-word-ex-out/entry.txt'; d=open(p,'rb').read(); print(len(d), d.endswith(b'\n'), oct(os.stat(p).st_mode & 0o777))"
```

The output file holds one word, 1-24 characters, UTF-8, with no trailing newline and mode 0644.
