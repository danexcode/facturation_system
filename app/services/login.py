from tkinter import messagebox

def login(username_entry, password_entry):
    username = "danifanton"
    password = "admin"
    if (username_entry.get() == username and password_entry.get() == password):
        messagebox.showinfo(title="Login Success", message="Te logueaste de forma correcta")
    else:
        messagebox.showinfo(title="Error", message="Datos invalidos")