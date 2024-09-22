import sys
import math

def calculate(a, b, h):
    if a == b:
        return -1 
    elif a == 0:
        return (b ** 2 + h ** 2) * math.pi
    elif a < b:
        return (((b * h / (b - a)) ** 2 + b ** 2) - (((b * h / (b - a)) - h) ** 2 + a ** 2)) * math.pi
    elif a > b:
        return (((a * h / (a - b)) ** 2 + a ** 2) - (((a * h / (a - b)) - h) ** 2 + b ** 2)) * math.pi
    else:
        return ((a * h / (a - b)) - (((a * h / (a- b)) - h) ** 2 + b ** 2)) * math.pi

if __name__ == "__main__":
    a, b, h = map(int, sys.stdin.readline().split())
    print(calculate(a, b, h))