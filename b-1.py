# 下記のような出力が得られる b-1.py を実装してください。
# # ターミナルで以下のコマンドを実行
# $ python b-1.py
# # 実行結果
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8 10 12 14 16 18
# 3 6 9 12 15 18 21 24 27
# 4 8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54
# 7 14 21 28 35 42 49 56 63
# 8 16 24 32 40 48 56 64 72
# 9 18 27 36 45 54 63 72 81

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# リスト内包表記で1~81までのリストを作ってから、分割
# [x * 2 for x in numbers] で、リストの要素を２倍

# 1~81までのリストを作成
numbers_1_81 = []

i = 1
while i <= 9:
    numbers_1_81.extend([x * i for x in numbers])
    i += 1

# 分割 9の倍数でスライス{range(start, stop(含くまれない), step)}し、リストの形でnumber_tableリストに追加する

numbers_table = []
for i in range(0, 81, 9):
    numbers_table.append(numbers_1_81[i : i + 9])


# 一行ずつ出力 rowはnumbers_table中のリストを[]ごとに抽出　map(str, row) は、row の各要素を文字列に変換するために使用。
for row in numbers_table:
    print(" ".join(map(str, row)))
