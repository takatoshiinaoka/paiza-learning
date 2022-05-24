"""
https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_step4
python3 answer.py < input.txt
"""
import time

def answer():
    input_line = input()
    k = int(input_line)
    
    a = [0] * k
    a[0] = 1
    a[1] = 1
    for i in range(2, k):
        a[i] = a[i-2]+a[i-1]
    
    print(a[i])




if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")