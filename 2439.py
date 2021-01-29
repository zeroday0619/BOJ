import sys

nx = int(sys.stdin.readline())

for i in range(nx):
    for a in range(nx-i-1):
        del a
        sys.stdout.write(' ')
    for b in range(i+1):
        del b
        sys.stdout.write('*')
    del i
    sys.stdout.write(""+"\n")

