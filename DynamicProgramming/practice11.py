"""
https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_step1
python3 answer.py < input.txt
"""
import time

def answer():
    input_line = input()
    n, a, b= input_line.split(" ")
    n = int(n)
    a = int(a)
    b = int(b)
    dp = [10000] * (n+5)
    
    dp[0] = 0
    dp[2] = a
    dp[4] = a*2
    for i in range(5,n+5):
        dp[i] = min(dp[i-2] + a, dp[i-5] + b)

    print(min(dp[n],dp[n+1],dp[n+2],dp[n+3],dp[n+4]))


if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")