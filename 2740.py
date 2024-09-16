import sys

def matrix_multiply(A, B):
    n, m = len(A), len(A[0])
    k = len(B[0])
    result = [[0] * k for _ in range(n)]

    for i in range(n):
        for j in range(k):
            for l in range(m):
                result[i][j] += A[i][l] * B[l][j]

    return result


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    M, K = map(int, sys.stdin.readline().split())
    B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    result = matrix_multiply(A, B)

    for row in result:
        print(' '.join(map(str, row)))
