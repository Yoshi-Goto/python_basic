# こういうことじゃないんだよね～？
yoko = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tate = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in yoko:
    new_list = []
    for m in tate:
        new_list.append(n * m)

    print(new_list)

# こんなのもあるかしら？？
for x in range(1, 10):
    new_list = []
    for y in range(1, 10):
        new_list.append(x * y)

    print(new_list)
