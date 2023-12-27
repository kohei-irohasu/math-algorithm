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