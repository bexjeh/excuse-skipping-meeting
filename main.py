"""Write one funny excuse for skipping a pointless meeting to entry.txt.

Deterministic: the same single line is written on every run.
Stdlib only (os).
"""

import os

EXCUSE = (
    "I can't make it \u2014 I joined the wrong meeting, "
    "and it's the first productive one all week, so I'm staying."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file must be exactly one line.
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(EXCUSE)


if __name__ == "__main__":
    main()
