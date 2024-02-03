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