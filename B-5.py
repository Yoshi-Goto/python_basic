# これまたとんでもなくダサいコードになってます。
strtemp = "1 36 78 92 61 12 4 97 45 28 66"


def goukei():
    new_list = strtemp.split(' ')
    tot = 0
    for n in new_list:
        tot = tot + int(n)

    return tot


def saidai():
    new_list = strtemp.split(' ')
    cnt = 1
    a = 0
    for n in new_list:
        if cnt == 1:
            a = int(n)
        else:
            if a < int(n):
                a = int(n)

        cnt += 1

    return a


def saisyo():
    new_list = strtemp.split(' ')
    cnt = 1
    i = 0
    for n in new_list:
        if cnt == 1:
            i = int(n)
        else:
            if i > int(n):
                i = int(n)

        cnt += 1

    return i


def heikin():
    new_list = strtemp.split(' ')
    cnt = 0
    tot = 0
    for n in new_list:
        tot = tot + int(n)
        cnt += 1

    return tot / cnt


def main():
    print(goukei())
    print(saidai())
    print(saisyo())
    print(heikin())


if __name__ == '__main__':
    main()
