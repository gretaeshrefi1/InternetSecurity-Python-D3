from tkinter import *
# from Pillow import ImageTk,Image
import tkinter

root = Tk()
root.title("Aplikacioni per detyren e trete")
root.iconbitmap('up.png')
root.geometry("500x400")

# logo = ImageTk.PhotoImage(Image.open("up.png"))
# labela = Label(image=logo)
# labela.pack()

my_menu = Menu(root)
root.config(menu=my_menu)

def our_command():
	hide_frames()
	teksti = Label(root, text = "You clicked a dropdown menu..").pack()

def fk():
	hide_frames()
	file_new_frame.pack(fill="both", expand=1)
	teksti = Label(file_new_frame, text = "Universiteti i Prishtinës 'Hasan Prishtina'").pack()
	teksti = Label(file_new_frame, text = "Viti 3 ").pack()
	teksti = Label(file_new_frame, text = "Lënda: 'Siguria e Internetit'").pack()
	teksti = Label(file_new_frame, text = "Profesori i lëndës: Blerim Rexha").pack()
	teksti = Label(file_new_frame, text = "Asistenti i lëndës: Arbnor Halili").pack()

def students():
	hide_frames()
	file_new_frame.pack(fill="both", expand=1)
	teksti = Label(file_new_frame, text="Studentet: ").pack()
	teksti = Label(file_new_frame, text="Arianita Kabashi").pack()
	teksti = Label(file_new_frame, text="Etnika Halili").pack()
	teksti = Label(file_new_frame, text="Gretë Eshrefi").pack()

def projekti():
	hide_frames()
	file_new_frame.pack(fill="both", expand=1)
	teksti = Label(file_new_frame, text = "Projekti i trete ne lenden siguria e Internetit ka te beje me krijimin e nje Aplikacioni.").pack()
	teksti = Label(file_new_frame, text = "Ky aplikacion duhet te permbaje nje meny per perzgjedhjen e opcioneve te ndryshme.").pack()
	teksti = Label(file_new_frame, text = "Menyja duhet te jete e punuar si GUI duke perdorur vetem modulin tkinter te Python.").pack()

def hide_frames():
	file_new_frame.pack_forget()
	edit_cut_frame.pack_forget()


#create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="About", menu=file_menu)
file_menu.add_command(label="University", command=fk)
file_menu.add_separator()
file_menu.add_command(label="Students", command=students)
file_menu.add_separator()
file_menu.add_command(label="Project", command=projekti)


#create another menu
edit_menu = Menu (my_menu)
my_menu.add_cascade(label="Show", menu=edit_menu)
edit_menu.add_command(label="Show passwords from Google Chrome", command=our_command)
file_menu.add_separator()
edit_menu.add_command(label="Show passwords from Mozilla Firefox", command=our_command)


#create some frames
file_new_frame = Frame(root, width=400, height=400, bg="grey")
edit_cut_frame = Frame(root, width=400, height=400, bg="pink")


butoni = Button(root, text="Dil nga programi", command=root.quit)
butoni.pack(side=tkinter.BOTTOM)

root.mainloop()





