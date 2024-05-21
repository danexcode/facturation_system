import tkinter as tk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.configure(bg="#333333")
        self.title("Tienda")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        principal_container = tk.Frame(self, bg="yellow")
        principal_container.grid(padx=40, pady=50, sticky="news")
        
        self.all_frames = dict()
        
        for F in (Frame_1, Frame_2):
            frame = F(principal_container, self)
            self.all_frames[F] = frame
            frame.grid(row=0, column=0, sticky="news")
            
        self.show_frame(Frame_1)
        
    
    def show_frame(self, container):
        pass
            
            
class Frame_1():
    pass


class Frame_2():
    pass
        

