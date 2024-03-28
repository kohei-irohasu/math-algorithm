# 031
n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)

dp[0] = 0
dp[1] = a[0]
for i in range(2, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + a[i - 1])

print(dp[n])


# 032
n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# 二分探索
    # a[mid] != xのとき、midは探索範囲から外してよい
    # よって、right = mid - 1, left = mid + 1とする
    # また、xが探索範囲にないとき、right = midにようにしていると
    # 無限ループに陥る可能性がある。
ans = 'No'
left, right = 0, n - 1
while left <= right:
    mid = (left + right) // 2
    if a[mid] == x:
        ans = 'Yes'
        break
    if a[mid] > x:
        right = mid - 1
    if a[mid] < x:
        left = mid + 1

print(ans)


# 033
# math.sqrtは与えられた引数の平方根を求める
import math

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

# ベクトルの成分
BAx, BAy = ax - bx, ay - by
BCx, BCy = cx - bx, cy - by
CAx, CAy = ax - cx, ay - cy
CBx, CBy = bx - cx, by - cy

# 点の位置で場合分け
# pattern1: <ABCが鈍角 => ABが最短
# pattern2: <ABCが鋭角 => 点Aと線分BCの高さが最短
# pattern3: <ACBが鈍角 => ACが最短
pattern = 2
if BAx * BCx + BAy * BCy < 0:
    pattern = 1
if CAx * CBx + CAy * CBy < 0:
    pattern = 3
    
# 点と直線の距離を求める
if pattern == 1:
    ans = math.sqrt(BAx ** 2 + BAy ** 2)
if pattern == 3:
    ans = math.sqrt(CAx ** 2 + CAy ** 2)
if pattern == 2:
    s = abs(BAx * BCy - BAy * BCx) # 面積 = 外積
    bc = math.sqrt(BCx ** 2 + BCy ** 2)
    ans = s / bc
    
print("%.7f" % ans)


# 034
n = int(input())
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]
for i in range(n):
    x[i], y[i] = map(int, input().split())
    
# 全探索
ans = 10 ** 7
for i in range(n):
    for j in range(i + 1, n):
        dist = (((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5)
        ans = min(ans, dist)

print("%.10f" % ans)


# 035
x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

d = ((x1 - x2)**2 + (y1 - y2)** 2)**0.5

if d < abs(r1 - r2):
    print(1)
elif d == abs(r1 - r2):
    print(2)
elif d < r1 + r2:
    print(3)
elif d == r1 + r2:
    print(4)
else:
    print(5)