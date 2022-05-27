# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
k, s = map(int, input().split(" ")) 
answer = int(0)

for x in range(k+1):
    for y in range(k+1):
        # 3重にすると時間オーバーする
        # for z in range(k+1):
        #     if (x+y+z)==s:
        #         answer += 1
        z = s-(x+y)
        if 0 <= z <= k:
            answer += 1

print(answer)







