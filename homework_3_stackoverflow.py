import requests
import json
import datetime


def get_tagged_questions(tag, days):
    timedelta = datetime.timedelta(days=days)
    todate = datetime.date.today()
    fromdate = todate - timedelta
    todate = todate.strftime('%Y-%m-%d')
    fromdate = fromdate.strftime('%Y-%m-%d')

    url = 'https://api.stackexchange.com/2.2/search' \
          '?fromdate=' + fromdate + \
          '&todate=' + todate + \
          '&tagged=' + tag + \
          '&site=stackoverflow'
    response = requests.get(url)
    response = response.json()

    if response['has_more']:
        print(f"Найдено {len(response['items'])} вопросов"
              f" за последние {days} дней, содержащих тег '{tag}':")
        for elm in response['items']:
            print(f"{elm['title']}, {elm['link']}")
    else:
        print('По заданным параметрам ничего не найдено.')
        elm = 0
    return elm

def main():
    get_tagged_questions('python', 2)

main()