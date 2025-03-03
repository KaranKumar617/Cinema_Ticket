import tkinter as tk
root=tk.Tk()

def next_function():
    print("Button clicked!")
    
canvas=tk.Canvas()
canvas.pack()

background_image= tk.PhotoImage(file='cinema5.png')
background_label= tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1 )
frame=tk.Frame(root,bg="black", bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75,relheight=0.1,anchor="n")
button=tk.Button(root, text="NEXT", bg="royalblue4", fg="azure", font=90, bd= 50, command=root.destroy)
button.pack()
label=tk.Label(frame, text="WELCOME TO IMAX DIGITAL ", bg="royalblue4", font=180, bd=15)
label.place(relwidth=1, relheight=1)

root.mainloop()

from tkinter import *
import os

# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="royalblue4").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()

# Designing window for login 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Implementing event on register button
def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Implementing event on login button 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()
    else:
        user_not_found()

# Designing popup for login success
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups
def delete_login_success():
    login_success_screen.destroy()
    main_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="royalblue4", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()

main_account_screen()

from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Ticket form")
window.geometry('200x200')
window.configure(background = "royalblue4");

a = Label(window ,text = "no of Tickets").grid(row = 0,column = 1)
b = Label(window ,text = "Name of Movie").grid(row = 1,column = 1)
c = Label(window ,text = "Seat Number").grid(row = 2,column = 1)
d = Label(window ,text = "age").grid(row = 3,column = 1)
e = Label(window ,text = "CNIC").grid(row = 4,column = 1)
f = Label(window ,text = "Date").grid(row = 5,column = 1)
g = Label(window ,text = "Day").grid(row = 6,column = 1)
a1 = Entry(window).grid(row = 0,column = 4)
b1 = Entry(window).grid(row = 1,column = 4)
c1 = Entry(window).grid(row = 2,column = 4)
d1 = Entry(window).grid(row = 3,column = 4)
e1 = Entry(window).grid(row = 4,column = 4)
f1 = Entry(window).grid(row = 5,column = 4)
g1 = Entry(window).grid(row = 6,column = 4)
def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit", command=window.destroy).grid(row=8,column=4)
window.mainloop()

import tkinter as tk
root=tk.Tk()

def next_function():
    print("Button clicked!")
    
canvas=tk.Canvas()
canvas.pack()

background_image= tk.PhotoImage(file='cinema6.png')
background_label= tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1 )
frame=tk.Frame(root,bg="black", bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75,relheight=0.1,anchor="n")
button=tk.Button(root, text="EXIT", bg="Royalblue4", fg="azure", font=90, bd= 50, command=root.destroy)
button.pack()
label=tk.Label(frame, text="Your TICKETS have been confirmed!", bg="royalblue4", font=180, bd=15)
label.place(relwidth=1, relheight=1)

root.mainloop()
