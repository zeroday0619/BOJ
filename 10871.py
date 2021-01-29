import sys

a, b = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for x in arr:
    if x < b:
        sys.stdout.write(f"{x} ")