import tkinter
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Aplikacioni per detyren e trete")
root.iconbitmap('up.png')
root.geometry("470x400")


my_menu = Menu(root)
root.config(menu=my_menu)


def our_command():
	hide_frames()
	teksti = Label(root, text = "You clicked a dropdown menu..").pack()

def fk():
	hide_frames()
	korniza.pack(fill="both", expand=1)
	teksti = Label(korniza, text = "Universiteti i Prishtinës 'Hasan Prishtina'").pack()
	teksti = Label(korniza, text = "Departamenti: Inxhinieri Kompjuterike").pack()
	teksti = Label(korniza, text = "Viti 3").pack()
	teksti = Label(korniza, text = "Lënda: 'Siguria e Internetit'").pack()
	teksti = Label(korniza, text = "Profesori i lëndës: Blerim Rexha").pack()
	teksti = Label(korniza, text = "Asistenti i lëndës: Arbnor Halili").pack()
	teksti = Label(korniza, text="").pack()

def students():
	hide_frames()
	korniza.pack(fill="both", expand=1)
	teksti = Label(korniza, text="Studentet: ").pack()
	teksti = Label(korniza, text="Arianita Kabashi").pack()
	teksti = Label(korniza, text="Etnika Halili").pack()
	teksti = Label(korniza, text="Gretë Eshrefi").pack()
	teksti = Label(korniza, text="").pack()

def projekti():
	hide_frames()
	korniza.pack(fill="both", expand=1)
	teksti = Label(korniza, text="").pack()
	teksti = Label(korniza, text = "Projekti i trete ne lenden siguria e Internetit ka te beje me krijimin e nje Aplikacioni.").pack()
	teksti = Label(korniza, text = "Ky aplikacion duhet te permbaje nje meny per perzgjedhjen e opcioneve te ndryshme.").pack()
	teksti = Label(korniza, text = "Menyja duhet te jete e punuar si GUI duke perdorur vetem modulin tkinter te Python.").pack()
	teksti = Label(korniza, text="").pack()

def hide_frames():
	korniza.pack_forget()
	teksti.pack_forget()


#krijimi i menyse se pare "About"
about = Menu(my_menu)
my_menu.add_cascade(label="About", menu=about)
about.add_command(label="University", command=fk)
about.add_separator()
about.add_command(label="Students", command=students)
about.add_separator()
about.add_command(label="Project", command=projekti)

#krijimi i menyse se dyte "Show"
show_menu = Menu (my_menu)
my_menu.add_cascade(label="Show", menu=show_menu)
show_menu.add_command(label="Show passwords from Google Chrome", command=our_command)
about.add_separator()
show_menu.add_command(label="Show passwords from Mozilla Firefox", command=our_command)


korniza = Frame(root, width=400, height=400, bg="light blue")
teksti = Label(root)


butoni = Button(root, text="Dil nga programi", command=root.quit)
butoni.pack(side=tkinter.BOTTOM)

root.mainloop()





