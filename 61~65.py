# 061
n = int(input())

flag = False
for i in range(1, 60):
    if n == (2 ** i) - 1:
        flag = True

print('Second' if flag else 'First')


# 062
def find_kth_town(n, k, a):
    first = [-1] * (n + 1)
    second = [-1] * (n + 1)
    
    cnt = 0
    cur = 1
    l = list()
    
    while True:
        if first[cur] == -1:
            first[cur] = cnt
            l.append(cur)
        elif second[cur] == -1:
            second[cur] = cnt
            index = (k - first[cur]) % (second[cur] - first[cur])
            return l[first[cur] + index]
        
        # ループしないとき
        if cnt == k:
            return cur
        
        cur = a[cur - 1]
        cnt += 1

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = find_kth_town(n, k, a)
print(result)

# 別解
import sys

n, k = map(int, input().split())
a = list(map(int, input().split()))

# 配列の初期化
first = [-1 for _ in range(n + 1)]
second = [-1 for _ in range(n + 1)]

# 答えを求める
# curは現在の町
cnt = 0
cur = 1
while True:
    if first[cur] == -1:
        first[cur] = cnt
    elif second[cur] == -1:
        second[cur] = cnt
    
    # k回後の移動で町curにいるか判定
    if cnt == k:
        print(cur)
        sys.exit()
    elif second[cur] != -1 and (k - first[cur]) % (second[cur] - first[cur]) == 0:
        print(cur)
        sys.exit()
    
    cur = a[cur - 1]
    cnt += 1
    

# 063
n = int(input())
print('Yes' if n % 2 == 0 else 'No')


# 064
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = 0
for i in a:
    s += i

if s > k:
    print('No')
elif (s - k) % 2 == 0:
    print('Yes')
else:
    print('No')
    
    
# 065
h, w = map(int, input().split())
if h == 1 or w == 1:
    print(1)
else:
    evan = w // 2
    add = w - evan
    enum = h // 2
    anum = h - enum
    ans = evan * enum + add * anum
    print(ans)
    
# 別解、スマート
h, w = map(int, input().split())
if h == 1 or w == 1:
    print(1)
else:
    print((h * w + 1) // 2)