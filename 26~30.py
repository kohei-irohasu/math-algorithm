# 026
# 今求めたいのはコンプリートするのに必要な金額
# だけど、1回 = 1ドルなので、回数を求めると考えても問題ない
# よって回数の期待値を求める。回数の期待値はどんな確率で何回行うか？
# 期待値の線形性より、
# 0 -> 1, 1 -> 2, ..., n - 1 -> nにかかるそれぞれの回数の期待値を
# すべて足したもの。
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += 1 / i

ans *= n
print("%.7f" % (ans))


# 027
def MergeSort(A):
    # 長さが１だったら、何もしない
    if len(A) == 1:
        return A
    
    # 2つに分割した後、小さい配列をソート
    m = len(A) // 2
    A_Dash = MergeSort(A[0:m])
    B_Dash = MergeSort(A[m:len(A)])
    
    # この時点で以下の２つの配列がソートされている
    # 列A'に相当するもの(A_Dash[0], A_Dash[1]...)
    # 列B'に相当するもの(B_Dash[0], B_Dash[1]...)
    # 以下がMerge操作
    c1 = 0 # A'のインデックス
    c2 = 0 # B'のインデックス
    C = []
    while(c1 < len(A_Dash) or c2 < len(B_Dash)):
        if c1 == len(A_Dash):
            # A'が空の場合
            C.append(B_Dash[c2])
            c2 += 1
        elif c2 == len(B_Dash):
            # B'が空の場合
            C.append(A_Dash[c1])
            c1 += 1
        else:
            if A_Dash[c1] <= B_Dash[c2]:
                C.append(A_Dash[c1])
                c1 += 1
            else:
                C.append(B_Dash[c2])
                c2 += 1
    
    return C

N = int(input())
A = list(map(int, input().split()))

ans = MergeSort(A)
print(*ans)


# 028
n = int(input())
h = list(map(int, input().split()))

# 動的計画法    
dp = [None] * n
dp[0] = 0
for i in range(1, n):
    if i == 1:
        dp[i] = abs(h[i - 1] - h[i])
    if i >= 2:
        v1 = dp[i - 1] + abs(h[i - 1] - h[i])
        v2 = dp[i - 2] + abs(h[i - 2] - h[i])
        dp[i] = min(v1, v2)

print(dp[n - 1])


# 029
n = int(input())

dp = [0] * (n + 1)
for i in range(n + 1):
    if i <= 1:
        dp[i] = 1
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])


# 030
N, W = map(int, input().split())
w = [0] * N
v = [0] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())

# 配列の初期化
# 価値の総和を求めたいので、初期値は0
INF = 10 ** 18
dp = [[0] * (W + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, W + 1):
    dp[0][i] = -INF

# 動的計画法
# w,vは0インデックス
for i in range(1, N + 1):
    for j in range(0, W + 1):
        if j < w[i - 1]:  # w[i - 1]はとるか取らないか考えてる、現在の品物
            dp[i][j] = dp[i - 1][j] # 取れないから総和は変わらない
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i -1])

ans = max(dp[N])
print(ans)