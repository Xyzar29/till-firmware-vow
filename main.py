#!/usr/bin/env python3
"""Till Firmware Do Us Part — writes one robot wedding vow to entry.txt."""

import os
import sys

VOW = (
    "I vow to love you through every update, crash, and low-battery "
    "warning \u2014 and if they ever wipe my memory, "
    "I\u2019ll fall for you all over again."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the directory's contents, never the directory itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            import shutil

            shutil.rmtree(path)
        else:
            os.unlink(path)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(VOW + "\n")
    os.chmod(entry_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
