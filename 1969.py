import sys

def Seq(a, g, c, max):
    if max == a:
        return 'A'
    elif max == c:
        return 'C'
    elif max == g:
        return 'G'
    else:
        return 'T'

def main():
    n, m = map(int, sys.stdin.readline().split())
    dna = [sys.stdin.readline().strip() for _ in range(n)]
    max_count = 0
    hamming_distance = 0
    bufferSeq = []
    for i in range(m):
        a, t, g, c = 0, 0, 0, 0
        for j in range(n):
            if dna[j][i] == 'A':
                a += 1
            elif dna[j][i] == 'T':
                t += 1
            elif dna[j][i] == 'G':
                g += 1
            else:
                c += 1
        max_count = max(a, c, g, t)
        hamming_distance += (n - max_count)
        bufferSeq.append(Seq(a, g, c, max_count))

    print(''.join(bufferSeq))
    print(hamming_distance)

if __name__ == "__main__":
    main()