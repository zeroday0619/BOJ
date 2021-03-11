import sys

def merge(left: list, right: list):
    if not left or not right:
        return left or right
    
    result = []
    _result = result.append
    while left and right:
        if left[-1] >= right[-1]:
            _result(left.pop())
        else:
            _result(right.pop())
    result.reverse()
    return (left or right) + result


def merge_sort_sep(seq: list):
    if len(seq) < 2:
        return seq
    
    mid = len(seq) // 2
    left = merge_sort_sep(seq[:mid])
    right = merge_sort_sep(seq[mid:])
    return merge(left, right)


firt_input = int(sys.stdin.readline())

data = [int(sys.stdin.readline()) + (i - i) for i in range(firt_input)]

res = merge_sort_sep(data)

def __print(rx):
    sys.stdout.write(f"{rx}\n")

[__print(i) for i in res]