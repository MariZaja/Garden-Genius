from dataclasses import dataclass
from typing import List, Dict, Optional



@dataclass
class Dimensions:
    type: Optional[str]
    min_value: float
    max_value: float
    unit: str

@dataclass
class WaterRequirement:
    unit: str
    value: float

@dataclass
class Hardiness:
    min: str
    max: str

@dataclass
class HardinessLocation:
    full_url: str
    full_iframe: str

@dataclass
class DefaultImage:
    image_id: int
    license: int
    license_name: str
    license_url: str
    original_url: str
    regular_url: str
    medium_url: str
    small_url: str
    thumbnail: str

@dataclass
class Species:
    id: int
    common_name: str
    scientific_name: List[str]
    other_name: List[str]
    type: str
    dimensions: Dimensions
    cycle: str
    watering: str
    depth_water_requirement: WaterRequirement
    volume_water_requirement: WaterRequirement
    watering_period: str
    watering_general_benchmark: Dict[str, int]
    sunlight: List[str]
    hardiness: Hardiness
    hardiness_location: HardinessLocation
    flowers: bool
    color: str
    soil: List[str]
    cones: bool
    fruits: bool
    edible_fruit: bool
    leaf_color: List[str]
    edible_leaf: bool
    growth_rate: str
    maintenance: str
    poisonous_to_humans: bool
    poisonous_to_pets: bool
    indoor: bool
    description: str
    default_image: DefaultImage


def create_species_from_json(json_data: dict) -> Species:
    dimensions = Dimensions(**json_data['dimensions'])
    depth_water_requirement = WaterRequirement(**json_data['depth_water_requirement'])
    volume_water_requirement = WaterRequirement(**json_data['volume_water_requirement'])
    hardiness = Hardiness(min=json_data['hardiness']['min'], max=json_data['hardiness']['max'])
    hardiness_location = HardinessLocation(**json_data['hardiness_location'])
    default_image = DefaultImage(**json_data['default_image'])

    return Species(
        id=json_data['id'],
        common_name=json_data['common_name'],
        scientific_name=json_data['scientific_name'],
        other_name=json_data['other_name'],
        type=json_data['type'],
        dimensions=dimensions,
        cycle=json_data['cycle'],
        watering=json_data['watering'],
        depth_water_requirement=depth_water_requirement,
        volume_water_requirement=volume_water_requirement,
        watering_period=json_data['watering_period'],
        watering_general_benchmark=json_data['watering_general_benchmark'],
        sunlight=json_data['sunlight'],
        hardiness=hardiness,
        hardiness_location=hardiness_location,
        flowers=json_data['flowers'],
        color=json_data['color'],
        soil=json_data['soil'],
        cones=json_data['cones'],
        fruits=json_data['fruits'],
        edible_fruit=json_data['edible_fruit'],
        leaf_color=json_data['leaf_color'],
        edible_leaf=json_data['edible_leaf'],
        growth_rate=json_data['growth_rate'],
        maintenance=json_data['maintenance'],
        poisonous_to_humans=json_data['poisonous_to_humans'],
        poisonous_to_pets=json_data['poisonous_to_pets'],
        indoor=json_data['indoor'],
        description=json_data['description'],
        default_image=default_image
    )

# @dataclass
# class Species:
#     id: int
#     common_name: str
#     scientific_name: List[str]
#     other_name: List[str]
#     # family: str # out
#     # origin: Optional[str] # out
#     type: str
#     dimensions: Dimensions
#     cycle: str
#     watering: str
#     depth_water_requirement: WaterRequirement
#     volume_water_requirement: WaterRequirement
#     watering_period: str
#     watering_general_benchmark: Dict[str, int]
#     # plant_anatomy: Dict[str, str] # out
#     sunlight: List[str]
#     # pruning_month: List[str] # out
#     # pruning_count: PruningCount # out
#     # seeds: int # out
#     # attracts: List[str] # out
#     # propagation: List[str] # out
#     hardiness: Hardiness
#     hardiness_location: HardinessLocation
#     flowers: bool
#     # flowering_season: str
#     color: str
#     soil: List[str]
#     pest_susceptibility: Optional[str]
#     cones: bool
#     fruits: bool
#     edible_fruit: bool
#     # fruit_color: Optional[str] # out
#     # fruiting_season: Optional[str] # out
#     # harvest_season: Optional[str] # out
#     # harvest_method: str # out
#     # leaf: bool # out
#     leaf_color: List[str]
#     edible_leaf: bool
#     growth_rate: str
#     maintenance: str
#     # medicinal: bool # out
#     poisonous_to_humans: bool
#     poisonous_to_pets: bool
#     # drought_tolerant: bool # out
#     # salt_tolerant: bool # out
#     # thorny: bool # out
#     # invasive: bool # out
#     # rare: bool # out
#     # rare_level: str # out
#     # tropical: bool # out
#     # cuisine: bool # out
#     indoor: bool
#     # care_level: str # out
#     description: str
#     default_image: DefaultImage





