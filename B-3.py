# Python 九九で検索した結果の例を整形してみる（なるほど）

yoko = int(input("行数を入力してください:"))
tate = int(input("列数を入力してください:"))

for r in range(1, yoko + 1):
    for c in range(1, tate + 1):
        print(f'{c} × {r} = {r*c:2d}', end='|')
    print('\n', end='')
