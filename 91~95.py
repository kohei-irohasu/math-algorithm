# 091
n, x = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            if i + j + k == x:
                ans += 1
    
print(ans)


#092
n = int(input())
def divided(n):
    div = []
    LIMIT = int(n ** 0.5) + 1
    for i in range(1, LIMIT):
        if n % i == 0:
            div.append((i, n// i))    
    return div

ans = 10 ** 12
div = divided(n)
for i in div:
    a, b = i
    ans = min(ans, a + b)

print(ans * 2)


# 093
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())

lcm = a // gcd(a, b) * b
if lcm > 10 ** 18:
    print('Large')
else:
    print(lcm)


# 094
n = int(input())
b = list(map(int, input().split()))

ans = b[0] + b[n - 2]
for i in range(1, n - 1):
    ans += min(b[i - 1], b[i])

print(ans)


# 095
n = int(input())
a = [0] * (n + 1)
b = [0] * (n + 1)
    
for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        a[i + 1] += p
    else:
        b[i + 1] += p
    
    a[i + 1] += a[i]
    b[i + 1] += b[i]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    A = a[r] - a[l - 1]
    B = b[r] - b[l - 1]
    print(A, B)
    

# 095模範解答
n = int(input())
c = [None] * (n + 1)
p = [None] * (n + 1)
for i in range(1, n + 1):
    c[i], p[i] = map(int, input().split())

# 累積和
s1 = [None] * (n + 1)
s1[0] = 0
for i in range(1, n + 1):
    s1[i] = s1[i - 1] + (p[i] if c[i] == 1 else 0)
s2 = [None] * (n + 1)
s2[0] = 0
for i in range(1, n + 1):
    s2[i] = s2[i - 1] + (p[i] if c[i] == 2 else 0)

# 質問に答える
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(s1[r] - s1[l - 1], s2[r] - s2[l - 1])