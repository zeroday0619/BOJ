"""
3
21 Junkyu
21 Dohyun
20 Sunyoung
"""

count = int(input())

data = []

while count > 0:
    count -= 1
    age, name = input().split(" ")
    data.append([int(age), name])

data.sort(key=lambda x: x[0])    

[print(f"{i[0]} {i[1]}")for i in data]