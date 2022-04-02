from enum import Enum
from typing import List, Tuple
from classes.Settings import Settings
from classes.Statistics import Statistics
import matplotlib.pyplot as plt

class Datasets(Enum):
    Population = 0
    Maximum = 1
    Minimum = 2
    Average = 3

class Visualizer:
    def draw() -> None:
        gen = [i for i in range(len(Statistics.all))]

        figures: List[plt.Figure] = []
        for dataset in Datasets:
            fig = plt.figure(num=dataset.name, figsize=(10, 5))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            match dataset:
                case Datasets.Maximum: x, y, z = Statistics.maximum()
                case Datasets.Minimum: x, y, z = Statistics.minimum()
                case Datasets.Average: x, y, z = Statistics.average()
                case _: x, y, z, w = Statistics.population()
            if dataset != Datasets.Population:
                labels = ['Size', 'Speed', 'Sense']
            else:
                labels = ['Population', 'Cloned', 'Died', 'Food']

            ax.plot(gen, x, label=labels[0])
            ax.plot(gen, y, label=labels[1])
            ax.plot(gen, z, label=labels[2])
            if dataset == Datasets.Population: ax.plot(gen, w, label=labels[3])
            ax.grid()
            ax.legend()
            
        plt.show()