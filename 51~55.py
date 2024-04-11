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
    return division(fact[n], fact[r] * fact[n - r] % MOD, MOD)

x, y = map(int, input().split())
MOD = 1000000007
n = x + y

fact =[0] * (n + 1)
fact[0] = 1
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % MOD

ans = ncr(n, y)
print(ans)


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
    

# 053
def modpow(a, b, m):
    p = a
    ans = 1
    for i in range(60):
        if (b &(1 << i)) != 0:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans

def division(a, b, m):
    return (a * modpow(b, m - 2, m)) % m

n = int(input())
mod = 1000000007
v = modpow(4, n + 1, mod) - 1
ans = division(v, 3, mod)
print(ans)


# 054
from copy import deepcopy
mod = 1000000000

# 行列の積を返す関数
def multiply(a, b):
    global mod
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= mod
    return c

# aのn乗を返す関数
def power(a, n):
    p = deepcopy(a)
    q = [[0, 0], [0, 0]]
    flag = False
    for i in range(60):
        if (n & (1 << i)) != 0:
            if flag == False:
                q = deepcopy(p)
                flag = True
            else:
                q = deepcopy(multiply(q, p))
        p = deepcopy(multiply(p, p))
    return q

n = int(input())
a = [[1, 1], [1, 0]]
b = power(a, n - 1)

ans = (b[1][0] + b[1][1]) % mod
print(ans)


# 055
from copy import deepcopy
mod = 1000000007

# 行列の積を返す関数
def multiply(a, b):
    global mod
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += (a[i][k] * b[k][j]) % mod
    return c

# aのn乗を返す関数
def power(a, n):
    p = a
    q = [[0, 0], [0, 0]]
    flag = False
    for i in range(60):
        if (n & (1 << i)) != 0:
            if flag == False:
                q = deepcopy(p)
                flag = True
            else:
                q = multiply(q, p)
        p = multiply(p, p)
    return q

n = int(input())
a = [[2, 1], [1, 0]]
b = power(a, n - 1)

ans = (b[1][0] + b[1][1]) % mod
print(ans)