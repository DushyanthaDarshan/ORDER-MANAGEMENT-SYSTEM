from tkinter import *
import tkinter as tk
from tkinter import messagebox

import pymysql
import os


# Author : Dushyantha Rubasinghe
# Date   : 02/23/2020
from OrderList import Order

global email_login
global password_login


class Login(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Login Page")
        self.master.geometry('600x500+0+0')
        self.master.config(bg="LightBlue1")
        self.frame.pack()

        global email_login_info
        global password_login_info

        email_login_info = StringVar()
        password_login_info = StringVar()

        self.l8 = Label(self.master, bg="cyan", text="Login Form", width="50", height="2",
                        font=("bald" + "Calibri", 15))
        self.l8.place(x=0, y=0)
        self.l9 = Label(self.master, bg="LightBlue1", fg="blue", text="Email Address:", font=("bald" + "Calibri", 12))
        self.l9.place(x=0, y=100)
        self.email_login = Entry(self.master, width="30", textvariable=email_login_info)
        self.email_login.place(x=130, y=100)
        self.l5 = Label(self.master, bg="LightBlue1", fg="blue", text="Password:", font=("bald" + "Calibri", 12))
        self.l5.place(x=0, y=142)
        self.password_login = Entry(self.master, width="30", textvariable=password_login_info, show="*")
        self.password_login.place(x=130, y=142)
        self.login_button = Button(self.master, text="Login", bg="gold", width="10", height="2",
                                      font=("bald" + "Calibri", 15), command=self.user_login)
        self.login_button.place(x=170, y=226)
        self.log_exit = Button(self.master, text="Exit", bg="red", width="10", height="1",
                               font=("bald" + "Calibri", 13), command=self.log_out)
        self.log_exit.place(x=400, y=400)
        self.log_back = Button(self.master, text="Back", bg="SlateBlue1", width="10", height="1",
                               font=("bald" + "Calibri", 13), command=self.back_to_home_page)
        self.log_back.place(x=0, y=400)
        self.footer = Label(self.master, bg="cyan", width="90", height="4").place(x=0, y=450)

    def back_to_home_page(self):
        from MainPage import Main

        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        aa = Main(self.newWindow)

    def user_login(self):
        if email_login_info.get()=="" or password_login_info.get()=="":
            messagebox.showerror("Error", "All fields are required!!!")
        else:
            checking = self.check_db()
            if checking:
                messagebox.showinfo("Message", "Login Successfully")
                self.new_window3()
            else:
                messagebox.showerror("Alert!!", "Wrong, username or password")

    def check_db(self):
        check_email = email_login_info.get()
        check_password = password_login_info.get()

        connection = pymysql.connect(host="localhost", user="root", password="gvt123", db="ORDER_MANAGEMENT_DB")
        cur = connection.cursor()
        get_sql = "SELECT * FROM USERS WHERE EMAIL=%s AND PASSWORD=%s"
        values = (check_email, check_password)
        email_query = cur.execute(get_sql, values)
        account = cur.fetchone()
        connection.close()
        return account

    def new_window3(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        dd = Order(self.newWindow)

    def log_out(self):
        msg1 = messagebox.askyesno("EXIT","Do you want to exit?")
        if msg1==YES:
            exit()
