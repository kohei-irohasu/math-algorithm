# 071
# x + yが最大となりうるのは交点の場合。
# 全ての交点を求め、その中のすべての条件式を満たすものを求め、
# その中で。X + yが最大なものを選ぶ。
n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
c = [0 for i in range(n)]
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())
    
# 交点を全探索
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] * b[j] == a[j] * b[i]:
            continue
        # 交点の座標
        px = (c[i] * b[j] - c[j] * b[i]) / (a[i] * b[j] - a[j] * b[i])
        py = (c[i] * a[j] - c[j] * a[i]) / (b[i] * a[j] - b[j] * a[i])
        
        # 条件式をすべて満たすか
        ret = True
        for k in range(n):
            if a[k] * px + b[k] * py > c[k]:
                ret = False
        if ret == True:
            ans = max(ans, px + py)

print("%.12f" % ans)


# 072
# 答えは最大でもb(2 * 10 **5)なので、全探索の方針。
# 最大公約数として持つには、aからbまでに約数として２個以上持つ必要がある。
# aからbまでなので、階差の視点を使う。
def div_num(a, b, t):
    cl = (a - 1) // t
    cr = b // t
    if cr - cl >= 2:
        return True
    else:
        return False

a, b = map(int, input().split())
for i in range(1, b + 1):
    if div_num(a, b, i):
        ans = i
        
print(ans)


# 073
