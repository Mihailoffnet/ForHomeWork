import requests
from pprint import pprint

def heroes_request(list_name):
    my_url = 'https://akabab.github.io/superhero-api/api/all.json'
    # my_params = {"": ""}
    # my_headers = {"": ""}
    response = requests.get(url=my_url, timeout=5)
    pprint(response.json())

    # проверка по статусу запроса

    if response.status_code != 200: 
            print('request error')
            print()
    else:
            print('good request')
            print()

    data = response.json()
    cleverest = 0
    for names in list_name:
        for dict in data:
            if dict.get('name') == names:
                if dict.get('powerstats').get('intelligence') > cleverest:
                    name = dict.get('name')
                    cleverest = dict.get('powerstats').get('intelligence')
                    result = f'Самый умный {name}, ум = {cleverest}'
    print(result)



list_name = ['Hulk', 'Captain America', 'Thanos'] # обозначаем список
a = heroes_request(list_name) # запускаем команду

