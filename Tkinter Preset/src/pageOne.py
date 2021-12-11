import tkinter as tk 
import json
from navBar import NavBar
import style as s

#################### New Project Page ####################
class pageone(tk.Frame):
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        tk.Frame.__init__(self, parent)

        self.navBar = NavBar(self, controller)
        self.navBar.grid(row=0, column=0, columnspan=20)


        self.label1 = tk.Label(self, text="This is page one!", font=s.TITLE_FONT)
        self.label1.grid(row=1, column=0, columnspan=20, **s.STD_PAD)

    def reinitialise(self):
        print()