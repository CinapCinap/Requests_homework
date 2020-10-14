import requests
import json


def get_hero_iq(name):
    token = ''
    url = 'https://superheroapi.com/api/' + str(token) + '/search/' + name
    headers = {'User-Agent': 'Smth'}
    response = requests.get(url, headers=headers, timeout=5)
    data = response.json()
    if (data['response'] == 'error'):
        print(f'Супергерой {name} в базе данных не найден.')
        iq = 'err'
    else:
        iq_tmp = []
        for elm in data['results']:
            if elm['name'] == name:
                if elm['powerstats']['intelligence'] != 'null':
                    iq_tmp.append(int(elm['powerstats']['intelligence']))
                else:
                    iq_tmp.append(0)
        if len(iq_tmp) == 1:
            iq = iq_tmp[0]
        elif len(iq_tmp) > 1:
            iq = max(iq_tmp)
        else:
            print(f'Супергерой {name} в базе данных не найден.')
            iq = 'err'
    return iq

def find_smartest_hero(*names):
    heroes_list = {}
    for name in names:
        iq = get_hero_iq(name)
        if iq == 'err':
            continue
        else:
            heroes_list[name] = iq
    heroes_list = list(heroes_list.items())
    heroes_list.sort(key=lambda i: i[1], reverse=True)
    if len(heroes_list) == 0:
        smartest = 'null'
    else:
        smartest = heroes_list[0]
    return smartest

def main():
    # Добавила имена, чтобы проверить отработку вариантов:
    # Если имени нет в базе, выводится сообщение, из остальных выбирается самый умный.
    # Если несколько героев с одинаковым именем, берется наибольшее значение intelligence.
    # Если intelligence = 'null', считаю равной 0.
    smartest = find_smartest_hero('Hulk', 'Captain America', 'Thanos', 'Rick', 'Morty', 'Spider-Man', 'Blue Beetle')
    if smartest != 'null':
        print(f'Самый умный супергерой - {smartest[0]}, уровень интеллекта - {smartest[1]}.')

main()