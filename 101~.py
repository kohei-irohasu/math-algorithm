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
    

# 102
# ncrのmodｐはリュカの定理を覚えて
# 使えるようになろうということ
# リュカの定理でncr mod3を求める
# 商と余りの桁ごとの二項係数の積を割った余りと
# ncr mod 3は同じ値になる
def ncr(n, r):
    if n < 3 and r < 3:
        a = [
            [1, 0, 0],
            [1, 1, 0],
            [1, 2, 1]
        ]
        return a[n][r]
    return ncr(n // 3, r // 3) * ncr(n % 3, r % 3) % 3

n = int(input())
c = input()
ans = 0
for i in range(n):
    code = 'BWR'.find(c[i])
    ans += code * ncr(n - 1, i)
    ans %= 3

if n % 2 == 0:
    ans *= - 1 

print('BWR'[ans])