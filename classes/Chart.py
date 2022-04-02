from classes.Settings import Settings
from classes.Statistics import Statistics
from enum import Enum
import matplotlib.pyplot as plt

class DatasetType(Enum):
    AVERAGE = 0
    LOWEST = 1
    HIGHEST = 2
    CELLS = 3
    FOOD = 4

class Visualizer:
    def draw(datasetType: DatasetType) -> None:
        gen = [i for i in range(len(Statistics.all))]
        x = []
        y = []
        z = []

        match datasetType:
            case DatasetType.AVERAGE: 
                x = [statistic.avgSize for statistic in Statistics.all]
                y = [statistic.avgSpeed for statistic in Statistics.all]
                z = [statistic.avgSense for statistic in Statistics.all]
            case DatasetType.LOWEST:
                x = [statistic.lowestSize for statistic in Statistics.all]
                y = [statistic.lowestSpeed for statistic in Statistics.all]
                z = [statistic.lowestSense for statistic in Statistics.all]
            case DatasetType.HIGHEST:
                x = [statistic.highestSize for statistic in Statistics.all]
                y = [statistic.highestSpeed for statistic in Statistics.all]
                z = [statistic.highestSense for statistic in Statistics.all]
            case DatasetType.CELLS:
                x = [len(statistic.started) for statistic in Statistics.all]
                y = [len(statistic.cloned) for statistic in Statistics.all]
                z = [len(statistic.died) for statistic in Statistics.all]
            case DatasetType.FOOD:
                x = [statistic.food for statistic in Statistics.all]

        if (Settings.SHOW_RELATIVE_TO_INITIALS and datasetType != DatasetType.FOOD):
            x = [x[i] / Settings.SIZE for i in range(len(x))]
            y = [y[i] / Settings.SPEED for i in range(len(y))]
            z = [z[i] / Settings.SENSE for i in range(len(z))]

        labels = ['Size', 'Speed', 'Sense']
        if datasetType == DatasetType.CELLS:
            labels = ['Cells', 'Cloned', 'Died']
        
        if (datasetType != DatasetType.FOOD):
            plt.plot(gen, x, label=labels[0])
            plt.plot(gen, y, label=labels[1])
            plt.plot(gen, z, label=labels[2])
        else:
            plt.plot(gen, x)
    
        plt.xticks(rotation = 25)
        plt.xlabel('Generation')
        plt.ylabel(datasetType.name)
        plt.grid()
        if (datasetType != DatasetType.FOOD): plt.legend()
        plt.show()