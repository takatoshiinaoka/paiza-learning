"""
https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_step1
"""
import time

def answer():
    input_line = input()
    x, d= input_line.split(" ")
    input_line = input()
    Q = int(input_line)
    x = int(x)
    d = int(d)
    k = [0] * Q
    max = 1000
    a = [0] * max

    for i in range(Q):
        input_line = input()
        k[i] = int(input_line) 
        # print(k)

    a[0]=x
    for i in range(1, max): # range(start, stop) <- (start ≦ i < stop)
        a[i] = a[i-1] + d

    for i in k:
        print(a[i-1])


if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")