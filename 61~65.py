# 061
n = int(input())

flag = False
for i in range(1, 60):
    if n == (2 ** i) - 1:
        flag = True

print('Second' if flag else 'First')