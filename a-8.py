# users_info を使って次のような出力をしてください
# Name: Bob, Age: 79
# Name: Tom, Age: 59
# Name: Ken, Age: 61


users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]

for user_info in users_info:
    print(f"Name: {user_info[0]}, Age: {str(user_info[1])}")
