from datetime import datetime
from typing import Final, List, Tuple, Union
import statistics
import csv

from classes.Settings import Settings

class Traits:
    def __init__(self, size, speed, sense):
        self.size = size
        self.speed = speed
        self.sense = sense

    def asTuple(self):
        return self.size, self.speed, self.sense

    def comparedToInitial(self):
        return self.size / Settings.SIZE, self.speed / Settings.SPEED, self.sense / Settings.SENSE


class Statistics:
    all: List = []
    filename: Final[str] = f'./data/{datetime.now()}.csv'
    csvFile = open(filename, 'a')
    myWriter = csv.writer(csvFile, delimiter = ',')
    first = True

    def __init__(self, cells: Tuple, food: int) -> None:
        self.started: Final[Tuple] = cells
        self.survived: Union[Tuple, None] = None
        self.survived: Union[Tuple, None] = None
        self.food = food

    def start(self) -> None:
        Statistics.all.append(self)

    def end(self, survived: Tuple, cloned: Tuple) -> None:
        self.survived = survived
        self.cloned = cloned

    def died(self) -> List:
        died = []
        for cell in self.started:
            if cell not in self.survived:
                died.append(cell)
        return died

    def avgTraits(self) -> Traits:
        avgSize: int = statistics.mean(cell._SIZE for cell in self.started)
        avgSpeed: int = statistics.mean(cell._SPEED for cell in self.started)
        avgSense: int = statistics.mean(cell._SENSE for cell in self.started)
        return Traits(avgSize, avgSpeed, avgSense)

    def lowestTraits(self) -> Traits:
        lowestSize: int = min(cell._SIZE for cell in self.started)
        lowestSpeed: int = min(cell._SPEED for cell in self.started)
        lowestSense: int = min(cell._SENSE for cell in self.started)
        return Traits(lowestSize, lowestSpeed, lowestSense)

    def highestTraits(self) -> Traits:
        highestSize: int = max(cell._SIZE for cell in self.started)
        highestSpeed: int = max(cell._SPEED for cell in self.started)
        highestSense: int = max(cell._SENSE for cell in self.started)
        return Traits(highestSize, highestSpeed, highestSense)

    def log(self) -> None:
        print(f"Generation: {len(Statistics.all)}")
        print(f"Started: {len(self.started)}")
        print(f"Survived: {len(self.survived)}")
        print(f"Cloned: {len(self.cloned)}")
        print(f"Died: {len(self.died())}")
        print(f"Average traits:")
        print(self.avgTraits().asTuple())
        print(self.avgTraits().comparedToInitial())
        print(f"Lowest traits:")
        print(self.lowestTraits().asTuple())
        print(self.lowestTraits().comparedToInitial())
        print(f"Highest traits:")
        print(self.highestTraits().asTuple())
        print(self.highestTraits().comparedToInitial())
        print(f"Food: {self.food}")
        print("\n")

    def asTuple(self) -> Tuple:
        avgTraits: Tuple[float] = self.avgTraits().comparedToInitial()
        lowestTraits: Tuple[float] = self.lowestTraits().comparedToInitial()
        highestTraits: Tuple[float] = self.highestTraits().comparedToInitial()

        return (
            len(Statistics.all), 
            len(self.started), 
            len(self.survived), 
            len(self.cloned), 
            len(self.died()), 
            avgTraits[0], 
            avgTraits[1], 
            avgTraits[2], 
            lowestTraits[0],
            lowestTraits[1],
            lowestTraits[2],
            highestTraits[0],
            highestTraits[1],
            highestTraits[2],
            self.food
        )
    
    def appendToCSV(self) -> None:
        if (Statistics.first):
            Statistics.myWriter.writerow((
                'Generation', 
                'Started', 
                'Survived', 
                'Cloned', 
                'Died', 
                'Avg Size',
                'Avg Speed',
                'Avg Sense', 
                'Lowest Size',
                'Lowest Speed',
                'Lowest Sense',
                'Highest Size',
                'Highest Speed',
                'Highest Sense',
                'Food'
            ))
            Statistics.first = False
        row = self.asTuple()
        Statistics.myWriter.writerow(row)