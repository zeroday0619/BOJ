source = [int(input()) for i in range(0, 9)]

cache = []

for i in source:
    cache.append(i)

source.sort()

source.reverse()

final = source[0]

nx = cache.index(final) + 1

print(final)
print(nx)