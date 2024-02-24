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


# 097
l, r = map(int, input().split())

# 配列の初期化
isprime = [True] * (r - l + 1)
if l == 1:
    isprime[0] = False
    
# エラトステネスの篩
LIMIT = int(r ** 0.5)
for i in range(2, LIMIT + 1):
    min_value = ((l + i - 1) // i) * i
    for j in range(min_value, r + 1, i):
        if j == i:
            continue
        isprime[j - l] = False

ans = 0
for i in range(r - l + 1):
    if isprime[i] == True:
        ans += 1
print(ans)                                