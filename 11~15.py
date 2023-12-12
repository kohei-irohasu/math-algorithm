# 011
def isPrime(num):
    LIMIT = int(num ** 0.5)
    for i in range(2, LIMIT + 1):
        if num % i == 0:
            return False
    return True

N = int(input())
for i in range(2, N + 1):
    if isPrime(i):
        print(i, end=" ")


# 012
def isPrime(num):
    LIMIT = int(num ** 0.5)
    for i in range(2, LIMIT + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
print('Yes' if isPrime(n) else 'No')


# 013
n = int(input())

LIMIT = int(n ** 0.5)
ans = set()
for i in range(1, LIMIT + 1):
    if n % i == 0:
        ans.add(i)
        ans.add(n // i)

for i in ans:
    print(i)


# 014
n = int(input())
ans = []
LIMIT = int(n ** 0.5)
for i in range(2, LIMIT + 1):
    while n % i == 0:
        n //= i
        ans.append(i)

if n > 2:
    ans.append(int(n))

print(*ans)


# 015
# 地道version
a, b = map(int, input().split())
if a > b:
    a, b = b, a

a_div = []
LIMIT = int(a ** 0.5)
for i in range(2, LIMIT + 1):
    while a % i == 0:
        a //= i
        a_div.append(i)
if a > 1:
    a_div.append(a)

ans = 1
for i in a_div:
    if b % i == 0:
        ans *= i
        b //= i

print(ans)


# 015
# エラトステネスの篩version
a, b = map(int, input().split())
if a > b:
    a, b = b, a
    
while b % a != 0:
    a, b = b % a, a

print(a)


# 015
# 模範解答例(TLE)
def gcd(a, b):
    ans = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans = i
    return ans

a, b = map(int, input().split())
print(gcd(a, b))