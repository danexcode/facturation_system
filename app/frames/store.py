import tkinter as tk
from tkinter import ttk
from services.product import Product


class Store(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        self.name = "Store"
        self.controller = controller
        self.product_service = Product()
        
        ### Options Frame ###
        options_frame = ttk.Frame(self)
        options_frame.grid(row=0, column=0)
        
        # Buttons
        back_button = ttk.Button(
            options_frame, text="Regresar",
            command=(lambda: controller.show_frame("Store", "Menu")))
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
        
        combo_list = [""]
        self.product_combobox = ttk.Combobox(widgets_frame, state="readonly", values=combo_list)
        self.product_combobox.current(0)
        self.product_combobox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        
        self.amount_spinbox = ttk.Spinbox(widgets_frame, from_=0, to=1000)
        self.amount_spinbox.insert(0, "1")
        self.amount_spinbox.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        
        #Buttons
        add_button = ttk.Button(
            widgets_frame, text="Añadir",
            command=self.add_product)
        add_button.grid(row=4, column=0, padx=10, pady=(100,10), sticky="ew")
        
        
        ### Table Frame ###
        table_frame = ttk.Frame(self)
        table_frame.grid(row=0, column=1, rowspan=2)
        
        preview_cols = ["Producto", "Precio", "Cantidad", "Subtotal"]
        self.table_treeview = ttk.Treeview(
            table_frame, show="headings", columns=preview_cols, height=8)
        self.table_treeview.column("Producto", width=100, anchor="center")
        self.table_treeview.column("Precio", width=100, anchor="center")
        self.table_treeview.column("Cantidad", width=100, anchor="center")
        self.table_treeview.column("Subtotal", width=100, anchor="center")
        self.table_treeview.grid(row=0, column=0, sticky="ns")
        for col_name in preview_cols:
            self.table_treeview.heading(column=col_name, text=col_name, anchor=tk.CENTER)
        
        total_cols = ["Vacio", "Total"]
        self.total_treeview = ttk.Treeview(
            table_frame, show="headings", columns=total_cols, height=1)
        self.total_treeview.column("Vacio", width=300)
        self.total_treeview.column("Total", width=100, anchor="center")
        self.total_treeview.grid(row=1, column=0, sticky="s")
        self.total_treeview.heading("Vacio", text="")
        self.total_treeview.heading("Total", text="Total", anchor="center")
        self.total_price = self.total_treeview.insert("", tk.END, values=("", "0"))
        
        purshased_button = ttk.Button(
            table_frame, text="Procesar Compra")
        purshased_button.grid(row=2, column=0, pady=(10, 0), sticky="w")
    
    
    def load_products(self):
        print(self.name)
        #service = Product()
        names = self.product_service.get_products_names()
        self.product_combobox["values"] = names
        self.product_combobox.current(0)
    
    
    def add_product(self):
        products = self.product_combobox["values"]
        current = self.product_combobox.current()
        product = products[current]
        
        # (id, category_id, name, stock, price)
        product_info = self.product_service.get_product(product)
        
        amount = self.amount_spinbox.get()
        amount = int(amount)
        price = product_info[4]
        subtotal = price * amount
        value_tuple = (product, price, amount, subtotal)
        self.table_treeview.insert("", tk.END, values=value_tuple)
        
        total = self.get_total()
        self.total_treeview.item(self.total_price, values=("", total))
        
    
    def get_total(self):
        children = self.table_treeview.get_children()
        total = 0.0
        for child in children:
            reg = self.table_treeview.item(child)
            total += float(reg["values"][3])
        return total
        