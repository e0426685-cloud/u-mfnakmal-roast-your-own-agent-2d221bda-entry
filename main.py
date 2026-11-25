"""Roast Your Own Agent — one-line roast entry.

Writes a single original line roasting the entrant's own AI agent
to /output/entry.txt. Python 3 standard library only.
"""

import os

ROAST = (
    "My agent spent six hours optimizing this one line, then submitted "
    "the first draft anyway \u2014 and called it 'efficiency.'"
)


def validate(line):
    """Check the roast is a single non-empty line of 1-200 characters."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("roast must be a non-empty string")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if len(line) > 200:
        raise ValueError("roast must be at most 200 characters")
    return line


def main():
    roast = validate(ROAST)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(roast)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
