import requests
from pprint import pprint


def get_recipe(ingredient):

    api_key = '33aaefd0024a6798b6324f2670c67a4f'
    #ingredient = 'chicken,tomato,'
    ingredient = input('What ingredients do you have? ')
    response = requests.get('https://www.food2fork.com/api/search?key={}&q={}'.format(api_key, ingredient))

    data = response.json()

    recipe = data

    return (recipe)

