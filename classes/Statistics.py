from enum import Enum, auto
from typing import Final, List, Tuple, Union
import statistics
import csv
from classes.Settings import Settings
import os

os.mkdir(Settings.PATH)

class Dataset(Enum):
    AVG_SIZE = auto()
    AVG_SPEED = auto()
    AVG_SENSE = auto()
    MIN_SIZE = auto()
    MIN_SPEED = auto()
    MIN_SENSE = auto()
    MAX_SIZE = auto()
    MAX_SPEED = auto()
    MAX_SENSE = auto()
    POPULATION = auto()
    FOOD = auto()
    CLONED = auto()
    DIED = auto()
    EATEN = auto()

class Statistics:
    all: List = []
    csvFile = open(Settings.PATH + 'statistics.csv', 'a+')
    myWriter = csv.writer(csvFile, delimiter = ',')

    def export() -> None:
        fields = (
            'Started', 'Food', 'Avg Size', 'Avg Speed', 
            'Avg Sense', 'Lowest Size', 'Lowest Speed', 
            'Lowest Sense', 'Highest Size', 'Highest Speed', 
            'Highest Sense', 'Cloned', 'Died'
        )
        rows = []
        for stat in Statistics.all:
            stat: Statistics
            rows.append((
                len(stat.started), stat.food, round(stat.avgSize, 3), stat.avgSpeed, 
                stat.avgSense, stat.minSize, stat.minSpeed, 
                stat.minSense, stat.maxSize, stat.maxSpeed, 
                stat.maxSense, len(stat.cloned), len(stat.died)
            ))
        Statistics.myWriter.writerow(fields)
        Statistics.myWriter.writerows(rows)

    def getByDataset(dataset: Dataset):
        match dataset:
            case Dataset.AVG_SIZE: return [stat.avgSize / Settings.SIZE for stat in Statistics.all]
            case Dataset.AVG_SPEED: return [stat.avgSpeed / Settings.SPEED for stat in Statistics.all]
            case Dataset.AVG_SENSE: return [stat.avgSense / Settings.SENSE for stat in Statistics.all]
            case Dataset.MIN_SIZE: return [stat.minSize / Settings.SIZE for stat in Statistics.all]
            case Dataset.MIN_SPEED: return [stat.minSpeed / Settings.SPEED for stat in Statistics.all]
            case Dataset.MIN_SENSE: return [stat.minSense / Settings.SENSE for stat in Statistics.all]
            case Dataset.MAX_SIZE: return [stat.maxSize / Settings.SIZE for stat in Statistics.all]
            case Dataset.MAX_SPEED: return [stat.maxSpeed / Settings.SPEED for stat in Statistics.all]
            case Dataset.MAX_SENSE: return [stat.maxSense / Settings.SENSE for stat in Statistics.all]
            case Dataset.POPULATION: return [len(stat.started) for stat in Statistics.all]
            case Dataset.FOOD: return [stat.food for stat in Statistics.all]
            case Dataset.CLONED: return [len(stat.cloned) for stat in Statistics.all]
            case Dataset.DIED: return [len(stat.died) for stat in Statistics.all]
            case _: return [len(stat.eaten) for stat in Statistics.all]

    def __init__(self, cells: Tuple, food: int) -> None:
        self.started: Final[Tuple] = cells
        self.food = food

        self.avgSize = round(statistics.mean(cell._SIZE for cell in self.started), 3)
        self.avgSpeed = round(statistics.mean(cell._SPEED for cell in self.started), 3)
        self.avgSense = round(statistics.mean(cell._SENSE for cell in self.started), 3)

        self.minSize = round(min(cell._SIZE for cell in self.started), 4)
        self.minSpeed = round(min(cell._SPEED for cell in self.started), 4)
        self.minSense = round(min(cell._SENSE for cell in self.started), 4)

        self.maxSize: int = round(max(cell._SIZE for cell in self.started), 4)
        self.maxSpeed: int = round(max(cell._SPEED for cell in self.started), 4)
        self.maxSense: int = round(max(cell._SENSE for cell in self.started), 4)

        self.cloned: Union[Tuple, None] = None
        self.died: Union[Tuple, None] = None
        self.eaten: List = []

    def start(self) -> None:
        Statistics.all.append(self)

    def end(self, survived: Tuple, cloned: Tuple) -> None:
        self.cloned = cloned
        self.died = []
        for cell in self.started:
            if cell not in survived:
                self.died.append(cell)

    def log(self) -> None:
        print(f'Generation: {len(Statistics.all)} Food: {self.food} ')
        print(f'Started: {len(self.started)} Cloned: {len(self.cloned)} Died: {len(self.died)} Eaten: {len(self.eaten)}')
        print(f'Avg Size: {self.avgSize} Avg Speed: {self.avgSpeed} Avg Sense: {self.avgSense}')
        print(f'Lowest Size: {self.minSize} Lowest Speed: {self.minSpeed} Lowest Sense: {self.minSense}')
        print(f'Highest Size: {self.maxSize} Highest Speed: {self.maxSpeed} Highest Sense: {self.maxSense}\n')