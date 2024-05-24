from tkinter import ttk
from .store import Store
from .inventory import Inventory


class Menu(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.columnconfigure(index=0, minsize=250)
        self.columnconfigure(index=1, minsize=250)
        self.configure(width="1000", height="700")
        
        self.name = "Menu"
        self.controller = controller
        
        # Labels
        menu_label = ttk.Label(
            self, text="Bienvenido!", font=("Arial", 30))
        menu_label.grid(
            row=0, column=0, columnspan=2, pady=(40,120))
        
        # Buttons
        store_button = ttk.Button(
            self, text="Tienda", command=self.goto_store)
        store_button.grid(row=1, column=0)
        
        inventory_button = ttk.Button(
            self, text="Inventario",
            command=self.goto_inventory)
        inventory_button.grid(row=1, column=1)
    
        
    def goto_inventory(self):
        Inventory.load_products(self.controller.all_frames["Inventory"])
        self.controller.show_frame("Menu", "Inventory")
        
    def goto_store(self):
        Store.load_products(self.controller.all_frames["Store"])
        self.controller.show_frame("Menu", "Store")
        