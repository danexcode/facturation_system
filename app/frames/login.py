from tkinter import ttk
from tkinter import messagebox
from database.connection import Connection

db_service = Connection.get_instance()


class Login(ttk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        self.name = "Login"
        self.controller = controller
        self.columnconfigure(index=0, minsize=150)
        self.columnconfigure(index=1, minsize=150)
        
        
        # Widgets locales (Labels)
        
        login_label = ttk.Label(
            self, text="Login", font=("Arial", 30))
        login_label.grid(row=0, column=0, columnspan=2, pady=40)
        
        username_label = ttk.Label(
            self, text="Usuario", font=("Arial", 16))
        username_label.grid(row=1, column=0, padx=5)
        
        password_label = ttk.Label(
            self, text="Contraseña", font=("Arial", 16))
        password_label.grid(row=2, column=0, padx=5)
        
        
        # Widgets globales (Entries)
        
        self.username_entry = ttk.Entry(self, font=("Arial", 16))
        self.username_entry.grid(row=1, column=1, pady=20)
        
        self.password_entry = ttk.Entry(self, show="*", font=("Arial", 16))
        self.password_entry.grid(row=2, column=1, pady=20)
        
        # Botones
        
        login_button = ttk.Button(
            self, text="Entrar", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=30)
        
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"User: {username} Pass: {password}")
        
        try:
            db_service.connect(username, password)  
            
            self.controller.show_frame("Login", "Menu")
            
        #DatabaseError    
        #ProgrammingError
        except:
            messagebox.showerror(title="Error", message="Datos invalidos")
        
               
