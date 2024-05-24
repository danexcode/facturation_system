import tkinter as tk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Se hacen configuraciones iniciales a la ventana
        self.configure(bg="#333333")
        self.title("Tienda")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # Se crea el frame principal
        principal_container = tk.Frame(self, bg="yellow")
        principal_container.grid(padx=40, pady=50, sticky="news")
        
        # Se crea el diccionario donde van todos los frames
        self.all_frames = dict()
        
        # Se instancian cada uno de los frames creados,
        # se añaden al diccionario de frames
        # finalmente se colocan todos en el frame principal
        for F in (Frame_1, Frame_2):
            frame = F(principal_container, self)
            self.all_frames[F] = frame
            frame.grid(row=0, column=0, sticky="news")
            
        self.show_frame(Frame_1)
        
    
    def show_frame(self, container_called):
        frame = self.all_frames[container_called]
        
        """
        # creo que esto es como un event
        # Es un evento que se ejecuta al darle enter
        self.bind("<Return>", frame.saludarme)
        self.bind("<KP_Enter>", frame.saludarme)
        
        # esto es para resetear valores al cambiar de frame
        frame.entrada_usuario.set("")   
        """
        
        frame.tkraise()
            
class Frame_1(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="blue")
        
        # Widgets locales
        label = tk.Label(self, text="Frame 1, Hola Mundo!!")
        label.grid(row=0, column=0)
        
        # Widgets globales
        self.user_entry = tk.Entry(self)
        self.grid(row=1, column=0)
        
        # Botones
        login_button = tk.Button(self, text="login", command=self.login)
        next_button = tk.Button(
            self, text="siguiente", 
            command=(lambda : controller.show_frame(Frame_2)))
        
        login_button.grid(row=2, column=0)
        next_button.grid(row=3, column=0)
        
    
    def login(self, *args):
        print("Te logueaste")
        


class Frame_2():
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg="red")
        

