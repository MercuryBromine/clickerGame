from tkinter import Tk
from tkinter import Frame
from tkinter import IntVar
from tkinter import Label
from tkinter import Button

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
		bg_colour = "#03ffe6" # blue bg 
		fg_colour = "#ff3e03" #red fg
		btn_bg_colour = "#d91200" #red btn 
		btn_fg_colour = "#00ff55" #blue fg
		self.master.config(bg=bg_colour)

		### Frames ###
		self.counter_frame = Frame(self.master, bd=10, bg=bg_colour)
		self.counter_frame.pack()
		self.btn_frame = Frame(self.master, bd=10, bg=bg_colour)
		self.btn_frame.pack()

		### Contents ### 

		counter = IntVar()
		self.counter = Label(self.counter_frame, textvariable=counter, bg=bg_colour, fg=fg_colour, font=("Open Sans", 20))
		self.counter.grid(row=0,column=0)

		self.btn = Button(self.btn_frame, text="Click me", font=("Open Sans", 12), bg=btn_bg_colour, fg=btn_fg_colour)
		self.btn.grid(row=0,column=0)

		
if __name__ == "__main__":
	main()