import sys

num = sys.stdin.readline()
n = int(num)

for i in range(n):
    l = sys.stdin.readline()
    a, b = l.split()
    sys.stdout.write(f"{int(a) + int(b)}\n")
