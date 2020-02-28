from tkinter import *
import tkinter as tk
from tkinter import messagebox

import pymysql
import os


# Author : Dushyantha Rubasinghe
# Date   : 02/23/2020

global email_entry
global password_entry
global full_name_entry


class Register(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Register Page")
        self.master.geometry('400x500+0+0')
        self.master.config(bg="white")
        self.frame.pack()

        global email_info
        global password_info
        global full_name_info
        global nic_info

        email_info = StringVar()
        password_info = StringVar()
        full_name_info = StringVar()
        nic_info = StringVar()

        self.l1 = Label(self.master, bg="powder blue", text="Register Form", width="33", height="2",
                        font=("bald" + "Calibri", 15))
        self.l1.place(x=0, y=0)
        self.l2 = Label(self.master, bg="white", fg="blue", text="Your Full Name:", font=("bald" + "Calibri", 12))
        self.l2.place(x=0, y=58)
        self.full_name_entry = Entry(self.master, width="30", textvariable=full_name_info)
        self.full_name_entry.place(x=130, y=58)
        self.l3 = Label(self.master, bg="white", fg="blue", text="Email Address:", font=("bald" + "Calibri", 12))
        self.l3.place(x=0, y=100)
        self.email_entry = Entry(self.master, width="30", textvariable=email_info)
        self.email_entry.place(x=130, y=100)
        self.l5 = Label(self.master, bg="white", fg="blue", text="Password:", font=("bald" + "Calibri", 12))
        self.l5.place(x=0, y=142)
        self.password_entry = Entry(self.master, width="30", textvariable=password_info, show="*")
        self.password_entry.place(x=130, y=142)
        self.l6 = Label(self.master, bg="white", fg="blue", text="NIC:", font=("bald" + "Calibri", 12))
        self.l6.place(x=0, y=184)
        self.phone_entry = Entry(self.master, width="30", textvariable=nic_info)
        self.phone_entry.place(x=130, y=184)
        self.register_button = Button(self.master, text="Register", bg="gold", width="10", height="2",
                                      font=("bald" + "Calibri", 15), command=self.check_register)
        self.register_button.place(x=100, y=226)
        self.reg_exit = Button(self.master, text="Exit", bg="red", width="10", height="1",
                               font=("bald" + "Calibri", 13), command=self.log_out)
        self.reg_exit.place(x=250, y=400)
        self.reg_back = Button(self.master, text="Back", bg="SlateBlue1", width="10", height="1",
                               font=("bald" + "Calibri", 13), command=self.back_to_home_page)
        self.reg_back.place(x=0, y=400)
        self.footer = Label(self.master, bg="powder blue", width="50", height="4").place(x=0, y=450)

    def register_user(self):
        connection = pymysql.connect(host="localhost", user="root", password="gvt123", db="ORDER_MANAGEMENT_DB")
        cur = connection.cursor()

        email = email_info.get()
        password = password_info.get()
        full_name = full_name_info.get()

        insert_sql = "INSERT INTO USERS(FULL_NAME, EMAIL, PASSWORD) VALUES (%s, %s, %s)"
        val = (full_name, email, password)
        cur.execute(insert_sql, val)
        connection.commit()
        # connection.rollback()
        connection.close()

        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.full_name_entry.delete(0, END)

    def back_to_home_page(self):
        from MainPage import Main

        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        aa = Main(self.newWindow)

    def check_register(self):
        if email_info.get()=="" or password_info.get()=="":
            messagebox.showerror("Error", "All fields are required!!!")
        elif len(password_info.get())!= 5:
            messagebox.showerror("Error", "There should be 5 characters or 5 numbers in password!!!")
        else:
            self.register_user()

    def log_out(self):
        msg1 = messagebox.askyesno("EXIT","Do you want to exit?")
        if msg1==YES:
            exit()
