import random

def saikoro(men, kai):
    n = 1
    new_list = []
    while n <= kai:
        # 1からだと面数は1足してよいのかな？むむっ
        new_list.append(random.randint(1, men + 1))
        n += 1
    return new_list


def main():
    r = int(input("サイコロの面の数は?:"))
    c = int(input("何回振りますか?:"))

    print(saikoro(r, c))


if __name__ == '__main__':
    main()
