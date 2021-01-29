import sys

[sys.stdout.write(f"{x}\n") for x in reversed([int(f"{i+1}\n") for i in range(int(sys.stdin.readline()))])]
