import tkinter as tk
from tkinter import ttk


class Store(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        ### Options Frame ###
        options_frame = ttk.Frame(self)
        options_frame.grid(row=0, column=0)
        
        # Buttons
        back_button = ttk.Button(options_frame, text="Regresar")
        back_button.grid(row=0, column=0, padx=(0,30), sticky="w")
        
        sales_button = ttk.Button(options_frame, text="Ver ventas")
        sales_button.grid(row=0, column=1, padx=(30,0), sticky="e")
        
        
        ### Widgets Frame ###
        widgets_frame = ttk.LabelFrame(self, text="Añadir producto")
        widgets_frame.grid(row=1, column=0, padx=20, pady=20)
        widgets_frame.columnconfigure(index=0, minsize=250)
        
        # Labels
        product_label = ttk.Label(widgets_frame, text="Seleccione el producto")
        product_label.grid(row=0, column=0, padx=5, pady=(15,0), sticky="ew")
        
        amount_label = ttk.Label(widgets_frame, text="Indique la cantidad")
        amount_label.grid(row=2, column=0, padx=5, pady=(15,0), sticky="ew")
        
        # Entries
        combo_list = ["Azucar 1kg", "Leche 1.5Lts"]
        product_combobox = ttk.Combobox(widgets_frame, state="readonly", values=combo_list)
        product_combobox.current(0)
        product_combobox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        
        amount_spinbox = ttk.Spinbox(widgets_frame, from_=0, to=1000)
        amount_spinbox.insert(0, "1")
        amount_spinbox.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        
        #Buttons
        add_button = ttk.Button(widgets_frame, text="Añadir")
        add_button.grid(row=4, column=0, padx=10, pady=(100,10), sticky="ew")
        
        
        ### Table Frame ###
        table_frame = ttk.Frame(self)
        table_frame.grid(row=0, column=1, rowspan=2)
        
        preview_cols = ["Producto", "Precio", "Cantidad", "Subtotal"]
        table_treeview = ttk.Treeview(
            table_frame, show="headings", columns=preview_cols, height=8)
        table_treeview.column("Producto", width=100)
        table_treeview.column("Precio", width=100)
        table_treeview.column("Cantidad", width=100)
        table_treeview.column("Subtotal", width=100)
        table_treeview.grid(row=0, column=0, sticky="ns")
        
        total_cols = ["Total", "Price"]
        total_treeview = ttk.Treeview(
            table_frame, show="headings", columns=total_cols, height=1)
        total_treeview.column("Total", width=300)
        total_treeview.column("Price", width=100)
        total_treeview.grid(row=1, column=0, sticky="s")
        
        purshased_button = ttk.Button(table_frame, text="Procesar Compra")
        purshased_button.grid(row=2, column=0, pady=(10, 0), sticky="w")
        
        