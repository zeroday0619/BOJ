from itertools import cycle


data = [int(input()) for i in range(0, 3)]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


source = cycle(data)

a = next(source)
b = next(source)
c = next(source)

res = a * b * c
co = [*str(res)]

for i in number:
    x = co.count(str(i))
    print(x)
