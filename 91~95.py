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