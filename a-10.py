# 下記のコードが期待通り動作するような、dice() 関数を実装してください ※ dice()関数は1から6の整数をランダムに返す
# print(dice())  # 1から6の整数をランダムに出力する

import random


def dice():
    return random.randrange(1, 7)


print(dice())
