# 036
# 余弦定理version
import math

a, b, h, m = map(int, input().split())

angle_h = 30 * h + 0.5 * m
angle_m = 6 * m

degrees = abs(angle_h - angle_m)
radians = math.radians(degrees)
cos = math.cos(radians)
ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * cos)

print("%.9f" % ans)

# 三角関数version
import math

a, b, h, m = map(int, input().split())

# 座標を求める
angle_h = 30 * h + 0.5 * m 
angle_m = 6 * m
hx = a * math.cos(angle_h * math.pi / 180)
hy = a * math.sin(angle_h * math.pi / 180)
mx = b * math.cos(angle_m * math.pi / 180)
my = b * math.sin(angle_m * math.pi / 180)

# 答えを出力
d = (((hx - mx) ** 2 + (hy - my) ** 2) ** 0.5)
print("%.10f" % d)


# 037
# cross関数(ベクトル(ax, ay)と(bx, by)の外積の絶対値を外した値)
def cross(ax, ay, bx, by):
    return ax * by - ay * bx

# 入力
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
dx, dy = map(int, input().split())

# それぞれのcrossを求める
crossBAC = cross(bx - ax, by - ay, cx - ax, cy - ay)
crossBAD = cross(bx - ax, by - ay, dx - ax, dy - ay)
crossDCA = cross(dx - cx, dy - cy, ax - cx, ay - cy)
crossDCB = cross(dx - cx, dy - cy, bx - cx, by - cy)

# 一直線上に並んでいる状態
if crossBAC == 0 and crossBAD == 0 and crossDCA == 0 and crossDCB == 0:
    a = (ax, ay)
    b = (bx, by)
    c = (cx, cy)
    d = (dx, dy)
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if max(a, c) <= min(b, d):
        print('Yes')
    else:
        print('No')

#普通の場合
else:
    # isAB => 線分ABは点C, Dを分けているか？
    isAB = False
    isCD = False

    if crossBAC >= 0 and crossBAD <= 0:
        isAB = True
    if crossBAC <= 0 and crossBAD >= 0:
        isAB = True
    if crossDCA >= 0 and crossDCB <= 0:
        isCD = True
    if crossDCA <= 0 and crossDCB >= 0:
        isCD = True
    
    if isAB == True and isCD == True:
        print('Yes')
    else:
        print('No')


# 038
# b[0] = 0と置くと実装が楽
n, q = map(int, input().split())
a = list(map(int, input().split()))

b = [0 for _ in range(n + 1)]
for i in range(n):
    b[i + 1] = b[i] + a[i]

for i in range(q):
    l, r = map(int, input().split())
    print(b[r] - b[l - 1])


# 039
# 求めるのは大小関係のみだから、階差をとって
# 計算量を減らす。
n, q = map(int, input().split())

# 階差の計算
b = [0] * (n + 2)   # 1~n+1までで0インデックスだから
for i in range(q):
    l, r, x = map(int, input().split())
    b[l] += x
    b[r + 1] -= x

ans = ""
for i in range(2, n + 1):  # bi = i - (i - 1)
    if b[i] > 0:
        ans += "<"
    if b[i] == 0:
        ans += "="
    if b[i] < 0:
        ans += ">"
print(ans)


# 040
# 階差をとるときはインデックスに注意。
# 0なのか、1なのか注意する
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = [0] * m
for i in range(m):
    b[i] = int(input())

s = [0] * n
for i in range(1, n):
    s[i] = s[i - 1] + a[i - 1]

ans = 0
for i in range(m - 1):
     ans += abs(s[b[i] - 1] - s[b[i + 1] - 1])

print(ans)