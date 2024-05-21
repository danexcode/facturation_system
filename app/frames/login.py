import tkinter as tk
from maintk import window
from services import login


frame = tk.Frame(window, bg="#333333")

################ Components ###################
login_label = tk.Label(
    frame, text="Login", bg="#333333", fg="#FF3399", font=("Arial", 30))

username_label = tk.Label(
    frame, text="Usuario", bg="#333333", fg="#FFFFFF", font=("Arial", 16))

username_entry = tk.Entry(frame, font=("Arial", 16))

password_label = tk.Label(
    frame, text="Contraseña", bg="#333333", fg="#FFFFFF", font=("Arial", 16))

password_entry = tk.Entry(frame, show="*", font=("Arial", 16))

login_button = tk.Button(
    frame, text="Entrar", bg="#FF3399", fg="#FFFFFF", 
    font=("Arial", 16), command=(lambda : login.login(username_entry, password_entry)))

################ Posicioning ###################
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
