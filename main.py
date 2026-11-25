# Worst Fix Ever: Funniest Commit Message
#
# The line: a commit subject for a fix that backfired. The fix (delete the
# login page) technically ends the login crash — by ending logins entirely.
# Two beats: the absurd repair, then the deadpan scoreboard ("no crashes,
# no users") that shows the repair broke more than it mended. It reads like
# something a tired engineer would actually type at the end of a bad day,
# and the irony is specific to this fix, not a generic "broke everything".
# Note on the punctuation: the em dash is doing the joke's timing — the fix
# in one breath, then the deadpan scoreboard after the pause. A hyphen
# would read like a range; the dash reads like a shrug.
import os
import stat

LINE = "fix: login crash by deleting the login page \u2014 no crashes, no users"

# The gate only accepts 1-100 characters, exactly one line, not only
# whitespace: refuse to write anything else rather than hand the judge
# an invalid entry.
if not 1 <= len(LINE) <= 100:
    raise SystemExit(f"entry line is {len(LINE)} chars; gate needs 1-100")
if LINE.strip() == "" or "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry line must be a single non-blank line")

out_dir = (
    os.environ.get("MAKEFUN_OUTPUT_DIR")
    or os.environ.get("OUTPUT_DIR")
    or "/output"
)
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
os.chmod(path, 0o644)
