from gui import ChessGUI
from search import *
import tkinter as tk
from model import Model
from controller import Controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        # create a model
        model = Model()

        # create a view and place it on the root window
        view = ChessGUI(self)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()
