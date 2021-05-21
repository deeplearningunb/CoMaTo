from tkinter import *
import tkinter as tk


PlantList = [
    "Milho",
    "Soja",
]


class App:
    def __init__(self, master):
        self.fontePadrao = ("Arial", "10")
        self.firstContainer = tk.Frame(master)
        self.firstContainer["pady"] = 10
        self.firstContainer.pack()
        self.firstContainer["bg"] = "#6DDE81"

        self.select()

    # Components

    def select(self):
        self.selected_option = StringVar(root)
        self.selected_option.set("Selecione uma variedade de planta")

        self.plant_question = OptionMenu(
            self.firstContainer,
            self.selected_option,
            *PlantList,
            command=self.change_images,
        )
        self.plant_question["font"] = ("Arial", "10", "bold")
        self.plant_question.pack()

    # Functions

    def change_images(self, option):
        print(self.selected_option.get())
        return None


root = Tk()
root["bg"] = "#6DDE81"
root.title("Verificador de planta")
root.minsize(640, 400)

App(root)
root.mainloop()
