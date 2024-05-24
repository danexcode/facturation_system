import tkinter as tk
from tkinter import ttk

from frames.login import Login
from frames.menu import Menu
from frames.store import Store
from frames.inventory import Inventory


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Se hacen configuraciones iniciales a la ventana
        self.title("Tienda")
        self.geometry("1080x600")
        #self.columnconfigure(0, weight=1)
        #self.rowconfigure(0, weight=1)


        # Se crea el frame principal
        principal_container = ttk.Frame(self)
        #principal_container.grid(padx=40, pady=50, sticky="news")
        principal_container.pack(expand=True)
        
        #Se crea el cursor de la base de datos
        self.cursor = ""
        
        # Se crea el diccionario donde van todos los frames
        self.all_frames = dict()
        
        # Se instancian cada uno de los frames creados,
        # se añaden al diccionario de frames
        # finalmente se colocan todos en el frame principal
        for F in (Login, Menu, Store, Inventory):
            frame = F(principal_container, self)
            self.all_frames[frame.name] = frame
            #frame.grid(row=0, column=0, sticky="news")
            
        self.show_frame("", "Login")
        
    
    def show_frame(self, current, container_called):
        if current:
            current_frame = self.all_frames[current]
            current_frame.pack_forget()
        frame = self.all_frames[container_called]
        frame.pack(expand=True)
        """
        # creo que esto es como un event
        # Es un evento que se ejecuta al darle enter
        self.bind("<Return>", frame.saludarme)
        self.bind("<KP_Enter>", frame.saludarme)
        
        # esto es para resetear valores al cambiar de frame
        frame.entrada_usuario.set("")   
        """
        #frame.tkraise()
        