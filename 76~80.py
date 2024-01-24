# 076
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

ans = 0
for i in range(n):
    ans += a[i] * (-n + 2 * i + 1)
print(ans)


# 077
n = int(input())
x = [None] * (n)
y = [None] * (n)
for i in range(n):
    x[i], y[i] = map(int, input().split())

x.sort()
y.sort()
    
x_sum = 0
y_sum = 0
for i in range(n):
    x_sum += x[i] * (-n + (2 * i + 1))
    y_sum += y[i] * (-n + (2 * i + 1))
    
print(x_sum + y_sum)


# 078
# 人を頂点として、年齢差を辺としたグラフを考える。
# 幅優先探索をして、その時の最短経路長が年齢。
# 到達できない(条件がない)、distが120以上だったら、120。
import queue

n, m = map(int, input().split())
a = [None] * m
b = [None] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())

# 隣接リストの作成
g = [list() for _ in range(n + 1)]
for i in range(m):
    g[a[i]].append(b[i])
    g[b[i]].append(a[i])

# 幅優先探索の初期化
dist = [-1] *(n + 1)
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
    print(120 if dist[i] >= 120 or dist[i] == -1 else dist[i])


# 079
n = int(input())

ans = n * (n - 1) // 2
print(ans)


# 080