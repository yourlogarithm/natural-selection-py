from abc import ABC
from typing import Final, Tuple

class Settings(ABC):
    WIDTH = 750
    HEIGHT = 750
    FPS = 60
    CELLS: Final[int] = 15
    SIZE: Final[int] = 7.5
    SPEED: Final[int] = 4
    SENSE: Final[int] = 30
    ENERGY: Final[int] = 50000
    REQUIRED_SIZE_DIFFERENCE: Final[float] = 0.4
    FOOD: Final[int] = 15
    FOOD_SIZE: Final[int] = 5
    FOOD_AMOUNT_VARIATION: Final[Tuple[int]] = (100, 150, 75, 50)
    FOOD_DISTANCE_FROM_SPAWN: Final[int] = 125
    CYCLIC_VARIATION: bool = True
    MUTATION_CHANCE: Final[float] = 0.4
    SIZE_MUTATION: Final[float] = 0.1
    SPEED_MUTATION: Final[float] = 0.1
    SENSE_MUTATION: Final[float] =0.1
    GENERATIONS: Final[int] = 5000