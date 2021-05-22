from tkinter import *
import tkinter as tk
import os
from tkinter import filedialog
from PIL import ImageTk, Image
from . import prediction
from . import plant_list


class App():
    def __init__(self, master):
        self.bg = master['bg']
        self.fontePadrao = ("Arial", "10")

        self.firstContainer = tk.Frame(
            master, bg=self.bg, width=400, height=50)
        self.firstContainer.pack()
        self.firstContainer.propagate(0)
        self.secondContainer = tk.Frame(
            master, bg=self.bg, width=400, height=250)
        self.secondContainer.pack()
        self.secondContainer.propagate(0)

        self.thirdContainer = Frame(master, bg=self.bg, width=640, height=80)
        self.thirdContainer.pack()
        self.thirdContainer.propagate(0)

        self.header()
        self.content()
        self.footer()
    
    # Components
    def header(self):
        self.selected_option = StringVar()
        self.selected_option.set("Selecione uma variedade de planta")

        self.plant_question = OptionMenu(
            self.firstContainer, self.selected_option, *plant_list.keys(), command=self.change_images)
        self.plant_question["font"] = ("Arial", "10", "bold")
        self.plant_question.pack()

    def content(self):
        self.imagem = self.label(self.secondContainer, "", TOP)

    def footer(self):
        self.predict_message = self.label(self.thirdContainer, "", TOP)
        self.button_browse = self.button(
            self.thirdContainer, "Selecionar arquivo")

    def button(self, container, text):
        button = Button(container, pady=10, text=text)
        button.pack(side=BOTTOM)
        return button

    def label(self, container, text, side):
        lbl = Label(container, bg=self.bg, text=text, font=("Arial", "14", "bold"), fg="white")
        lbl.pack(side=side)
        return lbl

    # Functions

    def change_images(self, option):
        print(self.selected_option.get())
        self.photo = ImageTk.PhotoImage(Image.open(
            self.absolute_path(option.lower())))
        self.imagem['image'] = self.photo
        self.button_browse['command'] = self.fileDialog
        self.predict_message['text'] = ""

    def fileDialog(self):
        self.file = filedialog.askopenfile(initialdir="/home", title="Selecione a imagem que deseja verificar",
                                           filetypes=(("imagem", "*.jpg *.png *.jpeg"), ("All Files", "*.*")))
        if(self.file):
            self.photo = ImageTk.PhotoImage(Image.open(self.file.name))
            self.imagem['image'] = self.photo
            pred, pred_percentage = prediction.Prediction(
                self.file.name, plant_list[self.selected_option.get()]).predict()
            self.predict_message['text'] = f"Resposta: {pred}\nProbabilidade: {pred_percentage}"

    def absolute_path(self, img_name):
        this_path = os.path.dirname(__file__)
        file_path = f"images/{img_name}.jpg"
        return os.path.join(this_path, file_path)
