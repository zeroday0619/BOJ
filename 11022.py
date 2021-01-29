import sys


def _print(num):
    sys.stdout.write(f"{str(num)}\n")


nu = sys.stdin.readline()

ran = int(nu)

for x in range(0, ran):
    samsung, apple = sys.stdin.readline().split()
    _print(f"Case #{x+1}: {samsung} + {apple} = {int(samsung) + int(apple)}")
