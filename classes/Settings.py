from abc import ABC
from typing import Dict, Final, Tuple

class Settings(ABC):
    WIDTH = 750
    HEIGHT = 750
    FPS = 0
    CELLS: Final[int] = 15
    SIZE: Final[int] = 7.5
    SPEED: Final[int] = 4
    SENSE: Final[int] = 30
    ENERGY: Final[int] = 50000
    REQUIRED_SIZE_DIFFERENCE: Final[float] = 1.3 # 30%
    FOOD: Final[int] = 20
    FOOD_SIZE: Final[int] = 5
    FOOD_AMOUNT_VARIATION: Final[Tuple[Tuple[int]]] = (
        (20, 90),
        (80, 90),
        (80, 90),
        (50, 90)
    )
    FOOD_DISTANCE_FROM_SPAWN: Final[int] = 125
    MUTATION_CHANCE: Final[float] = 0.4
    SIZE_MUTATION: Final[float] = 0.1
    SPEED_MUTATION: Final[float] = 0.1
    SENSE_MUTATION: Final[float] =0.1
    GENERATIONS: Final[int] = 5000