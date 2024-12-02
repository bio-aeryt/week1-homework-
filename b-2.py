# ターミナルで以下のコマンドを実行
# $ python b-2.py

# # 実行結果
# 行数を入力してください: 4
# 列数を入力してください: 6
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24


row = int(input("行数を入力してください:"))
column = int(input("列数を入力してください:"))

# 行の数の設定
row_numbers = []

i = 1
while i <= row:
    row_numbers.append(i)
    i += 1

# 列数の情報を踏まえて数のリストを作る
numbers_list = []

i = 1
while i <= column:
    numbers_list.extend([x * i for x in row_numbers])
    i += 1

# 分割 リストに追加

numbers_table = []
for i in range(0, row * column, row):
    numbers_table.append(numbers_list[i : i + row])

# 一行ずつ出力
for each_row in numbers_table:
    print(" ".join(map(str, each_row)))


def matrix_calculation():
    row = int(input("行数を入力してください:"))
    column = int(input("列数を入力してください:"))

    # 行の数の設定
    row_numbers = []

    i = 1
    while i <= row:
        row_numbers.append(i)
        i += 1

    # 列数の情報を踏まえて数のリストを作る
    numbers_list = []

    i = 1
    while i <= column:
        numbers_list.extend([x * i for x in row_numbers])
        i += 1

    # 分割 リストに追加

    numbers_table = []
    for i in range(0, row * column, row):
        numbers_table.append(numbers_list[i : i + row])

    # 一行ずつ出力
    for each_row in numbers_table:
        print(" ".join(map(str, each_row)))

    return
