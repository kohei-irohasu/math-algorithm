# 086
n = int(input())
s = input()
state = 0
for i in s:
    if i == "(":
        state += 1
    else:
        state -= 1
    
    if state < 0:
        print("No")
        break
else:
    if state == 0:
        print("Yes")
    else:
        print("No")


# 087
n = int(input())
mod = 1000000007

ans = ((n * (n + 1) // 2) ** 2) % mod
print(ans)


# 088
a, b, c = map(int, input().split())

mod = 998244353
a_sum = a * (a + 1) // 2
b_sum = b * (b + 1) // 2
c_sum = c * (c + 1) // 2

ans = (a_sum * b_sum * c_sum) % mod
print(ans)


# 089
import sys

a, b, c = map(int, input().split())

if c == 1:
    print('No')
    sys.exit()

v = 1
for i in range(b):
    v *= c
    if a < v:
        print('Yes')
        sys.exit()

print('No')


# 090
# 整数mの各桁の積を返す関数
def product(m):
    if m == 0:
        return 0
    ans = 1
    while m >= 1:
        ans *= (m % 10)
        m //= 10
    return ans

# 各桁の積の候補の集合を返す関数
# digitは現在の桁数
def func(digit, m):
    if digit == 11:
        return {product(m)}
    min_value = m % 10
    ret = set()
    for i in range(min_value, 10):
        r = func(digit + 1, m * 10 + i)
        for j in r:
            ret.add(j)
    return ret

n, b = map(int, input().split())

# 各桁の候補の積を列挙
fm_cand = func(0, 0)

ans = 0
for fm in fm_cand:
    m = fm + b
    prod_m = product(m)
    if m - prod_m == b and m <= n:
        ans += 1

print(ans)