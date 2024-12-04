# 別解
# b-2.py

rows = int(input("行数を入力してください: "))
columns = int(input("列数を入力してください: "))

# 行と列を基に表を生成
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print(i * j, end=" ")
    # print() だけを単独で使用すると、『改行文字（\n）」を出力
    print()
