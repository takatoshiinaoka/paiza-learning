# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_line = input()
N = int(input_line)
input_line = input()
x_R, x_G, x_B= input_line.split(" ")
x_R = int(x_R) #カブトムシ赤
x_G = int(x_G) #カブトムシ緑
x_B = int(x_B) #カブトムシ青

t = [''] * N # 右か左か
c = [''] * N # 色

for i in range(N):
    input_line = input()
    t[i], c[i] = input_line.split(" ")

def move_to_t(x, t_i):
    if t_i == 'R': #+
        x += 1
        return x
    else: #-
        x -= 1
        return x 

for i in range(N):
    # print(x_R, end=" ")
    # print(x_G, end=" ")
    # print(x_B, end="\n")
    
    if c[i] in ['R','Y','M','W']:
        x_R = move_to_t(x_R, t[i])
    if c[i] in ['G','Y','C','W']:
        x_G = move_to_t(x_G, t[i])
    if c[i] in ['B','M','C','W']:
        x_B = move_to_t(x_B, t[i])
    if x_R == x_G and x_G == x_B:
        print(x_R)
        exit()

print("no")