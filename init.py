from tkinter import Tk
from tkinter import Frame

def main():
	win = Tk()
	new_win = application(win)
	win.mainloop()

class application:
	def __init__(self,master):
		### Main Configuration ###
		self.master = master
		self.master.title("Clicker Window")
		self.master.resizable(False,False)
		bg_colour = "#E1341E" # red bg
		fg_colour = "#1ECBE1" #blue fg
		btn_colour = "#BD2C19" #red btn colour or #19AABD (blue)
		self.master.config(bg=bg_colour)

		### Frames ###
		self.counter_frame = Frame(self.master, bd=10, bg=bg_colour)
		self.counter_frame.pack()
		self.btn_frame = Frame(self.master, bd=10, bg=bg_colour)
		self.btn_frame.pack()

		
if __name__ == "__main__":
	main()