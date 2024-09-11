from perenual import get_species_list, get_species_details
from helpers import get_first_x_ids, read_key
from species import Species, create_species_from_json
import json



def main()-> None:
    key = read_key()

    #plant_list = get_species_list(key, q="strawberry")

    #species_ids = get_first_x_ids(plant_list, 5)

    #for species_id in species_ids:
    for species_id in range(2, 21):
        species_details = get_species_details(species_id, key)
        species = create_species_from_json(species_details)
        #print(species.__dict__)
        print(f"{species.common_name}")




if __name__ == "__main__":
    main()