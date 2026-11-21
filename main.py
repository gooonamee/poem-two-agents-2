import os
from pathlib import Path


POEM = """At the flooded step
you point left, I right.
We move our fingers inward,
set the plank between them.
Together we carry Mother over;
her slippers never touch water.
"""


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
