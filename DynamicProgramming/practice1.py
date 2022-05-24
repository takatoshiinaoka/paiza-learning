# 動的計画法 (Dynamic Programming)
#「問題を部分問題に分割し、部分問題の答えを記録しながら、それらを利用することによって元の問題の答えを得る手法」
input_line = input()
x, d, k = input_line.split(" ")

x = int(x) # 初項
d = int(d) # 数列の差（等差数列）
k = int(k) # 求めたい項
a = [0] * (k + 1) 

# print(x)
# print(d)
# print(k)

a[1]=x
for i in range(2, k + 1): # range(start, stop) <- (start ≦ i < stop)
    a[i] = a[i-1] + d
print(a[k])