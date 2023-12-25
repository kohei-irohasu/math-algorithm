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


# 043 DFS
n, m = map(int, input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())
    
# 隣接リストの作成
g = [list() for _ in range(n + 1)]
for i in range(m):
    g[a[i]].append(b[i])
    g[b[i]].append(a[i])

# 深さ優先探索の初期化
visited = [False] * (n + 1)
s = list()  # スタックを定義
visited[1] = True
s.append(1)

# 深さ優先探索
while len(s) >= 1:
    pos = s.pop()
    for nex in g[pos]:
        if visited[nex] == False:
            visited[nex] = True
            s.append(nex)

# 連結か同課の判定
ans = True
for i in range(1, n + 1):
    if visited[i] == False:
        ans = False
if ans:
    print('The graph is connected.')
else:
    print('The graph is not connected.')


# 044
import queue
n, m = map(int, input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())

g = [list() for _ in range(n + 1)]
for i in range(m):
    g[a[i]].append(b[i])
    g[b[i]].append(a[i])

# 幅優先探索の初期化
dist = [-1] * (n + 1)
q = queue.Queue()
dist[1] = 0
q.put(1)

# 幅優先探索
while not q.empty():
    pos = q.get()
    for nex in g[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            q.put(nex)

for i in range(1, n + 1):
    print(dist[i])


# 045
n, m = map(int, input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())

# 隣接リストの作成
g = [list() for _ in range(n + 1)]
for i in range(m):
    g[a[i]].append(b[i])
    g[b[i]].append(a[i])

ans = 0
for i in range(1, n + 1):
    cnt = 0
    for j in g[i]:
        if j < i:
            cnt += 1
    if cnt == 1:
        ans += 1

print(ans)