# 046 DFS
import queue

h, w = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [input() for _ in range(h)]
start = (sy - 1) * w + (sx - 1)
goal = (gy - 1) * w + (gx - 1)

# 隣接リストの作成
g = [list() for i in range(h * w)]

# 横方向の辺をグラフに追加
for i in range(h):
    for j in range(w - 1):
        if c[i][j] == '.' and c[i][j + 1] == '.':
            idx1 = i * w + j
            idx2 = i * w + (j + 1)
            g[idx1].append(idx2)
            g[idx2].append(idx1)

# 縦方向の辺をグラフに追加
for i in range(h - 1):
    for j in range(w):
        if c[i][j] == '.' and c[i + 1][j] == '.':
            idx1 = i * w + j
            idx2 = (i + 1) * w + j
            g[idx1].append(idx2)
            g[idx2].append(idx1)

# 幅優先探索の初期化
dist = [-1] * (h * w)
q = queue.Queue()
dist[start] = 0
q.put(start)

# 幅優先探索
while not q.empty():
    pos = q.get()
    for nex in g[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            q.put(nex)

print(dist[goal])


# 047
# 連結を前提としないなら、すべての頂点について
# 深さ優先探索を行わなければならない。
def dfs(start, g, color):
    s = [start]
    color[start] = 0
    
    while s:
        pos = s.pop()
        for nex in g[pos]:
            if color[nex] == -1:
                color[nex] = 1 - color[pos]
                s.append(nex)

n, m = map(int, input().split())
a = [None] * m
b = [None] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())

g = [[] for _ in range(n + 1)]
for i in range(m):
    g[a[i]].append(b[i])
    g[b[i]].append(a[i])

color = [-1] * (n + 1)

for i in range(1, n + 1):
    if color[i] == -1:
        dfs(i, g, color)
    
# 二部グラフかどうか
ans = all(color[a[i]] != color[b[i]] for i in range(m))
print('Yes' if ans else 'No') 


# 048 ダイクストラ法
# kの倍数＝ kで割り切れる
import heapq
k = int(input())

# 隣接リストの作成 → グラフの辺を追加
g = [list() for i in range(k)]
for i in range(k):
    for j in range(10):
        if i == 0 and j == 0:
            continue
        g[i].append(((i * 10 + j) % k, j))

# ダイクストラ法: 配列の初期化
dist = [10 ** 10] * k
used = [False] * k
q = list()
heapq.heappush(q, (0, 0))  #d[0] = 0としない

# ダイクストラ法: 優先度付きキューの更新
while len(q) >= 1:
    pos = heapq.heappop(q)[1]
    if used[pos] == True:
        continue
    used[pos] = True
    for i in g[pos]:
        to = i[0]
        cost = dist[pos] + i[1]
        if pos == 0:
            cost = i[1]
        if dist[to] > cost:
            dist[to] = cost
            heapq.heappush(q, (dist[to], to))

print(dist[0])


# 049
# fibonacci、効率的な余りの計算
n = int(input())

a = [None] * (n + 1)
a[1], a[2] = 1, 1
for i in range(3, n + 1):
    a[i] = (a[i - 1] + a[i - 2]) % 1000000007
print(a[n] % 1000000007)


# 050
def modpow(a, b, m):
    p = a
    ans = 1
    for i in range(30):
        if (b & (1 << i)) != 0:
            ans = (ans * p) % m
        p = (p * p) % m
    return ans

MOD = 1000000007
a, b = map(int, input().split())
print(modpow(a, b, MOD))