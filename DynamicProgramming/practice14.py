"""
https://paiza.jp/works/mondai/dp_primer/dp_primer_lis_continuous_step0
python3 answer.py < input.txt
"""
import time

def answer():
    input_line = input()
    n= int(input_line) 
    a = [0] * n
    dp = [0] * n

    for i in range(n):
        input_line = input()
        a[i] = int(input_line) 
    
    # print(a)
    # print(dp)
    dp[0] = 1
    for i in range(1, n):
        if a[i-1] <= a[i]:
            dp[i] = dp[i-1]+1
        else:
            dp[i] = 1
    
    print(max(dp))


if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")