# 041
t = int(input())
n = int(input())
l = [0] * n
r = [0] * n
for i in range(n):
    l[i], r[i] = map(int, input().split())

# 階差を計算
b = [0] * (t + 1)  # t時退勤する人がいるかもしれないので
for i in range(n):
    b[l[i]] += 1
    b[r[i]] -= 1

# 累積和の計算
a = [0] * (t)   # t-1 + 0.5までだから 
a[0] = b[0]
for i in range(1, t):
    a[i] = a[i - 1] + b[i]
    
for i in range(t):
    print(a[i])
    
    
# 042
# エラトステネスの篩version
n = int(input())
f = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, (n // i) + 1):
        f[i * j] += 1

ans = 0
for i in range(1, n + 1):
    ans += i * f[i]

print(ans)

# 足された回数
# i * dの和を考えて、そのdについて、d回分
# 1からnまでのそれぞれの数がかけられているので
# i * (1からdまでの総和)を1からnまで足していく。
n = int(input())
ans = 0

for i in range(1, n+1):
	d = (n // i)
	ans += i * (d * (d + 1) // 2)

print(ans)

