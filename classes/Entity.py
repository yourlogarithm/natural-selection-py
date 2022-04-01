from abc import ABC
from typing import List, Tuple
from classes.Movement import Coordinates
from pygame import Rect

class Entity(ABC): 
    cells: List = []
    food: List = []

    def __init__(self, coordinates: Coordinates, size: int, color: str) -> None:
        super().__init__()
        self._coordinates: Coordinates = coordinates
        self._SIZE: int = size
        self.COLOR: str = color

    def asRect(self) -> Tuple[Tuple[int], Tuple[int]]:
        return Rect((self._coordinates.x, self._coordinates.y), (self._SIZE, self._SIZE))

    def spawn(self):
        if (str(type(self)) == "<class 'classes.Cell.Cell'>"): Entity.cells.append(self)
        else: Entity.food.append(self)

    def _terminate(self) -> None:
        if (str(type(self)) == "<class 'classes.Cell.Cell'>"): Entity.cells.remove(self)
        else: Entity.food.remove(self)
