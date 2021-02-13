import os
import sqlite3
import win32crypt
import tkinter
from tkinter import *
from tkinter import ttk
import re


root = Tk()
root.title("Aplikacioni per detyren e trete")
root.geometry("470x400")
guiFont = font = dict(family='Courier New, monospaced', size=18, color='#7f7f7f')

my_menu = Menu(root)
root.config(menu=my_menu)


def get_chrome():

    data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    c = sqlite3.connect(data_path)
    cursor = c.cursor()
    select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
    cursor.execute(select_statement)

    login_data = cursor.fetchall()

    cred = {}

    string = ''

    for url, user_name, pwd in login_data:
        pwd = win32crypt.CryptUnprotectData(pwd)
        cred[url] = (user_name, pwd[1].decode('utf8'))
        string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url,user_name,pwd[1].decode('utf8'))
        print(string)


if _name__=='__main_':
    get_chrome()

def our_command():
	hide_frames()
	teksti = Label(root, text = "Passwordat jane shfaqur ne terminal").pack()

def fk():
	hide_frames()
	korniza.pack(fill="both", expand=1)
	teksti = Label(korniza, text = "Universiteti i Prishtinës 'Hasan Prishtina'").pack()
	teksti = Label(korniza, text = "Departamenti: Inxhinieri Kompjuterike").pack()
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



#input i paswordit permes keyboard
eLabel = Label(root, text="Please Enter you Password:   ", font=guiFont)
eLabel.pack(side=tkinter.TOP)
ePassword = Entry(root, show="*")
ePassword.pack(side=tkinter.TOP)



#kontrollimi per validimin e paswordit (strength check)
def checkPassword():
    strength = ['Password can not be Blank', 'Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong']
    score = 1
    password = ePassword.get()

    hide_frames()


    if len(password) < 1:
        return strength[0]

    if len(password) < 4:
        return strength[1]

    if len(password) >= 8:
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1

    if re.search(".", password):
        score += 1

    passwordStrength.set(strength[score])


passwordStrength = StringVar()
checkStrBtn = Button(root, text="Check Strength", command=checkPassword, height=1, width=18, font=guiFont)
checkStrBtn.pack(side=tkinter.TOP)
checkStrLab = Label(root, textvariable=passwordStrength)
checkStrLab.pack(side=tkinter.TOP)


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
show_menu.add_command(label="Show passwords from Google Chrome", command=get_chrome)



#krijimi i menyse se trete
validimi = Menu(my_menu)
my_menu.add_cascade(label="Validation", menu=validimi)
validimi.add_command(label="Validimi i passwords", command=checkPassword)
validimi.add_separator()



korniza = Frame(root, width=400, height=400, bg="light blue")
teksti = Label(root)



butoni = Button(root, text="Dil nga programi", command=root.quit)
butoni.pack(side=tkinter.BOTTOM)

root.mainloop()
