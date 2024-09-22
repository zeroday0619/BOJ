import sys

def equal(P, original_index, sorted_index):
    P[original_index] = sorted_index

def find_permutation(A, N):
    P = [0] * N
    [equal(P, original_index, sorted_index) for sorted_index, (_, original_index) in enumerate(sorted((value, index) for index, value in enumerate(A)))]
    return P

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    P = find_permutation(A, N)
    print(*P)


