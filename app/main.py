from tkinter import ttk
from app import App

window = App()

style = ttk.Style(window)
window.tk.call("source", "theme/forest-light.tcl")
window.tk.call("source", "theme/forest-dark.tcl")
style.theme_use("forest-dark")

window.mainloop()
