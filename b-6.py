# # ターミナルで以下のコマンドを実行
# $ python b-6.py

# # 実行結果
# サイコロの面の数は?: 8
# 何回振りますか?: 20
# [6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]


# N面サイコロをM回振ったときの結果を表示してください

N = int(input("サイコロの面の数は?:"))
M = int(input("何回振りますか?:"))

# random関数を用いて、一回の施行で出る数字を考える
import random


def dice():
    return random.randrange(1, N)


# M回やる時のことを考える
log = []
throw = 0
while throw <= M - 1:
    log.append(dice())
    throw += 1

print(log)
