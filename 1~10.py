# 001
N = int(input())
print(N + 5)


# 002
A = list(map(int, input().split()))
print(A[0] + A[1] + A[2])


# 003
N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in A:
    ans += i

print(ans)


# 004
A1, A2, A3 = map(int, input().split())
print(A1 * A2 * A3)


# 005
N = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    ans += i
print(ans % 100)


# 006
N = int(input())
print(2 * N + 3)


# 007
N, X, Y = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    if i % X == 0 or i % Y == 0:
        ans +=1

print(ans)


# 008
N, S = map(int, input().split())
cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i + j <= S:
            cnt += 1

print(cnt)


# 009 動的計画法Version
# 入力
N, S = map(int, input().split())
A = list(map(int, input().split()))

# 配列の初期化
dp = [ [  None ] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(1, S + 1):
    dp[0][i] = False

# 動的計画法
for i in range(1, N + 1):
    for j in range(0, S + 1):
        if j < A[i - 1]: # カードiを選べない
            dp[i][j] = dp[i - 1][j]
        else:
            # カードiを選ぶ、選ばないの両方の選択肢がある
            if (dp[i - 1][j] == True or dp[i - 1][j - A[i - 1]] == True):
                dp[i][j] = True
            else:
                dp[i][j] = False

# 答えを出力
if dp[N][S] == True:
    print('Yes')
else:
    print('No')   
    

# 010
N = int(input())

ans = 1
for i in range(1, N + 1):
    ans *= i
print(ans)