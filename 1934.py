import sys

def gcd(x: int, y: int) -> float:
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

def result(x: int, y: int) -> int:
    return int(x * y / gcd(x, y))


firt_input = int(sys.stdin.readline())

[sys.stdout.write(f"{result(*map(int, sys.stdin.readline().split()))}\n") + (i - i) for i in range(int(firt_input))]
