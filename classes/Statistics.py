from typing import Final, List, Tuple, Union
import statistics
import csv
from classes.Settings import Settings
import os

os.mkdir(Settings.PATH)

class Statistics:
    all: List = []
    csvFile = open(Settings.PATH + 'statistics.csv', 'a+')
    myWriter = csv.writer(csvFile, delimiter = ',')

    def last():
        return Statistics.all[-1]

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
                stat.avgSense, stat.lowestSize, stat.lowestSpeed, 
                stat.lowestSense, stat.highestSize, stat.highestSpeed, 
                stat.highestSense, len(stat.cloned), len(stat.died)
            ))
        Statistics.myWriter.writerow(fields)
        Statistics.myWriter.writerows(rows)

    def __init__(self, cells: Tuple, food: int) -> None:
        self.started: Final[Tuple] = cells
        self.food = food

        self.avgSize = round(statistics.mean(cell._SIZE for cell in self.started), 3)
        self.avgSpeed = round(statistics.mean(cell._SPEED for cell in self.started), 3)
        self.avgSense = round(statistics.mean(cell._SENSE for cell in self.started), 3)

        self.lowestSize = round(min(cell._SIZE for cell in self.started), 4)
        self.lowestSpeed = round(min(cell._SPEED for cell in self.started), 4)
        self.lowestSense = round(min(cell._SENSE for cell in self.started), 4)

        self.highestSize: int = round(max(cell._SIZE for cell in self.started), 4)
        self.highestSpeed: int = round(max(cell._SPEED for cell in self.started), 4)
        self.highestSense: int = round(max(cell._SENSE for cell in self.started), 4)

        self.cloned: Union[Tuple, None] = None
        self.died: Union[Tuple, None] = None

    def start(self) -> None:
        Statistics.all.append(self)

    def end(self, survived: Tuple, cloned: Tuple) -> None:
        self.cloned = cloned
        self.died = []
        for cell in survived:
            if cell not in self.started:
                self.died.append(cell)

    def log(self) -> None:
        print(f'Generation: {len(Statistics.all)}')
        print(f'Food: {self.food} Started: {len(self.started)} Cloned: {len(self.cloned)} Died: {len(self.died)}')
        print(f'Avg Size: {self.avgSize} Avg Speed: {self.avgSpeed} Avg Sense: {self.avgSense}')
        print(f'Lowest Size: {self.lowestSize} Lowest Speed: {self.lowestSpeed} Lowest Sense: {self.lowestSense}')
        print(f'Highest Size: {self.highestSize} Highest Speed: {self.highestSpeed} Highest Sense: {self.highestSense}\n')