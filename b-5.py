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

    return total


# 最大値　降順にソートして最初の数字を持ってくる
def max(data_list):
    data_list.sort(reverse=True)
    
    return data_list[0]


# 最小値　最大値の逆
def min(data_list):
    data_list.sort()

    return data_list[0]


# 平均値
def average(data_list):
    total = 0
    for number in data_list:
        total += number
    result = total / len(data_list)

    return int(result)


print(sum_of_list(data_list))
print(max(data_list))
print(min(data_list))
print(average(data_list))