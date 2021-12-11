import tkinter as tk 
import json
import style as s


class NavBar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        self.parent = parent
        self.fullscreen = self.controller.fullscreen

        button1 = tk.Button(self, text="Toggle Fullscreen", **s.STD_BUTTON_NAV, command=lambda: self.changeFullscreen())
        button1.grid(row=0, column=0, columnspan=25)
        button2 = tk.Button(self, text="Page One", **s.STD_BUTTON_NAV, command=lambda: self.controller.show_frame("pageone"))
        button2.grid(row=0, column=25, columnspan=25)
        button3 = tk.Button(self, text="Page Two", **s.STD_BUTTON_NAV, command=lambda: self.controller.show_frame("pagetwo"))
        button3.grid(row=0, column=50, columnspan=25)
        button4 = tk.Button(self, text="Exit", **s.STD_BUTTON_NAV, command=self.exit)
        button4.grid(row=0, column=75, columnspan=25)

    def changeFullscreen(self):
        if self.fullscreen:
            self.controller.wm_attributes("-fullscreen", False)
            self.fullscreen = False
        elif not self.fullscreen:
            self.controller.wm_attributes("-fullscreen", True)
            self.fullscreen = True

    def exit(self):
        self.parent.controller.destroy()