import tkinter as tk
from typing import List
from classes.Statistics import Dataset, Statistics
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class App(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.title('Statistics')

        self.checkVars: List[tk.IntVar] = [tk.IntVar() for _ in enumerate(Dataset)]
        self.checkButtons: List[tk.Checkbutton] = [tk.Checkbutton(self, text=dataset.name, variable=self.checkVars[i], command=self.plot) for i, dataset in enumerate(Dataset)]
        for index, checkButton in enumerate(self.checkButtons):
            checkButton.grid(row=index, column=0)

        self.checkVars[Dataset['AVG_SIZE'].value-1].set(1)
        self.checkVars[Dataset['AVG_SPEED'].value-1].set(1)
        self.checkVars[Dataset['AVG_SENSE'].value-1].set(1)

    def plot(self) -> None:
        length = len(Dataset)

        fig = Figure(figsize=(10, 4.8))
        plt = fig.add_subplot(111)

        gen = [i for i in range(len(Statistics.all))]

        for i, checkVar in enumerate(self.checkVars):
            if checkVar.get() == 1:
                dataset = Dataset(i+1)
                plt.plot(gen, Statistics.getByDataset(dataset), label=dataset.name)
        
        plt.legend()
        plt.grid()

        canvas = FigureCanvasTkAgg(fig, master=self)  
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar=False)
        toolbar.update()
        canvas.get_tk_widget().grid(row=0, column=1, rowspan=length)
        toolbar.grid(row=length, column=0, columnspan=2)

