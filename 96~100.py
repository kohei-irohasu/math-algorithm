# 096
n = int(input())
t = list(map(int, input().split()))

# 配列の初期化
sumT = sum(t)
dp = [[False] * (sumT + 1) for i in range(n + 1)]
dp[0][0] = True

# 動的計画法
for i in range(1, n + 1):
    for j in range(sumT + 1):
        if j < t[i - 1]:
            if dp[i - 1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False
        
        if j >= t[i - 1]:
            if dp[i - 1][j] == True or dp[i - 1][j - t[i -1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

ans = 10 ** 10
for i in range(sumT + 1):
    if dp[n][i] == True:
        cooking_time = max(i, sumT - i)
        ans = min(ans, cooking_time)
print(ans)                                         