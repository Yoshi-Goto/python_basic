import random


def dice():
    num = random.randint(1, 6)
    return num


# 面倒なので10回繰り返してみよう！！
n = 1
while n <= 10:
    print(dice())
    n += 1
