# 016
def gcd(a, b):
    if a > b:
        a, b = b, a
    
    while b % a != 0:
        a, b = b % a, a
    return a

n = int(input())
a = list(map(int, input().split()))

ans = gcd(a[0], a[1])
for i in range(2, n):
    ans = gcd(ans, a[i])

print(ans)


# 017
# 最大公約数を返す関数
def gcd(a, b):
    if a > b:
        a, b = b, a
    
    while b % a != 0:
        a, b = b % a, a
    return a

# 最小公倍数を返す関数
def lcm(a, b):
    return int(a / gcd(a, b) * b)

# 入力
n = int(input())
a = list(map(int, input().split()))

ans = lcm(a[0], a[1])
for i in range(2, n):
    ans = lcm(ans, a[i])

# 出力
print(ans)


# 018
n = int(input())
A = list(map(int, input().split()))

a, b, c, d = 0, 0, 0, 0
for i in range(n):
    if A[i] == 100:
        a += 1
    elif A[i] == 200:
        b += 1
    elif A[i] == 300:
        c += 1
    else:
        d += 1

print(a * d + b * c)


# 019
n = int(input())
a = list(map(int, input().split()))

colors = [0] * 3
for i in a:
    if i == 1:
        colors[0] += 1
    elif i == 2:
        colors[1] += 1
    else:
        colors[2] += 1

ans = 0
for i in colors:
    ans += i * (i-1) // 2
print(ans)


# 020
n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                for m in range(l+1, n):
                    if a[i] + a[j] + a[k] + a[l] + a[m] == 1000:
                        ans += 1
                        
print(ans)