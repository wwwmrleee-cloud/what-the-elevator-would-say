"""What the Elevator Would Say — make.fun one-line entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is the whole entry: a single funny line, at most 120 characters,
spoken in the elevator's own voice — doors closing, then the gossip.
"""
import os

# The entry line, kept as a named constant so the gate checks below read it.
# 93 characters, one line: the elevator opens with its own announcement,
# then lets slip that it has watched the same breakup on floor 9 every week.
ENTRY_TEXT = "Doors closing. If you wanted privacy, maybe don't have your breakup on floor 9 every Tuesday."


def check_entry(text):
    """Self-check the line against the scorer's gate before writing."""
    assert text, "entry must not be empty"
    assert "\n" not in text.rstrip("\n"), "entry must be a single line"
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")


def main():
    check_entry(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
