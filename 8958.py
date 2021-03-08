import sys

case_num = int(sys.stdin.readline())
length = len([i for i in range(case_num)])

_index = 0

while True:
    if _index == length:
        break
    ox = [i for i in sys.stdin.readline()]
    ox.remove("\n")
    score = 0
    score_db = []
    for xc in ox:
        if type(xc) is str:
            if xc == "X":
                score = 0
                continue
            if xc == "O":        
                score += 1
        score_db.append(score)
    print(sum(score_db))
    _index += 1