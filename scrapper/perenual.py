import requests
import json
from enums import Order, CycleType, Watering, Sunlight

def get_species_list(key: str, page: int = None, q: str = None, order: Order = None, edible: bool = None,
        poisonous: bool = None, cycle: CycleType = None, watering: Watering = None, sunlight: Sunlight = None,
        indoor: bool = None, hardiness: str = None):
    url = f"https://perenual.com/api/species-list?key={key}"
    if page is not None:
        url += f"&page={page}"
    if q is not None:
        url += f"&q={q}"
    if order is not None:
        url += f"&order={order.value}"
    if edible is not None:
        url += f"&edible={int(edible)}"
    if poisonous is not None:
        url += f"&poisonous={int(poisonous)}"
    if cycle is not None:
        url += f"&cycle={cycle.value}"
    if watering is not None:
        url += f"&watering={watering.value}"
    if sunlight is not None:
        url += f"&sunlight={sunlight.value}"
    if indoor is not None:
        url += f"&indoor={int(indoor)}"
    if hardiness is not None:
        url += f"&hardiness={hardiness}"

    #print(url)

    payload = {}
    headers = {}
    response = requests.request("get", url, headers=headers, data=payload)

    if response.status_code == 200:
        # Parsing response as JSON
        data = response.json()

        with open('species_list/species_list.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
         print(f"The request failed with status code: {response.status_code}")

    return response.json()

def get_species_details(id: int, key: str):
    url = f"https://perenual.com/api/species/details/[{id}]?key={key}"

    payload = {}
    headers = {}
    response = requests.request("get", url, headers=headers, data=payload)

    if response.status_code == 200:
        # Parsing response as JSON
        data = response.json()

        with open(f"species_details/species_{id}_details.json", 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"The request failed with status code: {response.status_code}")

    return response.json()