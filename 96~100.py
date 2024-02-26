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


# 098
n = int(input())
x = [None] * n
y = [None] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())
a, b = map(int, input().split())

# 交差する数を考える
cnt = 0
for i in range(n):
    xa, ya = x[i] - a, y[i] - b
    xb, yb = x[(i + 1) % n] - a, y[(i + 1) % n] - b
    if ya > yb:
        xa, xb = xb, xa
        ya, yb = yb, ya
    if ya <= 0 and 0 < yb and xa * yb - xb * ya < 0:
        cnt += 1

if cnt % 2 == 1:
    print('INSIDE')
else:
    print('OUTSIDE')
    

# 099
import sys

# 深さ優先探索を行う関数
def dfs(pos, g, visited, dp):
    visited[pos] = True
    dp[pos] = 1
    for i in g[pos]:
        if visited[i] == False:
            dfs(i, g, visited, dp)
            dp[pos] += dp[i]

sys.setrecursionlimit(120000)

n = int(input())
a = [None] * (n - 1)
b = [None] * (n - 1)
for i in range(n - 1):
    a[i], b[i] = map(int, input().split())

g = [list() for i in range(n + 1)]
for i in range(n - 1):
    g[a[i]].append(b[i])
    g[b[i]].append(a[i])

# 深さ優先探索(DFS)を使った動的計画法
visited = [False] * (n + 1)
dp = [None] * (n + 1)
dfs(1, g, visited, dp)

ans = 0
for i in range(2, n + 1):
    ans += dp[i] * (n - dp[i])
print(ans)