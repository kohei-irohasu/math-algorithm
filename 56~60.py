# 056
from copy import deepcopy
mod = 1000000007

# 行列の積を返す関数
def multiply(a, b):
    global mod
    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                c[i][j] += (a[i][k] * b[k][j]) % mod
    return c

# aのn乗を返す関数
def power(a, n):
    p = a
    q = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    flag = False
    for i in range(60):
        if (n & (1 << i)) != 0:
            if flag == False:
                q = deepcopy(p)
                flag = True
            else:
                q = multiply(q, p)
        p = multiply(p, p)
    return q

n = int(input())
a = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
b = power(a, n - 1)

ans = (b[2][0] * 2 + b[2][1] + b[2][2]) % mod
print(ans)


# 058
