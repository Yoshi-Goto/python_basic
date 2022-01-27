# 非常にダサくなってしまいましたが実力はこんなもん！！

def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},
        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},
        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    tot = 0
    for n in weather_information:
        tot = tot + n['temperature']

    print(tot / len(weather_information))
    # もっと簡単な方法があるなずだが・・・

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    new_list = []
    for n in weather_information:
        if n['prefecture'] == '大阪府':
            new_list.append(n['station'])

    print(new_list)
    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    tot = 0
    cnt = 0
    for n in weather_information:
        if n['prefecture'] == '福岡県':
            tot = tot + n['temperature']
            cnt += 1

    print(tot / cnt)

if __name__ == '__main__':
    main()
