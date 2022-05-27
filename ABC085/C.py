# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import time 
start=time.time()


"""
自分で書いたコード(3重ループで効率が悪い)
"""
# n, y = map(int, input().split(" ")) 
# # print('n:' ,n, ' y:', y, sep=' ')
# y = int(y/1000)

# for i in range(n+1):
#     for j in range(n+1):
#         for k  in range(n+1):
#             if (i+j+k)==n:
#                 if (10*i + 5*j + 1*k)==y:
#                     print(i, j, k, sep=' ')
#                     # print(time.time()-start)
#                     exit()

# print("-1 -1 -1")



"""
https://qiita.com/Gattaca/items/a4f0a9a3ed89b711b706
"""
n, y = list(map(int, input().split()))
a = b = c = 0

yen_a = 10000
yen_b = 5000
yen_c = 1000

target = y - yen_c * n
coef_a = yen_a - yen_c
coef_b = yen_b - yen_c
a = int(target / coef_a)

if a > n or target < 0:
    a = b = c = -1
else:
    while a >= 0:
        if coef_a * a + coef_b * b == target and n-a-b >= 0:
            c = n - a - b
            break
        elif coef_a * a + coef_b * b > target:
            a -= 1
        else:
            b += 1
    if a == -1:
        b = c = -1

print(a, b, c)



"""
https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2018/0107_abc085
O(N^2)
"""
# 擬似コード

for x in 0 .. N:
    for y in 0 .. N-x:
        if 10000 * x + 5000 * y + 1000 * (N-x-y) == Y:
            # 発見！
            
# ループ終了まで発見できない場合、NとYが不可能な組み合わせである



"""
O(N)
"""
def solve(n, y):
    tmp1000 = n * 1000
    if tmp1000 > y:
        return -1, -1, -1
    diff = y - tmp1000
    for y in range(diff // 4000 + 1):
        tmp5000 = y * 4000
        if diff - tmp5000 < 0:
            break
        if (diff - tmp5000) % 9000 == 0:
            x = (diff - tmp5000) // 9000
            if x >= 0 and x + y <= n:
                return x, y, n - x - y
    return -1, -1, -1

print(*solve(*map(int, input().split())))




"""
実行速度を表示
"""
print(time.time()-start)