# 071
# x + yが最大となりうるのは交点の場合。
# 全ての交点を求め、その中のすべての条件式を満たすものを求め、
# その中で。X + yが最大なものを選ぶ。
n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
c = [0 for i in range(n)]
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())
    
# 交点を全探索
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] * b[j] == a[j] * b[i]:
            continue
        # 交点の座標
        px = (c[i] * b[j] - c[j] * b[i]) / (a[i] * b[j] - a[j] * b[i])
        py = (c[i] * a[j] - c[j] * a[i]) / (b[i] * a[j] - b[j] * a[i])
        
        # 条件式をすべて満たすか
        ret = True
        for k in range(n):
            if a[k] * px + b[k] * py > c[k]:
                ret = False
        if ret == True:
            ans = max(ans, px + py)

print("%.12f" % ans)


# 072
# 答えは最大でもb(2 * 10 **5)なので、全探索の方針。
# 最大公約数として持つには、aからbまでに約数として２個以上持つ必要がある。
# aからbまでなので、階差の視点を使う。
def div_num(a, b, t):
    cl = (a - 1) // t
    cr = b // t
    if cr - cl >= 2:
        return True
    else:
        return False

a, b = map(int, input().split())
for i in range(1, b + 1):
    if div_num(a, b, i):
        ans = i
        
print(ans)


# 073
# それぞれの整数が何回最大となるかを考える。
# また、2^nの計算は先に計算して、リストを作り、
# 同じ計算を何度もしないようにして、計算量を減らす。
n = int(input())
a = list(map(int, input().split()))

# 2^iを先に求めておく
mod = 1000000007
power = [0 for _ in range(n)]
power[0] = 1
for i in range(1, n):
    power[i] = (2 * power[i - 1]) % mod
    
ans = 0
for i in range(n):
    ans += a[i] * power[i]
    ans %= mod

print(ans)


# 074
n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += a[i] * (- n + 2 * i + 1)

print(ans)


# 075
# nCrは階乗を先に計算しておく。
# また、割り算はモジュラ逆数を使って、累乗の掛け算にする。
# 累乗の計算を効率的に行うために、繰り返し二乗法を利用する。
def modpow(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        if (b & (1 << i)) != 0:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans 

def division(a, b, m):
    return a * modpow(b, m - 2, m) % m

def ncr(n, r):
    global s, mod
    return division(s[n], s[r] * s[n - r] % mod, mod)

n = int(input())
a = list(map(int, input().split()))
mod = 1000000007

s = [None] * (n + 1)
s[0] = 1
for i in range(1, n + 1):
    s[i] = (s[i - 1] * i) % mod

ans = 0
for i in range(n):
    ans += a[i] * ncr(n - 1, i)
    ans %= mod

print(ans)