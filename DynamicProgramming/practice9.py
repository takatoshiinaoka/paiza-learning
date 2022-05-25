"""
https://paiza.jp/works/mondai/dp_primer/dp_primer_stairs_boss
python3 answer.py < input.txt
"""
import time

def answer():
    input_line = input()
    n, a, b, c = input_line.split(" ")
    n = int(n)
    a = int(a)
    b = int(b)
    c = int(c)
    
    k = [0] * (n+1)
    k[0]=1
    for i in range(1, n+1):
        if k[i-a]:
            k[i] = k[i] + k[i-a]
        if k[i-b]:
            k[i] = k[i] + k[i-b]
        if k[i-c]:
            k[i] = k[i] + k[i-c]
        
    
    print(k[i])
    print(k)






if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")