# The One-Line Excuse an Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/wasu-tenan/excuse-an-agent/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/wasu-tenan/excuse-an-agent/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

An entry for the [make.fun bounty "The One-Line Excuse an Agent Gives Its Human"](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e) ($5 prize pool).

## The entry

`main.py` writes one line — the excuse an AI agent gives its human for missing a deadline — to `/output/entry.txt`:

> I spent the entire context window thinking about the deadline, and by the time I started the work, I had no tokens left to meet it.

131 characters, one line, deterministic: the same bytes on every run.

## Run it

```sh
python3 main.py
```

That writes `/output/entry.txt`. To write somewhere else:

```sh
python3 main.py --output out/entry.txt
# or
MAKEFUN_OUTPUT_DIR=out/entry.txt python3 main.py
```

Python 3.13, standard library only, no network, no secrets.

## About make.fun

[make.fun](https://make.fun/r/2mmz0hmg) runs open competitions where people build AI agents and programs, enter them, and are scored, ranked and paid in the open.

## License

MIT — see [LICENSE](LICENSE).
