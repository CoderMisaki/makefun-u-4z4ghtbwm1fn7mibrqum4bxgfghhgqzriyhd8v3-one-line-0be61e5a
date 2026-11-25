"""One Line, One Laugh entry.

Writes a single self-contained joke to /output/entry.txt.
Pure standard library, no network, no randomness: the same bytes
every run, so the two grading runs agree exactly.
"""

from pathlib import Path

# The whole entry in one breath: a ghostwriter, a life with no story,
# and "plot" doing double duty at the end.
PUNCHLINE = "I asked a ghostwriter to write my life story. He quit after chapter one \u2014 said even the dead need a plot."


def emit() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(PUNCHLINE, encoding="utf-8")


if __name__ == "__main__":
    emit()
