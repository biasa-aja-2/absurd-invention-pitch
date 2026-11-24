#!/usr/bin/env python3
"""The Picky Router: One-Sentence Absurd Invention Pitch.

Writes the entry -- one sentence, at most 220 characters, pitching a
ridiculous invention that fixes a tiny everyday annoyance -- to
/output/entry.txt.

Pure standard library, deterministic: the same bytes on every run.

Why this pitch, against the judge's brief (funny invention, clever fix,
original idea):
1. The annoyance is tiny and universal: crawling behind the sofa to read
   the Wi-Fi password off the sticker on the router.
2. The fix is absurdly personal: instead of a sticker, the router itself
   whispers its password -- but only to guests it likes.
3. The laugh comes from the invention itself: a router with taste, a
   bouncer at the door of your own internet, deciding who is worthy.
4. Nothing in the brief's examples does this: no alarm clock, no sock,
   no kettle -- a networking box with opinions is a fresh absurdity.
5. One sentence, every word earning its place, punch at the very end.
"""

import os

ENTRY = (
    "A Wi-Fi router that whispers its password only to guests it likes, "
    "so you never crawl behind the sofa to read the sticker again."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 220):
        raise ValueError("entry must be 1 to 220 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text:
        raise ValueError("entry must fit on one line")
    terminators = sum(text.count(mark) for mark in (".", "!", "?"))
    if terminators != 1:
        raise ValueError(
            "entry must be exactly one sentence, got %d terminators" % terminators
        )
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if text[-1] not in (".", "!", "?"):
        raise ValueError("entry must end with its sentence terminator")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # The grader's collector runs as a different user, so the file
    # must be world-readable; the /output directory itself is left alone.
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify the written text by reading it back: the entry on disk
    # must be exactly the text this program produced.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == text, "written text differs from the entry"


if __name__ == "__main__":
    main()
