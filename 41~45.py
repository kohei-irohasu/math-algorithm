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


# 044 BFS
from collections import deque

def bfs(start):
    queue = deque([start])
    distance[start] = 0
    while queue:
        node = queue.popleft()
        for next_node in g[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                queue.append(next_node)

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

distance = [-1] * (n + 1)
bfs(1)

print('\n'.join(map(str, distance[1:])))  #\nで文字列を結合


# 045
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ans = 0
for i in range(1, n + 1):
    cnt = 0
    for j in g[i]:
        if j < i:
            cnt += 1
    if cnt == 1:
        ans += 1

print(ans)