"""
https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_step3
python3 answer.py < input.txt
"""
import time

def answer():
    input_line = input()
    x, d_1, d_2 = input_line.split(" ")
    input_line = input()
    Q = int(input_line)
    x = int(x)
    d_1 = int(d_1)
    d_2 = int(d_2)
    k = [0] * Q
    max=0
    
    
    for i in range(Q):
        input_line = input()
        k[i] = int(input_line)
        if max<k[i]:
            max = k[i]
    
    a = [0] * max
    a[0]=x
    for i in range(1,max):
        if i&1:
            # print("偶数")
            a[i] = a[i-1] + d_2
        else:
            # print("奇数")
            a[i] = a[i-1] + d_1
    
    for i in k:
        print(a[i-1])








if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")