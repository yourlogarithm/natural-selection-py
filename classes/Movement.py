from abc import ABC
from enum import Enum
from math import sqrt, atan2, pi
from typing import Final, Tuple
from classes.Settings import Settings

class Direction(Enum):
    LEFT = 3
    RIGHT = 1
    UP = 0
    DOWN = 2
    UP_LEFT = 4
    UP_RIGHT = 5
    DOWN_LEFT = 6
    DOWN_RIGHT = 7

class Coordinates:
    def getDistanceToPoint(coordinatesA, coordinatesB) -> int:
        return sqrt((coordinatesA.x-coordinatesB.x)**2 + (coordinatesA.y - coordinatesB.y)**2)

    def getTotalDifferenceXY(coordinatesA, coordinatesB) -> int: 
        return abs(coordinatesA.x - coordinatesB.x) + abs(coordinatesA.y - coordinatesB.y)

    def getAngleDegrees(coordinatesA, coordinatesB) -> int:
        deltaX: int = coordinatesA.x - coordinatesB.x
        deltaY: int = coordinatesB.y - coordinatesA.y
        radians: int = atan2(deltaY, deltaX)
        degrees: int = (radians * 180) / pi
        while (degrees >= 360): degrees -= 360
        while (degrees < 0): degrees += 360
        return degrees

    def getAverageAngle(origin, coordinatesList) -> int:
        total: int = 0
        for coordinates in coordinatesList:
            total += Coordinates.getAngleDegrees(origin, coordinates)
        return total / len(coordinatesList)

    def getOppositeAngle(angle: int) -> int: 
        return (angle + 180) % 360

    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def asTuple(self):
        return self.x, self.y

class Corners(ABC):
    _TOP_LEFT: Final[Tuple[int]] = (5, 5)
    _TOP_RIGHT: Final[Tuple[int]] = (Settings.WIDTH-Settings.SIZE - 5, 5)
    _BOTTOM_LEFT: Final[Tuple[int]]= (5, Settings.HEIGHT-Settings.SIZE - 5)
    _BOTTOM_RIGHT: Final[Tuple[int]] = (Settings.WIDTH-Settings.SIZE - 5, Settings.HEIGHT-Settings.SIZE - 5)

    def TOP_LEFT():
        return Coordinates(*Corners._TOP_LEFT)
    
    def TOP_RIGHT():
        return Coordinates(*Corners._TOP_RIGHT)

    def BOTTOM_LEFT():
        return Coordinates(*Corners._BOTTOM_LEFT)
    
    def BOTTOM_RIGHT():
        return Coordinates(*Corners._BOTTOM_RIGHT)

    def asTuple() -> Tuple: 
        return Corners.TOP_LEFT(), Corners.TOP_RIGHT(), Corners.BOTTOM_LEFT(), Corners.BOTTOM_RIGHT()