"""
python3 answer.py < input.txt
"""
import time

def answer():
    input_line = input()
    N, M = input_line.split(" ")
    N = int(N)
    M = int(M)



if __name__ == '__main__':
    start = time.time()
    answer()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")