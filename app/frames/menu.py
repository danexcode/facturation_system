import tkinter as tk
from tkinter import ttk

from .store import Store


class Menu(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.columnconfigure(index=0, minsize=250)
        self.columnconfigure(index=1, minsize=250)
        
        
        # Labels
        menu_label = ttk.Label(
            self, text="Bienvenido!", font=("Arial", 30))
        menu_label.grid(
            row=0, column=0, columnspan=2, pady=(40,120))
        
        # Buttons
        store_button = ttk.Button(
            self, text="Tienda", command=(lambda : controller.show_frame(Store)))
        store_button.grid(row=1, column=0)
        
        inventory_button = ttk.Button(self, text="Inventario")
        inventory_button.grid(row=1, column=1)