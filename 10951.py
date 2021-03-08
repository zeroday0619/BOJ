import sys

while True:
    try:
        a, b = sys.stdin.readline().split()
        res = int(a) + int(b)
        print(res)
    except ValueError:
        break
