from tkinter import Tk
from app.app import App

root = Tk()
root["bg"] = "#6DDE81"
root.title("Verificador de doença de planta")
root.geometry('640x400')
root.resizable(width=0, height=0)

App(root)
root.mainloop()