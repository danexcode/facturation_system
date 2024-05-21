from maintk import window
from frames import login


window.title("Log in")
window.geometry("340x440")
window.configure(bg="#333333")

login.frame.pack()

window.mainloop()