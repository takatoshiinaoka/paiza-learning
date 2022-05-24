"""
https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_step2
python3 answer.py < input.txt
"""
import time

def answer():
    input_line = input()
    x, d_1, d_2, k = input_line.split(" ")
    x = int(x)
    d_1 = int(d_1)
    d_2 = int(d_2)
    k = int(k)
    a = [0] * k

    a[0]=x
    for i in range(1, k):
        if i&1: # 奇数の時,偶数の処理
            # print("奇数")
            a[i] = a[i-1] + d_2
        else: # 偶数
            # print("偶数")
            a[i] = a[i-1] + d_1
    
    print(a[k-1])



if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")