import tkinter as tk 
import json
from pageOne import pageone
from pageTwo import pagetwo
from navBar import NavBar

#################### Main Application Controller ####################

class Application(tk.Tk):
	def __init__(self, fullscreen):
		tk.Tk.__init__(self)
		container = tk.Frame(self)
		container.grid(columnspan=100)
		self.fullscreen = fullscreen
		self.startFullscreen()

		self.frames = {}
		self.frames2 = {}

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(3, weight=1)

		self.frameNames = ["pageone", "pagetwo"]
		i = 0
		for F in (pageone, pagetwo):
			frame = F(container, self)
			self.frames[F] = frame
			self.frames2[self.frameNames[i]] = F
			frame.grid(row=0, column=0, sticky="NSEW")
			i+=1

		self.show_frame("pageone")

	def show_frame(self, cont):
		frame = self.frames[self.frames2[cont]]
		frame.tkraise()
		self.frames2[cont].reinitialise(frame)

	def startFullscreen(self):
		if self.fullscreen:
			self.wm_attributes("-fullscreen", True)
			self.fullscreen = True
		elif not self.fullscreen:
			self.wm_attributes("-fullscreen", False)
			self.fullscreen = False

if __name__ == '__main__':
	fullscreen = True
	
	app = Application(fullscreen)
	app.protocol("WM_DELETE_WINDOW", exit)
	app.mainloop()
	print("Program ended...\n\n")