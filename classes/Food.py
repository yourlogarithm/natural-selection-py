from random import randrange
from classes.Entity import Entity
from classes.Movement import Coordinates
from classes.Settings import Settings

class Food(Entity):
    Variations: int = len(Settings.FOOD_AMOUNT_VARIATION)
    variationIndex: int = 0

    def generate() -> None:
        Entity.food.clear()
        for _ in range(Settings.FOOD):
            x: int = randrange(Settings.FOOD_DISTANCE_FROM_SPAWN, Settings.WIDTH-Settings.FOOD_DISTANCE_FROM_SPAWN)
            y: int = randrange(Settings.FOOD_DISTANCE_FROM_SPAWN, Settings.HEIGHT-Settings.FOOD_DISTANCE_FROM_SPAWN)
            coordinates: Coordinates = Coordinates(x, y)
            Food(coordinates, Settings.FOOD_SIZE, '#e069ba').spawn()

        if (Settings.FOOD_AMOUNT_VARIATION[Food.variationIndex] > Settings.FOOD):
            Settings.FOOD += 1
        elif (Settings.FOOD_AMOUNT_VARIATION[Food.variationIndex] < Settings.FOOD):
            Settings.FOOD -= 1
        else: 
            Food.variationIndex += 1
            if (Food.variationIndex == Food.Variations and Settings.CYCLIC_VARIATION):
                Food.variationIndex = 0



    def __init__(self, coordinates: Coordinates, size: int, color: str) -> None:
        super().__init__(coordinates, size, color)
        
    