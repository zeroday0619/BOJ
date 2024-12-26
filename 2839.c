#include <stdio.h>

int min(int x, int y) {
    return (x < y) ? x : y;
}

int find_min_box(int n) {
    if (n < 3) return -1;
    int dp[n+1];
    
    for (int i = 0; i <= n; i++) {
        dp[i] = 0;
    }

    if (n >= 3) dp[3] = 1;
    if (n >= 5) dp[5] = 1;

    for (int i = 6; i <= n; i++) {
        if (dp[i - 3] > 0) dp[i] = dp[i - 3] + 1;
        if (dp[i - 5] > 0) dp[i] = dp[i] ? min(dp[i], dp[i - 5] + 1) : dp[i - 5] + 1;
    }

    return (dp[n] == 0 ? -1 : dp[n]);
}

int main() {
    int N;
    scanf("%d", &N);
    int res = find_min_box(N);
    printf("%d\n", res);
    return 0;
}