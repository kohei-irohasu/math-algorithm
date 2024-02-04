# 081
n = int(input())
ans = 0

ans += n // 10000
n %= 10000

ans += n // 5000
n %= 5000

ans += n // 1000
n %= 1000

print(ans)


# 082
n = int(input())
m = []
for i in range(n):
    a, b = map(int, input().split())
    m.append([b, a])
    
m.sort()
cur = 0
ans = 0
for i in range(n):
    if m[i][1] >= cur:
        cur = m[i][0]
        ans += 1

print(ans)


# 083
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
ans = 0
for i in range(n):
    ans += abs(a[i] - b[i])

print(ans)


# 084
a, b, c = map(int, input().split())
if c - a - b > 0:
    if 4 * a * b < (c - a - b) ** 2:
        print('Yes')
    else:
        print('No')
else:
    print('No')


# 085
n, x, y = map(int, input().split())

if x > n * 4 or y > n ** 4:
    print('No')
else:
    d = []
    for i in range(1, n + 1):
        if y % i == 0:
            d.append(i)
    
    divcnt = len(d)
    flag = False
    for i in range(0, divcnt):
        for j in range(i, divcnt):
            for k in range(j, divcnt):
                for l in range(k, divcnt):
                    if d[i] + d[j] + d[k] + d[l] == x and d[i] * d[j] * d[k] * d[l] == y:
                        flag = True
                        
    print('Yes' if flag else 'No')