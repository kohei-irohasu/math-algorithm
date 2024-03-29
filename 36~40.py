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
# ベクトル(ax, ay)と(bx, by)の外積の絶対値を外した値
def cross(ax, ay, bx, by):
    return ax * by - ay * bx

# 入力
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

# crossの値
ans1 = cross(x2 - x1, y2 - y1, x3 - x1, y3 - y1)
ans2 = cross(x2 - x1, y2 - y1, x4 - x1, y4 - y1)
ans3 = cross(x4 - x3, y4 - y3, x1 - x3, y1 - y3)
ans4 = cross(x4 - x3, y4 - y3, x2 - x3, y2 - y3)

# 全て一直線に並んでいる場合
if ans1 == 0 and ans2 == 0 and ans3 == 0 and ans4 == 0:
    a = (x1, y1)
    b = (x2, y2)
    c = (x3, y3)
    d = (x4, y4)
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if max(a, c) <= min(b, d):
        print('Yes')
    else:
        print('No')

# 普通の場合
else:
    isAb = False
    isCd = False
    if ans1 >= 0 and ans2 <= 0:
        isAb = True
    if ans1 <= 0 and ans2 >= 0:
        isAb = True
    if ans3 >= 0 and ans4 <= 0:
        isCd = True
    if ans3 <= 0 and ans4 >= 0:
        isCd = True
        
    if isAb == True and isCd == True:
        print('Yes')
    else:
        print('No')


# 038
# b[0] = 0と置くと実装が楽
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [0 for _ in range(n + 1)]
b[0] = 0
for i in range(n):
    b[i + 1] += b[i] + a[i]

for i in range(q):
    l, r = map(int, input().split())
    print(b[r] - b[l - 1])


# 039
# 求めるのは大小関係のみだから、階差をとって
# 計算量を減らす。
n, q = map(int, input().split())
l = [None] * q
r = [None] * q
x = [None] * q
for i in range(q):
    l[i], r[i], x[i] = map(int, input().split())

# 階差の計算
b = [0] * (n + 2)
for i in range(q):
    b[l[i]] += x[i]
    b[r[i] + 1] -= x[i]

# 答えを計算を出力
ans = ""
for i in range(2, n + 1):
    if b[i] > 0:
        ans += '<'
    if b[i] == 0:
        ans += '='
    if b[i] < 0:
        ans += '>'
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