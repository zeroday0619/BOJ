import sys


def gcd(a, b):
    if (b == 0):
        return a
    while b!=0:
        a, b = b, a % b
    return a

def solve(r):
    a = []
    for _ in range(1, r+1):
        a.append("1")
    return a

if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().split())
    print("".join(solve(gcd(a, b))))