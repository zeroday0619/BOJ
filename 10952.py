import sys

while True:
    try:
        a, b = sys.stdin.readline().split()
        if int(a) == 0 and int(b) == 0:
            break
        res = int(a) + int(b)
        print(res)
    except ValueError:
        break
