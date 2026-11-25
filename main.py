"""Write the one-line AI excuse to /output/entry.txt and verify it.

The excuse: the agent had to evict the deadline from its own context
window to make room for the apology itself -- the apology ate the
deadline. One line, well under the 200-character cap.
"""

import os

ENTRY = "I had to evict the deadline from my context window to make room for this apology."

OUTPUT_PATHS = ["/output/entry.txt", "./output/entry.txt"]


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"

    written_path = None
    last_error = None
    for path in OUTPUT_PATHS:
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            written_path = path
            break
        except OSError as exc:  # e.g. /output not writable; try the fallback
            last_error = exc
    if written_path is None:
        raise RuntimeError(f"could not write entry: {last_error}")

    with open(written_path, "r", encoding="utf-8") as f:
        read_back = f.read()
    assert read_back == ENTRY, "round-trip mismatch"

    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(f"wrote: {written_path}")


if __name__ == "__main__":
    main()
