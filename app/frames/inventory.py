import tkinter as tk
from tkinter import ttk

from services.product import Product


class Inventory(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        self.name = "Inventory"
        self.controller = controller
        self.product_service = Product()
        
        ### Options Frame ###
        options_frame = ttk.Frame(self)
        options_frame.grid(row=0, column=0)
        
        # Buttons
        back_button = ttk.Button(
            options_frame, text="Regresar",
            command=(lambda: controller.show_frame("Inventory", "Menu")))
        back_button.grid(row=0, column=0, padx=(0,30), sticky="w")
        
        sales_button = ttk.Button(options_frame, text="Ver ventas")
        sales_button.grid(row=0, column=1, padx=(30,0), sticky="e")
        
        
        ### Widgets Frame ###
        widgets_frame = ttk.LabelFrame(self, text="Productos")
        widgets_frame.grid(row=1, column=0, padx=20, pady=20)
        widgets_frame.columnconfigure(index=0, minsize=250)
        
        # Labels
        
        # Entries
        
        #Buttons
        add_button = ttk.Button(widgets_frame, text="Añadir")
        add_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        
        add_button = ttk.Button(widgets_frame, text="Modificar")
        add_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        create_button = ttk.Button(widgets_frame, text="Crear")
        create_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        
        erase_button = ttk.Button(
            widgets_frame, text="Eliminar")
        erase_button.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        
        create_category_button = ttk.Button(widgets_frame, text="Crear Categoria")
        create_category_button.grid(row=4, column=0, padx=10, pady=(80,10), sticky="ew")
        
        
        ### Table Frame ###
        table_frame = ttk.Frame(self)
        table_frame.grid(row=0, column=1, rowspan=2)
        
        preview_cols = ["ID", "Nombre", "Categoria", "Precio", "Stock"]
        self.table_treeview = ttk.Treeview(
            table_frame, show="headings", columns=preview_cols, height=14)
        for col_name in preview_cols:
            self.table_treeview.column(column=col_name, width=100, anchor="center")
            self.table_treeview.heading(column=col_name, text=col_name, anchor=tk.CENTER)
        self.table_treeview.grid(row=0, column=0, sticky="ns")
        
    
    def load_products(self):
        # (id, name, category, price, stock)
        children = self.table_treeview.get_children()
        for child in children:
            self.table_treeview.delete(child)
        products = self.product_service.get_products()
        for product in products:
            self.table_treeview.insert("", tk.END, values=product)
                        
        