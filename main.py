"""One Line, One Chill: writes the entry text to /output/entry.txt.

The line is fixed and the output byte-identical on every run. The program
touches no network and reads nothing outside its own source.
"""
import os
import sys

LINE = (
    "My mother's handwriting grows younger every week, "
    "and this morning the shopping list was in mine."
)
MAX_CHARS = 200


def target_path():
    """The harness hands us /output; a local run may not have it."""
    for base in ("/output", os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")):
        try:
            os.makedirs(base, exist_ok=True)
            probe = os.path.join(base, ".probe")
            with open(probe, "w", encoding="utf-8"):
                pass
            os.unlink(probe)
            return os.path.join(base, "entry.txt")
        except OSError:
            continue
    raise SystemExit("no writable output directory")


def main():
    # Hold the entry to the gate ourselves: 1..200 characters, not blank.
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS or not text:
        raise SystemExit("line fails the gate")
    with open(target_path(), "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
