from abc import ABC
from typing import Final, Tuple
import json
from datetime import datetime

class Settings(ABC):
    PATH = f'./data/{datetime.now().timestamp()}/'
    WIDTH = 750
    HEIGHT = 750
    FPS = 0
    CELLS: Final[int] = 15
    SIZE: Final[int] = 7.5
    SPEED: Final[int] = 4
    SENSE: Final[int] = 30
    SHOW_RELATIVE_TO_INITIALS = True
    ENERGY: Final[int] = 50000
    REQUIRED_SIZE_DIFFERENCE: Final[float] = 1.3 # 30%
    FOOD_SIZE: Final[int] = 5
    FOOD_AMOUNT_VARIATION: Final[Tuple[Tuple[int]]] = (
        (100, 90),
        (20, 0)
    )
    FOOD_DISTANCE_FROM_SPAWN: Final[int] = 125
    MUTATION_CHANCE: Final[float] = 0.85
    SIZE_MUTATION: Final[float] = 0.1
    SPEED_MUTATION: Final[float] = 0.1
    SENSE_MUTATION: Final[float] =0.1
    GENERATIONS: Final[int] = 5000

    def toJSON() -> str:
        return json.dumps({
            'WIDTH': Settings.WIDTH,
            'HEIGHT': Settings.HEIGHT,
            'CELLS': Settings.CELLS,
            'SIZE': Settings.SIZE,
            'SPEED': Settings.SPEED,
            'SENSE': Settings.SENSE,
            'ENERGY': Settings.ENERGY,
            'REQUIRED_SIZE_DIFFERENCE': Settings.REQUIRED_SIZE_DIFFERENCE,
            'FOOD_SIZE': Settings.FOOD_SIZE,
            'FOOD_AMOUNT_VARIATION': Settings.FOOD_AMOUNT_VARIATION,
            'FOOD_DISTANCE_FROM_SPAWN': Settings.FOOD_DISTANCE_FROM_SPAWN,
            'MUTATION_CHANCE': Settings.MUTATION_CHANCE,
            'SIZE_MUTATION': Settings.SIZE_MUTATION,
            'SPEED_MUTATION': Settings.SPEED_MUTATION,
            'SENSE_MUTATION': Settings.SENSE_MUTATION,
            'GENERATIONS': Settings.GENERATIONS
        })