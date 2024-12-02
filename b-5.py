# # ターミナルで以下のコマンドを実行
# $ python b-5.py

# # 実行結果
# データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
# 合計値: 54
# 最大値: 21
# 最小値: 1
# 平均値: 6

data = input("データを入力してください(スペース区切り) >")

# スペース区切りのデータをリストにする
data_list = list(map(int, data.split()))


# 合計値
def sum_of_list(data_list):
    total = 0
    for number in data_list:
        total += number
    print(total)

    return


# 最大値　降順にソートして最初の数字を持ってくる
def max(data_list):
    data_list.sort(reverse=True)
    print(data_list[0])
    return


# 最小値　最大値の逆
def min(data_list):
    data_list.sort()
    print(data_list[0])
    return


# 平均値
def average(data_list):
    total = 0
    for number in data_list:
        total += number
    result = total / len(data_list)
    print(int(result))


sum_of_list(data_list)
max(data_list)
min(data_list)
average(data_list)
