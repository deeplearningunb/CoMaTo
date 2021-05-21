from tkinter import *
import tkinter as tk
import os
from tkinter import filedialog
from PIL import ImageTk, Image

PlantList = [
"Milho",
"Soja",
] 

class App():
    def __init__(self, master):
        self.fontePadrao = ("Arial", "10")
        self.firstContainer = tk.Frame(master)
        self.firstContainer["pady"] = 10
        self.firstContainer.pack()
        self.firstContainer['bg'] = '#6DDE81'


        self.secondContainer = tk.Frame(master)
        self.secondContainer['padx'] = 20
        self.secondContainer['bg'] = '#6DDE81'
        self.secondContainer.pack()
        

        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 10
        self.thirdContainer["pady"] = 10
        self.thirdContainer.pack()
        self.thirdContainer['bg'] = '#6DDE81'

        self.select()
        self.middle_img()
        self.button()

    # Components

    def select(self):
        self.selected_option = StringVar(root)
        self.selected_option.set("Selecione uma variedade de planta")

        self.plant_question = OptionMenu(self.firstContainer, self.selected_option, *PlantList, command=self.change_images)
        self.plant_question["font"] = ("Arial", "10", "bold")
        self.plant_question.pack()

    def middle_img(self):
        self.imagem = Label(self.secondContainer)
        self.imagem['bg'] = "#6DDE81"
        self.imagem.pack()

    def button(self):
        self.button_browse = Button(self.thirdContainer)
        self.button_browse['text'] = 'Browse a File'
        self.button_browse.pack(side = LEFT)

    # Functions

    def change_images(self, option):
        print(self.selected_option.get())
        self.photo = ImageTk.PhotoImage(Image.open(self.absolute_path(f"{option.lower()}")))
        self.imagem['image'] = self.photo
        self.button_browse['command'] = self.fileDialog
        return None
        
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/home", title = "Selecione a imagem que deseja verificar", filetypes = (("jpeg", "*.jpg"), ("All Files", "*.*")))

    def absolute_path(self, img_name):
        this_path = os.path.dirname(__file__)
        file_path = f"images/{img_name}.jpg"
        return os.path.join(this_path, file_path)


root = Tk()
root["bg"] = "#6DDE81"
root.title("Verificador de planta")
root.minsize(640, 400)

App(root)
root.mainloop()