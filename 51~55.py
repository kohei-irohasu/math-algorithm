# 051
# 解１
def modpow(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        if (b & (1 << i)) != 0:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans

def division(a, b, m):
    return (a * modpow(b, m - 2, m)) % m

MOD = 1000000007
x, y = map(int, input().split())

bunshi, bunbo = 1, 1
for i in range(1, x + y + 1):
    bunshi = (bunshi * i) % MOD
for i in range(1, x + 1):
    bunbo = (bunbo * i) % MOD
for i in range(1, y + 1):
    bunbo = (bunbo * i) % MOD

print(division(bunshi, bunbo, MOD))

# 解２
# 階乗の値を先に計算しておく。
# 何度も二項係数を計算する場合に有効。
def modpow(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        if (b & (1 << i)) != 0:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans

def division(a, b, m):
    return (a * modpow(b, m - 2, m)) % m

def ncr(n, r):
    global fact, MOD
    return division(fact[n], fact[r] * fact[n - r] % MOD, MOD)

MOD = 1000000007
LIMIT = 200000

fact = [None] * (LIMIT + 1)
fact[0] = 1
for i in range(1, LIMIT + 1):
    fact[i] = fact[i - 1] * i % MOD

x, y = map(int, input().split())
print(ncr(x + y, y))


# 052
def modpow(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        if (b & (1 << i)) != 0:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans

def division(a, b, m):
    return (a * modpow(b, m - 2, m)) % m

x, y = map(int, input().split())
mod = 1000000007

if (2 * y - x) < 0 or (2 * x - y) < 0:
    print(0)
elif (2 * y - x) % 3 != 0 or (2 * x - y) % 3 != 0:
    print(0)
else:
    bunshi, bunbo = 1, 1
    a = (2 * y - x) // 3
    b = (2 * x - y) // 3
    
    for i in range(1, a + b + 1):
        bunshi = (bunshi * i) % mod 
    for i in range(1, a + 1):
        bunbo = (bunbo * i) % mod
    for i in range(1, b + 1):
        bunbo = (bunbo * i) % mod
    print(division(bunshi, bunbo, mod))