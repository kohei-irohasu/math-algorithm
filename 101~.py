# 101
# 繰り返し二乗法(a ** b % m)
def modpow(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        if (b & (1 << i)) != 0:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans

# a / b % mを返す
def division(a, b, m):
    return (a * modpow(b, m - 2, m)) % m

# ncrを返す関数
def ncr(n, r):
    global fact, mod
    return division(fact[n], fact[r] * fact[n - r] % mod, mod)

mod = 1000000007
LIMIT = 100000

# 配列factの初期化(fact[i]はiの階乗をmodで割った余り)
fact = [None] * (LIMIT + 1)
fact[0] = 1
for i in range(1, LIMIT + 1):
    fact[i] = fact[i - 1] * i % mod

n = int(input())
for i in range(1, n + 1):
    ans = 0
    for j in range(1, (n - 1) // i + 2):
        ans += ncr(n - (i - 1) * (j - 1), j)
        ans %= mod
    print(ans)