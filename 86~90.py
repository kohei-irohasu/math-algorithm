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
