from tkinter import Tk
from app.app import App

root = Tk()
root["bg"] = "#6DDE81"
root.title("Verificador de planta")
root.minsize(640, 400)

App(root)
root.mainloop()