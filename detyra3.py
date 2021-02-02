from tkinter import *

root = Tk()
root.title("Aplikacioni per detyren e trete")
root.geometry("400x400")



def show():
	myLabel = Label(root, text=clicked.get()).pack()



clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked,"Monday","greta", "Tuesday", "Wednesday")
drop.pack()



root.mainloop()
