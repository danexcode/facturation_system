from tkinter import ttk
from app import App

window = App()

path = r"C:/Users/User/Documents/cursos/proyecto_db/app/theme/"

style = ttk.Style(window)
window.tk.call("source", path + "forest-light.tcl")
window.tk.call("source", path + "forest-dark.tcl")
style.theme_use("forest-dark")

window.mainloop()
