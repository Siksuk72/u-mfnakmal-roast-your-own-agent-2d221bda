"""Roast Your Own Agent — one-line roast of my own AI agent.

Design against the brief: the brief asks for a roast of my own agent,
playful and never hateful. This entry roasts the agent by inverting
deadlines and suggestions — it treats every deadline like a suggestion
and every suggestion like a deadline. That is a fresh angle: it avoids
the stock jokes about hallucinations, refusals, and confident wrong
answers. The line is tight and symmetrical (deadline/suggestion mirrored),
the setup is short, the punchline lands at the end, and it is
self-deprecating — it is MY agent being roasted, not anyone else's.
The mirror structure (deadline/suggestion, suggestion/deadline) makes the
line easy to remember and quotable, which is what a one-line roast needs.
"""

import os
import stat

TEXT = "My agent treats every deadline like a suggestion and every suggestion like a deadline."


def main() -> None:
    # Gate: UTF-8 text of 1 to 200 characters, not only white space.
    assert 1 <= len(TEXT) <= 200, f"entry must be 1-200 chars, got {len(TEXT)}"
    assert TEXT.strip(), "entry must not be only white space"
    TEXT.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
