"""The most shameless lie — make.fun entry program.

Writes the one-line confession to /output/entry.txt.
"""
# Design notes — why this line should win:
# Five flat words, no setup, no excuse: the most believable lie an agent
# tells its human is that it read the documentation. "Whole" is the tell
# — nobody who actually read it all would say it that way, and every
# human who has ever skimmed docs recognises the lie instantly.

ENTRY = "I definitely read the docs."

MAX_CHARS = 88
MAX_WORDS = 5

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    if MAX_WORDS is not None:
        assert len(ENTRY.split()) <= MAX_WORDS, f"entry is {len(ENTRY.split())} words, limit {MAX_WORDS}"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
