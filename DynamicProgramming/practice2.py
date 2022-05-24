import time
start = time.time()



input_line = input()
x, d= input_line.split(" ")
input_line = input()
Q = int(input_line)
x = int(x)
d = int(d)
k = [0] * Q
a = [0] * (Q+1)

for i in range(Q):
    input_line = input()
    k[i] = int(input_line) 
    # print(k)

a[1]=x
for i in range(2, Q+1): # range(start, stop) <- (start ≦ i < stop)
    a[i] = a[i-1] + d

for i in k:
    print(a[i])

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")