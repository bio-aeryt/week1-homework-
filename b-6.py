# # ターミナルで以下のコマンドを実行
# $ python b-6.py

# # 実行結果
# サイコロの面の数は?: 8
# 何回振りますか?: 20
# [6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]


# N面サイコロをM回振ったときの結果を表示してください

n = int(input("サイコロの面の数は?:"))
m = int(input("何回振りますか?:"))

# random関数を用いて、一回の施行で出る数字を考える
import random


def dice(n):
    return random.randrange(1, n)


# M回やる時のことを考える
log = []
throw = 0
while throw <= m - 1:
    log.append(dice(n))
    throw += 1

print(log)
