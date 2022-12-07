from django.conf import settings
import json
import os
from collections import defaultdict

import django
os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",  "backend.settings"
    )
django.setup()



'''

# -------------------------------------------------------------------------------
# read_country_data
# -------------------------------------------------------------------------------
def read_country_data():
    """Read Country data from json file

    Returns:
        list: list of country data
    """

    data_path = os.path.join(FIXTURES_ROOT, 'countries_states_cities.json')

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


# -------------------------------------------------------------------------------
# country_list
# -------------------------------------------------------------------------------
def country_list():
    """Get country list

    Returns:
        list: country list
    """
    if cache.has_key('country_list'):
        return cache.get('country_list')

    countries = [d['name'] for d in read_country_data()]
    cache.set('country_list', countries, 60*60*24)

    return countries


# -------------------------------------------------------------------------------
# state_list
# -------------------------------------------------------------------------------
def state_list(country_name):
    """Get state list of a country

    Args:
        country_name (str): country name

    Returns:
        list: state list
    """
    name_lookup = f'{country_name}_state_list'
    if cache.has_key(name_lookup):
        return cache.get(name_lookup)

    states = []
    country = next((d for d in read_country_data() if d['name'] == country_name), None)
    if country:
        states = [s['name'] for s in country['states']]
        cache.set(name_lookup, states, 60*60*24)

    return states


# -------------------------------------------------------------------------------
# city_list
# -------------------------------------------------------------------------------
def city_list(country_name, state_name):
    """Get City list of a country's state

    Args:
        country_name (str): country name
        state_name (str): state name

    Returns:
        list: city list
    """
    name_lookup = f'{country_name}_{state_name}_city_list'
    if cache.has_key(name_lookup):
        return cache.get(name_lookup)

    cities = []
    country = next((d for d in read_country_data() if d['name'] == country_name), None)
    if country:
        state = next(
            (s for s in country['states'] if s['name'] == state_name), None)
        if state:
            cities = [c['name'] for c in state['cities']]
            cache.set(name_lookup, cities, 60*60*24)

    return cities



    '''







def make_new_json(data):
    new_country_dict = {}

    for d in data:
        state = {}
        for s in  d['states']:
            state[s['name']] = [c['name'] for c in s['cities']]
        new_country_dict[d['name']] = state
    with open("countries_states_cities.json", "w") as outfile:
        json.dump(new_country_dict, outfile)
    print(new_country_dict)


def main_fun():
    data_path = settings.BASE_DIR / 'countries+states+cities.json'
    # print(settings.BASE_DIR)
    with open(data_path,'r' , encoding='utf-8') as f:
        data = json.load(f)
    make_new_json(data)
    return data


def new_main_fun():
    data_path = settings.BASE_DIR / 'countries_states_cities_lite.json'
    # print(settings.BASE_DIR)
    with open(data_path,'r' , encoding='utf-8') as f:
        data = json.load(f)
    # make_new_json(data)
    return data



if __name__ == '__main__':
    # data = main_fun()
    new_main_fun()

    # print(d)