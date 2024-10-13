from perenual import get_species_list, get_species_details
from helpers import read_key, read_keys

def one_key():
    key = read_key()

    start_id = int(input("Podaj id gatunku, od którego chcesz zacząć: "))
    if start_id < 1 or start_id > 2901:
        raise ValueError("start_id must be between 1 and 2901")

    for species_id in range(start_id, start_id + 100):
        species_details = get_species_details(species_id, key)

def main()-> None: # refaktoryzacja z chatem: https://chatgpt.com/share/66f86a93-25a8-800c-8b1e-1e77e0f9ac18
    keys = read_keys()

    for key in keys:
        print(f"Using key: {key}")

        start_id = int(input(f"Podaj id gatunku, od którego chcesz zacząć dla klucza {key}: "))
        if start_id < 1 or start_id > 2901:
            raise ValueError("start_id must be between 1 and 2901")

        for species_id in range(start_id, start_id + 100):
            get_species_details(species_id, key)

if __name__ == "__main__":
    main()