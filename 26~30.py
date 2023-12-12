# 026
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += 1 / i

ans *= n
print("%.7f" % (ans))


# 027
def mergeSort(a):
    if len(a) == 1:
        return a
    
    m = len(a) // 2
    a_dash = mergeSort(a[0:m])
    b_dash = mergeSort(a[m:len(a)])
    
    c1 = 0  # a_dashのcに入れた数
    c2 = 0  # b_dashのcに入れた数
    c = []
    while (c1 < len(a_dash) or c2 < len(b_dash)):
        if c1 == len(a_dash):
            # a_dashが空の場合
            c.append(b_dash[c2])
            c2 += 1
        elif c2 == len(b_dash):
            # b_dashが空の場合
            c.append(a_dash[c1])
            c1 += 1
        else:
            if a_dash[c1] <= b_dash[c2]:
                c.append(a_dash[c1])
                c1 += 1
            else:
                c.append(b_dash[c2])
                c2 += 1
    return c

n = int(input())
a = list(map(int, input().split()))

ans = mergeSort(a)
print(*ans)


# 028
n = int(input())
h = list(map(int, input().split()))

# 動的計画法    
dp = [None] * n
dp[0] = 0
for i in range(1, n):
    if i == 1:
        dp[i] = abs(h[i - 1] - h[i])
    if i >= 2:
        v1 = dp[i - 1] + abs(h[i - 1] - h[i])
        v2 = dp[i - 2] + abs(h[i - 2] - h[i])
        dp[i] = min(v1, v2)

print(dp[n - 1])