# 021
def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

def ncr(n, r):
    ans = fact(n) // (fact(r) * fact(n-r))
    return ans

n, r = map(int, input().split())
print(ncr(n, r))


# 022
n = int(input())
a = list(map(int, input().split()))

cnt = [0 for i in range(100000)]
for i in range(n):
    cnt[a[i]] += 1

ans = 0
for i in range(1, 50000):
    ans += cnt[i] * cnt[100000 - i]
ans += cnt[50000] * (cnt[50000] - 1) // 2

print(ans)


# 023
n = int(input())
b = list(map(int, input().split()))
r = list(map(int, input().split()))

total = 0
for x in b:
    total += x
for y in r:
    total += y
print(total / n)


# 024
n = int(input())
ans = 0
for _ in range(n):
    p, q = map(int, input().split())
    ans += q / p

print("%.7f" % (ans))


# 025
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += (a[i] / 3) + (b[i] / 3 * 2)

print("%.6f" % (ans))