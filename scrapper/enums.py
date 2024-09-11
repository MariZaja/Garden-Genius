from enum import Enum

class Order(Enum):
    """Enum for order types."""
    ASC = "asc"
    DESC = "desc"

class CycleType(Enum):
    """Enum for plant cycle types."""
    PERENNIAL = "perennial"
    ANNUAL = "annual"
    BIENNIAL = "biennial"
    BIANNUAL = "biannual"

class Watering(Enum):
    """Enum for watering amount."""
    FREQUENT = "frequent"
    AVERAGE = "average"
    MINIMUM = "minimum"
    NONE = "none"

class Sunlight(Enum):
    """Enum for sunlight amount."""
    FULL_SHADE = "full_shade"
    PART_SHADE = "part_shade"
    SUN_PART_SHADE = "sun-part_shade"
    FULL_SUN = "full_sun"
