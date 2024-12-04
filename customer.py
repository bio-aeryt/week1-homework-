class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # C-1. フルネームを取得できる
    # print(ken.full_name())  # "Ken Tanaka" という値を出力
    # print(tom.full_name())  # "Tom Ford" という値を出力

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    # C-2. 年齢という概念の追加
    # print(ken.age)  # 15 という値を出力
    # print(tom.age) # 57 という値を出力
    # print(ieyasu.age) # 75 という値を出力
    # def __init__で実装済み

    # C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
    # 料金の計算ルール
    # こども料金(20歳未満): 1000円
    # おとな料金(20歳以上65歳未満): 1500円
    # シニア料金(65歳以上): 1200円
    # print(ken.entry_fee())  # 1000 という値を出力

    def entry_fee(self):
        if self.age < 20:
            fee = 1000

        elif self.age >= 65:
            fee = 1200

        else:
            fee = 1500        

        return fee

    # C-4. 単一の顧客情報をCSV形式で取得できる
    # print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力

    def info_csv(self):
        import csv
        import io

        # ファイルのようなものを作る 実際にファイルを作成する必要がない場合に便利
        output = io.StringIO()

        # ファイルではなく、StringIOオブジェクトに対して書き込みする
        writer = csv.writer(output)
        writer.writerow([self.full_name(), self.age, self.entry_fee()])
        # StringIOオブジェクトに書き込んだ内容を文字列として取得
        csv_data = output.getvalue()
        output.close()

        return csv_data


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

# kenはcustomerクラスのインスタンス
print(ken.full_name())
print(ken.age)
print(ken.entry_fee())
print(ken.info_csv())
