from ctypes import Union
from enum import Enum
from random import choice, randrange
from math import ceil
from typing import Final, List
from classes.Entity import Entity
from classes.Food import Food
from classes.Movement import Coordinates, Corners, Direction
from classes.Settings import Settings

class CellState(Enum):
    HOME = 0
    WANDERING = 1
    GRABBING = 2
    ATTACKING = 3
    FLEEING = 4
    RETURNING = 5


class Cell(Entity):
    def areAllHome() -> bool:
        for cell in Entity.cells:
            cell: Cell
            if cell.state != CellState.HOME:
                return False
        return True

    def startGeneration() -> None:
        for cell in Entity.cells:
            cell: Cell
            cell._reset()

    def endGeneration() -> None:
        length: int = len(Entity.cells)
        i: int = 0
        while i < length:
            cell: Cell = Entity.cells[i]
            if cell._score == 0:
                cell._terminate() 
                length -= 1
            else:
                if cell._score == 2: cell._clone()
                i += 1

    def __init__(self, coordinates: Coordinates, size: int, color: str, speed: int, sense: int) -> None:
        super().__init__(coordinates, size, color)
        self.state = CellState.HOME
        self._SPEED: Final[int] = speed
        self._SENSE: Final[int] = sense
        self._score: int = 0
        self._energy: int = Settings.ENERGY
        self._ENERGY_COST: Final[int] = speed ** 2 + size ** 2 + sense
        self._movesCounter = 0
        self._direction = self.getRandomDirection(True)
        self._nearestCorner: Union[Coordinates, None] = None

    def executeState(self):
        match self.state:
            case CellState.WANDERING:
                self._wander()
            case CellState.GRABBING:
                self._grab()
            case CellState.ATTACKING:
                self._attack()
            case CellState.FLEEING:
                self._flee()
            case CellState.RETURNING:
                self._returnHome()

    def _move(self) -> None:
        self._movesCounter += 1
        self._energy -= self._ENERGY_COST
        match self._direction:
            case Direction.LEFT: self._coordinates.x -= self._SPEED
            case Direction.RIGHT: self._coordinates.x += self._SPEED
            case Direction.UP: self._coordinates.y -= self._SPEED
            case Direction.DOWN: self._coordinates.y += self._SPEED  
            case Direction.UP_LEFT:
                value: int = self._SPEED / 2
                self._coordinates.x -= value
                self._coordinates.y -= value
            case Direction.UP_RIGHT:
                value: int = self._SPEED / 2
                self._coordinates.x += value
                self._coordinates.y -= value
            case Direction.DOWN_LEFT:
                value: int = self._SPEED / 2
                self._coordinates.x -= value
                self._coordinates.y += value
            case Direction.DOWN_RIGHT:
                value: int = self._SPEED / 2
                self._coordinates.x += value
                self._coordinates.y += value

    def isEnoughEnergy(self) -> bool:
        nearestCorner: Coordinates = self._getNearestCorner()
        # TODO: compare getDistanceToPoint() and getTotalDifferenceXY()
        xyTotalDifference: int = Coordinates.getDistanceToPoint(self._coordinates, nearestCorner)
        energyToGoHome: int = ceil(xyTotalDifference / self._SPEED) * self._ENERGY_COST
        return energyToGoHome < self._energy

    def _getNearestCorner(self, assign = False) -> Coordinates:
        if not self._nearestCorner:
            nearestCorner: Coordinates = Corners.TOP_LEFT()
            distanceToNearestCorner: int = Coordinates.getDistanceToPoint(self._coordinates, nearestCorner)
            for corner in Corners.asTuple():
                newDistance: int = Coordinates.getDistanceToPoint(self._coordinates, corner)
                if (distanceToNearestCorner > newDistance):
                    nearestCorner = corner
                    distanceToNearestCorner = newDistance
            if assign: self._nearestCorner = nearestCorner
            return nearestCorner
        return self._nearestCorner

    def _nearestFood(self) -> Food:
        nearestFruit: Food = None
        if (len(Entity.food) > 0):
            distance: int = Settings.WIDTH * Settings.HEIGHT
            for food in Entity.food:
                food: Food
                newDistance: int = Coordinates.getDistanceToPoint(self._coordinates, food._coordinates)
                if newDistance < distance and newDistance <= self._SENSE:
                    nearestFruit = food
                    distance = newDistance
        return nearestFruit

    def getRandomDirection(self, initial: bool = False) -> Direction:
        if (initial):
            if self._coordinates == Corners.TOP_LEFT(): return Direction.DOWN_RIGHT
            elif self._coordinates == Corners.TOP_RIGHT(): return Direction.DOWN_LEFT
            elif self._coordinates == Corners.BOTTOM_LEFT(): return Direction.UP_RIGHT
            else: return Direction.UP_LEFT
  

        possibleDirections: List[Direction] = []
        
        for direction in Direction:
            if direction != self._direction:
                possibleDirections.append(direction)
                
        randomint: int = randrange(0, len(possibleDirections))
        return possibleDirections[randomint]

    def _wander(self):
        if not self.isEnoughEnergy():
            self.state = CellState.RETURNING
            return

        # if len(self._enemiesNearby()) > 0 and self._movesCounter > 35:
        #     self.state = CellState.FLEEING
        #     return

        if self._nearestFood():
            self.state = CellState.GRABBING
            return

        # if self._nearestPrey() and self._movesCounter > 70:
        #     self.state = CellState.ATTACKING
        #     return
        
        self._move()
        hasSwitchedDirection: bool = False

        if (
            self._coordinates.x >= Settings.WIDTH - self._SIZE or 
            self._coordinates.y >= Settings.HEIGHT - self._SIZE or 
            self._coordinates.x <= 0 or self._coordinates.y <= 0
        ):
            self._direction = self.getRandomDirection()
            if self._coordinates.x >= Settings.WIDTH - self._SIZE: self._coordinates.x -= self._SPEED
            elif self._coordinates.x <= 0: self._coordinates.x += self._SPEED

            if (self._coordinates.y >= Settings.HEIGHT - self._SIZE): self._coordinates.y -= self._SPEED
            elif (self._coordinates.y <= 0): self._coordinates.y += self._SPEED

            hasSwitchedDirection = True

        if self._movesCounter % 30 == 0 and not hasSwitchedDirection:
            willChangeDirection: bool = randrange(0, 100) < 20
            if (willChangeDirection):
                self._direction = self.getRandomDirection()

    def _moveToCoordinates(self, coordinates: Coordinates):
        x0: int = self._coordinates.x
        y0: int = self._coordinates.y
        x1: int = coordinates.x
        y1: int = coordinates.y
    
        if x0 < x1 and y0 < y1: self._direction = Direction.DOWN_RIGHT
        elif x0 < x1 and y0 > y1: self._direction = Direction.UP_RIGHT
        elif x0 > x1 and y0 < y1: self._direction = Direction.DOWN_LEFT
        elif x0 > x1 and y0 > y1: self._direction = Direction.UP_LEFT
        elif y0 > y1:  self._direction = Direction.UP
        elif y0 < y1: self._direction = Direction.DOWN
        elif x0 > x1: self._direction = Direction.LEFT
        elif x0 < x1: self._direction = Direction.RIGHT

        self._move()

        return Coordinates.getDistanceToPoint(self._coordinates, coordinates) <= self._SIZE

    def _returnHome(self):
        if self._moveToCoordinates(self._getNearestCorner(True)): self.state = CellState.HOME

    def _grab(self):
        nearestFood: Food = self._nearestFood()
        if nearestFood:
            if self._moveToCoordinates(nearestFood._coordinates):
                self.eat(nearestFood)
        else: self.state = CellState.WANDERING
    
    def eat(self, entity: Entity):
        entity._terminate()
        self._energy = Settings.ENERGY
        self._score += 1
        if self._score == 2: self.state = CellState.RETURNING

    def _clone(self):
        size: int = self._SIZE
        speed: int = self._SPEED
        sense: int = self._SENSE 
        color: str = self.COLOR
        if (randrange(0, 100) < Settings.MUTATION_CHANCE):
            value = choice((-1, 1))
            match randrange(0, 3):
                case 0: size += value * Settings.SIZE_MUTATION
                case 1: speed += value * Settings.SPEED_MUTATION
                case _: sense += value * Settings.SENSE_MUTATION

        Cell(self._getNearestCorner(), size, color, speed, sense).spawn()


    def _reset(self):
        self._score = 0
        self._energy = Settings.ENERGY
        self._coordinates = self._getNearestCorner()
        self._direction = self.getRandomDirection(True)
        self._nearestCorner = None
        self._movesCounter = 0
        self.state = CellState.WANDERING
