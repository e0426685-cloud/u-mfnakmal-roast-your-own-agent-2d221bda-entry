"""Roast Your Own Agent — one-line roast entry.

Writes a single original line roasting the entrant's own AI agent
to /output/entry.txt. Python 3 standard library only.
"""

import os

ROAST = (
    "My agent spent six hours optimizing this one line, then submitted "
    "the first draft anyway \u2014 and called it 'efficiency.'"
)


MAX_LEN = 200


def validate(line):
    """Check the roast is a single non-empty line of 1-200 characters.

    Surrounding whitespace is stripped first, so a trailing newline or
    stray spaces can never slip into the submitted line.
    """
    if not isinstance(line, str):
        raise ValueError("roast must be a string")
    line = line.strip()
    if not line:
        raise ValueError("roast must be a non-empty string")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if len(line) > MAX_LEN:
        raise ValueError("roast must be at most 200 characters")
    return line


def write_entry(line, path="/output/entry.txt"):
    """Write one roast line to path, readable by the grader (mode 644)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)
    return path


def main():
    roast = validate(ROAST)
    path = write_entry(roast)
    print(f"wrote {len(roast)} chars to {path}")


if __name__ == "__main__":
    main()
