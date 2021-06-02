import sys

temp = int(sys.stdin.readline())
del temp

first_input = sys.stdin.readline().replace("\n", "")

array = list(map(int, first_input.split(" ")))
del first_input

sys.stdout.write('{} {}\n'.format(min(array), max(array)))


