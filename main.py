from classes.App import App
from classes.Cell import Cell
from classes.Settings import Settings
from classes.Simulation import Simulation
from classes.Statistics import Statistics

if __name__ == "__main__":
    Simulation.initialize()
    try: 
        while (Simulation.run()): pass
    except KeyboardInterrupt: print('Simulation has been interrupted.')
    else: print('Simulation has been finished.')

    Cell.endGeneration()
    Statistics.export()
    with open(Settings.PATH + 'settings.json', 'w+') as f:
        f.write(Settings.toJSON())
    Statistics.csvFile.close()
    # Visualizer.draw()
    app = App()
    app.plot()
    app.mainloop()