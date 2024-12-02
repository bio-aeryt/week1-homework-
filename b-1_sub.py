# 別解
# b-1.py
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    # print() だけを単独で使用すると、『改行文字（\n）」を出力
    print()
