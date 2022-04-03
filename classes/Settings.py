from abc import ABC
from typing import Final, Tuple
import json
from datetime import datetime

class Settings(ABC):
    _jsonData = json.load(open('./settings.json', 'r'))
    PATH = f'./data/{datetime.now().timestamp()}/'
    WIDTH = _jsonData['WIDTH']
    HEIGHT = _jsonData['HEIGHT']
    FPS = _jsonData['FPS']
    CELLS: Final[int] = _jsonData['CELLS']
    SIZE: Final[int] = _jsonData['SIZE']
    SPEED: Final[int] = _jsonData['SPEED']
    SENSE: Final[int] = _jsonData['SENSE']
    SHOW_RELATIVE_TO_INITIALS = _jsonData['SHOW_RELATIVE_TO_INITIALS']
    ENERGY: Final[int] = _jsonData['ENERGY']
    REQUIRED_SIZE_DIFFERENCE: Final[float] = _jsonData['REQUIRED_SIZE_DIFFERENCE']
    FOOD_SIZE: Final[int] = _jsonData['FOOD_SIZE']
    FOOD_AMOUNT_VARIATION: Final[Tuple[Tuple[int]]] = _jsonData['FOOD_AMOUNT_VARIATION']
    FOOD_DISTANCE_FROM_SPAWN: Final[int] = _jsonData['FOOD_DISTANCE_FROM_SPAWN']
    MUTATION_CHANCE: Final[float] = _jsonData['MUTATION_CHANCE']
    SIZE_MUTATION: Final[float] = _jsonData['SIZE_MUTATION']
    SPEED_MUTATION: Final[float] = _jsonData['SPEED_MUTATION']
    SENSE_MUTATION: Final[float] = _jsonData['SENSE_MUTATION']
    GENERATIONS: Final[int] = _jsonData['GENERATIONS']

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