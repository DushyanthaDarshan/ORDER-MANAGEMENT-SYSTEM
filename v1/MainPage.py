from tkinter import *
import tkinter
from tkinter import messagebox

from PIL import Image, ImageTk
import tkinter as tk
from RegisterPage import Register
from LoginPage import Login


# Author : Dushyantha Rubasinghe
# Date   : 02/23/2020


class Main(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Main Page")
        self.master.geometry('1280x720+0+0')
        self.master.configure(bg="grey")
        self.frame.pack()

        self.header = Label(self.master, text="Dush Fo"
                                              "od city Orders", bg="powder blue", width="50", height="4",
                            font=("bald" + "arial", 35), anchor=CENTER, relief=RAISED, justify=CENTER)
        self.header.place(x=0, y=0)
        self.reg = Button(self.master, text="Register", bg="blue", width="20", height="2",
                          font=("bald" + "Calibri", 13),
                          command=self.new_window)
        self.reg.place(x=10, y=200)
        sign_in = Button(self.master, text="Sign In", bg="green", width="20", height="2", font=("bald" + "Calibri", 13),
                         command=self.new_window2)
        sign_in.place(x=250, y=200)
        faq = Button(self.master, text="FAQ", bg="orange", width="20", height="2",
                         font=("bald" + "Calibri", 13), command=self.coming)
        faq.place(x=500, y=200)
        about_us = Button(self.master, text="About Us", bg="purple", width="20", height="2",
                          font=("bald" + "Calibri", 13), command=self.coming)
        about_us.place(x=750, y=200)
        main_exit = Button(self.master, text="Exit", bg="red", width="20", height="2", font=("bald" + "Calibri", 13),
                           command=self.log_out)
        main_exit.place(x=1000, y=620)
        self.l2 = Label(self.master, fg="purple", text="Special Offers", font=("bald" + "Calibri", 19))
        self.l2.place(x=450, y=290)

        self.show_img()

    def new_window(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        bb = Register(self.newWindow)

    def new_window2(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        cc = Login(self.newWindow)

    def show_img(self):
        # Logo
        load = Image.open("Pizza-logos.png")
        imgs = load.resize((270, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(imgs)

        img = Label(self.master, image=render, relief=RAISED)
        img.image = render
        img.place(x=0, y=0)

        # Background images 1
        load2 = Image.open("Chillie Chicken Pizza-1.jpg")
        imgs2 = load2.resize((350, 200), Image.ANTIALIAS)
        render2 = ImageTk.PhotoImage(imgs2)

        img2 = Label(self.master, image=render2, relief=RAISED)
        img2.image = render2
        img2.place(x=80, y=350)
        self.l2 = Label(self.master, fg="purple", text="Devilled Chicken Pizza - Large - Only Rs.1650.00",
                        font=("bald" + "Calibri", 14))
        self.l2.place(x=20, y=570)

        # Background images 2
        load3 = Image.open("Cheese-Lover-Pizza.jpg")
        imgs3 = load3.resize((330, 200), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(imgs3)

        img3 = Label(self.master, image=render3, relief=RAISED)
        img3.image = render3
        img3.place(x=700, y=350)
        self.l3 = Label(self.master, fg="purple", text="Cheese Lovers Pizza - Large - Only Rs.1620.00",
                        font=("bald" + "Calibri", 14))
        self.l3.place(x=650, y=570)

    def coming(self):
        messagebox.showinfo("Alert", "This function will be coming soon!!!")

    def log_out(self):
        msg1 = messagebox.askyesno("EXIT","Do you want to exit?")
        if msg1==YES:
            exit()


if __name__ == "__main__":
    root = tk.Tk()
    Main(root).pack(side="top", fill="both", expand=True)
    root.mainloop()