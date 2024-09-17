import sys


if __name__ == "__main__":
    result = sum([num ** 2 for num in list(map(int, sys.stdin.readline().split()))]) % 10
    print(result)
