from datetime import datetime
from classes.Simulation import Simulation

if __name__ == "__main__":
    Simulation.initialize()
    while (Simulation.run()): pass
    print("Simulation ended")