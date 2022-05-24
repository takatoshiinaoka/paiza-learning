# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
N, M = input_line.split(" ")
N = int(N)
M = int(M)

# print(N) #ゴンドラの数
# print(M) # グループの数

A_i = [0] * N #i 番目のゴンドラに乗車できる人数
B_i = [0] * M #i 番目のグループの人数を表す整数
G_i = [0] * N #i 番目のゴンドラに乗車した人数

# ゴンドラに乗車できる人数をN個分入力
for i in range(N):
    input_line=input()
    A_i[i] = int(input_line)
# print("A_i"+str(A_i))
    
# グループの人数をMグループ分入力
for i in range(M):
    input_line=input()
    B_i[i] = int(input_line)
# print("B_i"+str(B_i))

g=0 #現在乗れるゴンドラの番号
g = int(g)

def chenge_gd(g):
    g += 1
    if g == N:
        g=0
    return g


for i in range(M): # Mグループ回
    while B_i[i] > 0: # グループの人数が0より大きい間
        if B_i[i] <= A_i[g]: # もしグループの全員がゴンドラに乗れるなら(人数<=人数人数制限)
            G_i[g] += B_i[i] #ゴンドラに乗った人をカウント
            B_i[i] -= A_i[g] # 人数-人数制限
        elif B_i[i] > int(A_i[g]): #もしグループ全員がのれないなら(人数>人数制限)
            G_i[g] += A_i[g] #乗った人数をカウント
            B_i[i] -= A_i[g] #人数-人数制限
        g = chenge_gd(g) #次のゴンドラへ
        # print(G_i,end=" ")
        # print(g)

# print(G_i)
for i in G_i:
    print(i)