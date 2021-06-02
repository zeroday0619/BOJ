import sys

num = int(sys.stdin.readline()) 

_list = [0] * 10001 

for i in range(num): 
    num_2 = int(sys.stdin.readline()) 
    _list[num_2] = _list[num_2] + 1 

for i in range(10001): 
    if _list[i] != 0:
        for j in range(_list[i]): 
            print(i)

