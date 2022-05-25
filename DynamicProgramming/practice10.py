"""
https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_step0
python3 answer.py < input.txt
"""
import time

def answer():
    input_line = input()
    n, a, b= input_line.split(" ")
    n = int(n)
    a = int(a)
    b = int(b)
    dp = [0] * (n+1)
    
    dp[0] = 0
    dp[1] = a
    
    for i in range(2,n+1):
        dp[i] = min(dp[i-1] + a, dp[i-2] + b)
    
    print(dp[n])
    # print(dp)


if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")