# 066
n, k = map(int, input().split())

yojisho = 0
for a in range(1, n + 1):
    l = max(1, a - (k - 1)) # b, cの下限
    r = min(n, a + (k - 1)) # b, cの上限
    for b in range(l, r + 1):
        for c in range(l, r + 1):
            if abs(b - c) < k:
                yojisho += 1
print(n ** 3 - yojisho)


# 067
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [[None] * w for _ in range(h)]

hs = [0] * h
ws = [0] * w
for i in range(h):
    hs[i] = sum(a[i])

for j in range(w):
    for i in range(h):
        ws[j] += a[i][j]

for i in range(h):
    for j in range(w):
        b[i][j] = hs[i] + ws[j] - a[i][j]

for i in range(h):
    print(*b[i])


# 068
# 最大公約数を返す関数
def gcd(a, b):
    while a >= 1 and b >= 1:
        if a < b:
            b = b % a
        else:
            a = a % b
    if a >= 1:
        return a
    else:
        return b

# 最小公倍数を返す関数
def LCM(a, b):
    return int(a / gcd(a, b)) * b

n, k = map(int, input().split())
v = list(map(int, input().split()))

# ビット全探索
ans = 0
for i in range(1, 1 << k):  # 2^k - 1個の集合
    cnt = 0  # 選んだ数の個数
    lcm = 1  # 最小公倍数
    for j in range(k):  # その集合を選ぶかどうか
        if (i & (1 << j)) != 0:
            cnt += 1
            lcm = LCM(lcm, v[j])
    
    num = n // lcm
    # 集合を偶数個選ぶときは－、奇数個選ぶときは＋
    if cnt % 2 == 1:
        ans += num
    else:
        ans -= num

print(ans)


# 069
# ぎりぎりを考える。
# 答えになりうる値で全探索。
a, b, c, d = map(int, input().split())
print(max(a * c, a * d, b * c, b * d))


# 070
# ギリギリ → 辺上に点がある → ありうる長方形の４点の座標は
# 与えられた点のどれかに合致しなくてはいけない。
# 最適でありうる長方形を全探索し、その中で、点をk点以上含む
# 長方形の最小値を求める。cl < cr, dl < drで計算量を削減。
def check_numpoints(n, x, y, lx, rx, ly, ry):
    cnt = 0
    for i in range(n):
        if lx <= x[i] and x[i] <= rx and ly <= y[i] and y[i] <= ry:
            cnt += 1
            
    return cnt

n, K = map(int, input().split())
x = [None] * n
y = [None] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = 10 ** 19
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                cl, cr, dl, dr = x[i], x[j], y[k], y[l]
                if cl < cr and dl < dr:
                    if check_numpoints(n, x, y, cl, cr, dl, dr) >= K:
                        area = (cr - cl) * (dr - dl)
                        ans = min(ans, area)

print(ans)