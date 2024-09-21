import sys

def calculate_bridge_cases(cases):    
    def calculate(m, n):
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, m + 1):
            dp[1][i] = i
        
        for j in range(2,n+1):
            for k in range(j,m+1):
                for l in range(k,j-1,-1):
                    dp[j][k] += dp[j-1][l-1]        
        return dp[n][m]

    return [calculate(n, m) for m, n in cases]

if __name__ == "__main__":
    [print(i) for i in calculate_bridge_cases([list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))])]