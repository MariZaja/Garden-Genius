from perenual import get_species_list, get_species_details
from helpers import get_first_x_ids, read_key
from species import Species, create_species_from_json
import json



def main()-> None:
    key = read_key()

    #plant_list = get_species_list(key, q="strawberry")

    #species_ids = get_first_x_ids(plant_list, 5)

    # species_details = get_species_details(101, key)
    # species = create_species_from_json(species_details)
    # print(f"{species.common_name}")

    start_id = int(input("Podaj id gatunku, od którego chcesz zacząć: "))
    if start_id < 1 or start_id > 2901:
        raise ValueError("start_id must be between 1 and 2901")

    for species_id in range(start_id, start_id + 100):
        species_details = get_species_details(species_id, key)

        # species = create_species_from_json(species_details)
        # print(species.__dict__)
        # print(f"{species.common_name}")




if __name__ == "__main__":
    main()