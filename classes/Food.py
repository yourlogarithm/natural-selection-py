from random import randrange
from classes.Entity import Entity
from classes.Movement import Coordinates
from classes.Settings import Settings

class Food(Entity):
    variationIndex: int = 0
    hold: int = 0
    repeat: bool = True

    def generate() -> None:
        Entity.food.clear()
        for _ in range(Settings.FOOD):
            x: int = randrange(Settings.FOOD_DISTANCE_FROM_SPAWN, Settings.WIDTH-Settings.FOOD_DISTANCE_FROM_SPAWN)
            y: int = randrange(Settings.FOOD_DISTANCE_FROM_SPAWN, Settings.HEIGHT-Settings.FOOD_DISTANCE_FROM_SPAWN)
            coordinates: Coordinates = Coordinates(x, y)
            Food(coordinates, Settings.FOOD_SIZE, '#e069ba').spawn()

        if (Food.repeat):
            target = Settings.FOOD_AMOUNT_VARIATION[Food.variationIndex][0]
            if (target > Settings.FOOD):
                Settings.FOOD += 1
            elif (target < Settings.FOOD):
                Settings.FOOD -= 1
            else: Food.hold += 1

            if (Food.hold == Settings.FOOD_AMOUNT_VARIATION[Food.variationIndex][1] and Settings.FOOD_AMOUNT_VARIATION[Food.variationIndex][1] != 0):
                Food.hold = 0
                Food.variationIndex += 1
                if (Food.variationIndex == len(Settings.FOOD_AMOUNT_VARIATION)):
                    Food.variationIndex = 0
            elif (target == Settings.FOOD and not Settings.FOOD_AMOUNT_VARIATION[Food.variationIndex][1]):
                Food.repeat = False

            


    def __init__(self, coordinates: Coordinates, size: int, color: str) -> None:
        super().__init__(coordinates, size, color)
        
    