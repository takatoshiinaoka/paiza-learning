"""
https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_boss
python3 answer.py < input.txt
"""
import time

def answer():
    input_line = input()
    Q = int(input_line)
    k = [0] * Q
    max = 0
    
    for i in range(Q):
        input_line = input()
        k[i] = int(input_line)
        if max < k[i]:
            max=k[i]
    
    a = [0] * max
    a[0] = 1
    a[1] = 1 
    for i in range(2, max):
        a[i] = a[i-2] + a[i-1]
    
    for i in k:
        print(a[i-1])





if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")