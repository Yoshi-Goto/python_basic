gyo = int(input("行数を入力してください。"))
retu = int(input("列数を入力してください。"))

for x in range(1, gyo + 1):
    new_list = []
    for y in range(1, retu + 1):
        new_list.append(x * y)

    print(new_list)
