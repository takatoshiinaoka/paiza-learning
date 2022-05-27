# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import math

N = int(input())
x = [0] * N
y = [0] * N
ma = 0.0

for i in  range(N):
    input_line = input()
    x[i], y[i] = map(int, input_line.split(" ")) 

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if i == j:
            continue
        len = math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
        if len > ma:
            ma = len

print(ma)


