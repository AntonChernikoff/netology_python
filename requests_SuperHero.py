from pprint import pprint
import requests

# https://superheroapi.com/api/2619421814940190/332/powerstats Halk
# https://superheroapi.com/api/2619421814940190/149/powerstats Captain America
# https://superheroapi.com/api/2619421814940190/655/powerstats Thanos

def request_hero(id_hero:str):
    url_api = "https://superheroapi.com/api/2619421814940190/"
    url = f"{url_api}{id_hero}/powerstats"
    response = requests.get(url)
    return response.json()

def get_intelligence_hero(id_hero:str) -> int:
    result = request_hero(id_hero)
    # print(result)
    return int(result['intelligence'])

if __name__ == '__main__':
    
    heros = [
                {'name':'Halk', 'id':'332', 'Intelligence':0}
                ,{'name':'Captain America', 'id':'149', 'Intelligence':0}
                ,{'name':'Thanos', 'id':'655', 'Intelligence':0}
            ]
    for hero in heros:
        hero['Intelligence'] = get_intelligence_hero(hero['id'])

    pprint(heros)

    hero_max_Intelligence = ''
    max_Intelligence = 0
    for hero in heros:
        if hero['Intelligence'] >= max_Intelligence:
            max_Intelligence = hero['Intelligence']
            hero_max_Intelligence = hero['name']
    print(f"Супергерой {hero_max_Intelligence} самый умный! Уровень Intelligence = {max_Intelligence}")

