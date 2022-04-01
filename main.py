from classes.Cell import Cell
from classes.Settings import Settings
from classes.Simulation import Simulation
from classes.Statistics import Statistics
from classes.Chart import Visualizer, DatasetType

if __name__ == "__main__":
    Simulation.initialize()
    try: 
        while (Simulation.run()): pass
    except KeyboardInterrupt: print('Simulation has been interrupted.')
    else: print('Simulation has been finished.')
    finally: 
        Cell.endGeneration()
        Statistics.export()
        with open(Settings.PATH + 'settings.json', 'w+') as f:
            f.write(Settings.toJSON())
        Statistics.csvFile.close()
        for datasetType in DatasetType:
            Visualizer.draw(datasetType)