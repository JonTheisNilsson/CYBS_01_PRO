import sys

count = 0
print("test")
print("oh no, my {err}", file=sys.stderr)
raise SystemExit(1)  