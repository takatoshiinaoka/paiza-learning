"""
https://paiza.jp/works/mondai/dp_primer/dp_primer_stairs_step0
python3 answer.py < input.txt
"""
import time

def answer():
    input_line = input()
    n = int(input_line)
    
    dp = [0] * (n+1)
    dp[0] = 1
    
    for i in range(1, n+1):
        dp[i] = 0
        if i >= 1:
            dp[i] = dp[i] + dp[i-1] #i-1段目から1段上ってi段へ到着
        if i >= 2:
            dp[i] = dp[i] + dp[i-2] # i-2段目から2段上ってi段へ到着
    
    print(dp[n])





if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")