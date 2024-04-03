# 041
t = int(input())
n = int(input())
b = [0] * (t + 1)  # t時退勤する人がいるかもしれないので
for i in range(n):
    l, r = map(int, input().split())
    b[l] += 1
    b[r] -= 1

ans = b[0]
print(ans)
for i in range(1, t):    # t-1 + 0.5までだから 
    ans += b[i] 
    print(ans)
    
    
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

# 足された回数を考える
# 1 ~ n までのそれぞれは何回掛けられて、
# 足されているかを考える。
# 例えば3は、
# f(3) => 1 * 3 
# f(6) => 1 * 6
# f(9) => 1 * 9
#  ....で3でくくると1~(n//3)の和
n = int(input())
ans = 0

for i in range(1, n + 1):
    d = n // i
    ans += i * (d * (d + 1) // 2)
    
print(ans)


# 043 DFS
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

# 隣接リストの作成
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# DFSの初期化と関数化
def dfs(start):
    visited = [False] * (n + 1)
    stack = [start] # スタックで管理する
    visited[start] = True
    
    while stack:
        pos = stack.pop()
        for nex in g[pos]:
            if not visited[nex]:
                visited[nex] = True
                stack.append(nex)
    return visited

# 連結かどうかの判定
visited = dfs(1)
if all(visited[i] for i in range(1, n + 1)):
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