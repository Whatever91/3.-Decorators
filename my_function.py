import requests

from parameters_decorator import logger


def _get_list_of_heroes(some_list):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url).json()
    heroes_list = []
    for item in response:
        if item["name"] in some_list:
            heroes_list.append(item)
    heroes_list.sort(key=lambda x: x['powerstats']['intelligence'], reverse=True)
    return heroes_list


@logger(path="super_hero.log")
def make_heroes_rating(some_list):
    heroes_list = _get_list_of_heroes(some_list)
    for id, hero in enumerate(heroes_list):
        return f"На {id + 1} месте по интеллекту стоит среди {', '.join(some_list)} стоит {hero['name']} " \
               f"с показателем {hero['powerstats']['intelligence']} единиц интеллекта"


if __name__ == '__main__':
    make_heroes_rating(['Hulk', 'Captain America', 'Thanos'])
