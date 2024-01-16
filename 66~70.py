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