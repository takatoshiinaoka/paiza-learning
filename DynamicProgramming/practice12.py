"""
https://paiza.jp/works/mondai/dp_primer/dp_primer_apples_step2
python3 answer.py < input.txt
"""
import time

def answer():
    input_line = input()
    n, x, a, y, b= input_line.split(" ")
    n = int(n) #ほしいりんごの数
    x = int(x)
    a = int(a) #x個でa円
    y = int(y)
    b = int(b) #y個でb円
    dp = [10000] * (n + max(x, y))
    
    print(b)

    dp[0] = 0
    for i in range(1, n+max(x,y)+1):
        if i%x == 0:
            dp[i] = min(dp[i], (i/x) * a)
        if i%y == 0:
            dp[i] = min(dp[i], (i/y) * b)
        if i>a and i>b:
            dp[i] = min(dp[i],dp[i-x] + a, dp[i-y] + b)
    
    print(dp)
    print(min(dp[n:]))


if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")