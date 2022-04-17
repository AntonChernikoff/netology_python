import requests
import datetime
import time

# https://api.stackexchange.com/2.3/questions?order=desc&min=1649980800&max=1650153600&sort=activity&site=stackoverflow

def request_stackoverflow():
    url_api = "https://api.stackexchange.com/2.3/questions"
    # # date_min = "17/04/2022"
    # # min = datetime.datetime.strptime(date_min, "%d/%m/%Y").timestamp()
    # # date_max = "15/04/2022"
    # # max = datetime.datetime.strptime(date_max, "%d/%m/%Y").timestamp()
    # date_max = datetime.datetime(2022,4,18)
    # date_min = datetime.datetime(2022,4,15)
    # # min = date_min.timestamp()
    # # max = date_max.timestamp()
    # max = date_max.strftime("%s")
    # min = date_min.strftime("%s")
    # # тренировался с датами, оставил для заметки
    # # date_max1 = datetime.datetime.fromtimestamp(int(max)).strftime('%Y-%m-%d %H:%M:%S')
    # # print(date_max1)
    # # date_min1 = datetime.datetime.fromtimestamp(int(min)).strftime('%Y-%m-%d %H:%M:%S')
    # # print(date_min1)
    from_date = datetime.datetime.today()-datetime.timedelta(days=2)
    from_date_int = from_date.strftime("%s")
    params = params = {
        "order": "desc"
        , "fromdate": {from_date_int}
        # , "min": {min}
        # , "max": {max}
        # , "sort": "activity"
        , "site": "stackoverflow"
        }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.get(url_api, headers=headers, params=params).json()
    return response


if __name__ == '__main__':
    result = request_stackoverflow()
    for question in result['items']:
        for tag in question['tags']:
            if 'python' == tag.lower():
                date_question = datetime.datetime.fromtimestamp(question['creation_date']).strftime('%Y-%m-%d %H:%M:%S')
                print(f"===> Дата: {date_question} Автор: {question['owner']['display_name']} Заголовок: {question['title']}")
                # print(f"Ссылка: {question['link']}")
                break




