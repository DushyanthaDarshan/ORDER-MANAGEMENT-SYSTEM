from tkinter import *
import tkinter as tk
from tkinter import messagebox

import pymysql
import os


# Author : Dushyantha Rubasinghe
# Date   : 02/23/2020


class Order(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Order Page")
        self.master.geometry('1280x720+0+0')
        self.master.config(bg="LightBlue1")
        self.frame.pack()

        self.order_list = Label(self.master, bg="LightBlue1", fg="blue", text="Order List:", font=("bald" + "Calibri", 15))
        self.order_list.place(x=10, y=20)
        self.price_list = Label(self.master, bg="LightBlue1", fg="blue", text="Items & Price List:", font=("bald" + "Calibri", 15))
        self.price_list.place(x=685, y=20)

        self.help = Button(self.master, text="Help", bg="DeepSkyBlue2", width="10", height="1",
                           font=("bald" + "Calibri", 13), command=self.coming)
        self.help.place(x=1100, y=15)
        self.log_exit = Button(self.master, text="Exit", bg="red", width="10", height="1", font=("bald" + "Calibri", 13), command=self.log_out)
        self.log_exit.place(x=1100, y=670)
        self.log_back = Button(self.master, text="Back", bg="RoyalBlue1", width="10", height="1",
                               font=("bald" + "Calibri", 13), command=self.back_to_home_page)
        self.log_back.place(x=0, y=670)

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Price List Frame <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        right_frame = Frame(self.master, bd=5, width=640, height=620, padx=5, bg="LightSteelBlue2", relief=RIDGE).pack(side=RIGHT)

        self.category = Label(self.master, bg="LightSteelBlue2", fg="SpringGreen3", text="Category: Pizza", font=("bald" + "Calibri", 14))
        self.category.place(x=670, y=60)
        self.food = Label(self.master, bg="LightSteelBlue2", fg="purple", text="Food Name",
                              font=("bald" + "Calibri", 13))
        self.food.place(x=670, y=92)
        self.f_size = Label(self.master, bg="LightSteelBlue2", fg="purple", text="Food Size",
                              font=("bald" + "Calibri", 14))
        self.f_size.place(x=860, y=92)
        self.f_price = Label(self.master, bg="LightSteelBlue2", fg="purple", text="Price",
                            font=("bald" + "Calibri", 14))
        self.f_price.place(x=1000, y=92)
        self.f_code = Label(self.master, bg="LightSteelBlue2", fg="purple", text="Code",
                             font=("bald" + "Calibri", 14))
        self.f_code.place(x=1110, y=92)
        self.f_status = Label(self.master, bg="LightSteelBlue2", fg="purple", text="Status",
                             font=("bald" + "Calibri", 14))
        self.f_status.place(x=1200, y=92)

        # Devilled Chicken Pizza personal
        self.l1 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Devilled Chicken",
                              font=("bald" + "Calibri", 11))
        self.l1.place(x=670, y=124)
        self.l2 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Personal",
                        font=("bald" + "Calibri", 11))
        self.l2.place(x=860, y=124)
        self.l7 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Rs.500.00",
                        font=("bald" + "Calibri", 11))
        self.l7.place(x=1000, y=124)
        self.l8 = Label(self.master, bg="LightSteelBlue2", fg="black", text="d100",
                        font=("bald" + "Calibri", 11))
        self.l8.place(x=1110, y=124)
        self.l9 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Available",
                        font=("bald" + "Calibri", 11))
        self.l9.place(x=1200, y=124)

        # Devilled Chicken Pizza medium
        self.l3 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Devilled Chicken",
                        font=("bald" + "Calibri", 11))
        self.l3.place(x=670, y=150)
        self.l4 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Medium",
                        font=("bald" + "Calibri", 11))
        self.l4.place(x=860, y=150)
        self.l10 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Rs.950.00",
                        font=("bald" + "Calibri", 11))
        self.l10.place(x=1000, y=150)
        self.l11 = Label(self.master, bg="LightSteelBlue2", fg="black", text="d150",
                        font=("bald" + "Calibri", 11))
        self.l11.place(x=1110, y=150)
        self.l12 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Available",
                        font=("bald" + "Calibri", 11))
        self.l12.place(x=1200, y=150)

        # Devilled Chicken Pizza Large
        self.l5 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Devilled Chicken",
                        font=("bald" + "Calibri", 11))
        self.l5.place(x=670, y=176)
        self.l6 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Large",
                        font=("bald" + "Calibri", 11))
        self.l6.place(x=860, y=176)
        self.l13 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Rs.1650.00",
                         font=("bald" + "Calibri", 11))
        self.l13.place(x=1000, y=176)
        self.l14 = Label(self.master, bg="LightSteelBlue2", fg="black", text="d190",
                         font=("bald" + "Calibri", 11))
        self.l14.place(x=1110, y=176)
        self.l15 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Available",
                         font=("bald" + "Calibri", 11))
        self.l15.place(x=1200, y=176)

        # Cheese Lovers Pizza Personal
        self.l16 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Cheese Lovers",
                        font=("bald" + "Calibri", 11))
        self.l16.place(x=670, y=202)
        self.l17 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Personal",
                        font=("bald" + "Calibri", 11))
        self.l17.place(x=860, y=202)
        self.l18 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Rs.500.00",
                         font=("bald" + "Calibri", 11))
        self.l18.place(x=1000, y=202)
        self.l19 = Label(self.master, bg="LightSteelBlue2", fg="black", text="d200",
                         font=("bald" + "Calibri", 11))
        self.l19.place(x=1110, y=202)
        self.l20 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Available",
                         font=("bald" + "Calibri", 11))
        self.l20.place(x=1200, y=202)

        # Cheese Lovers Pizza Medium
        self.l16 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Cheese Lovers",
                         font=("bald" + "Calibri", 11))
        self.l16.place(x=670, y=228)
        self.l17 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Medium",
                         font=("bald" + "Calibri", 11))
        self.l17.place(x=860, y=228)
        self.l18 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Rs.900.00",
                         font=("bald" + "Calibri", 11))
        self.l18.place(x=1000, y=228)
        self.l19 = Label(self.master, bg="LightSteelBlue2", fg="black", text="d250",
                         font=("bald" + "Calibri", 11))
        self.l19.place(x=1110, y=228)
        self.l20 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Available",
                         font=("bald" + "Calibri", 11))
        self.l20.place(x=1200, y=228)

        # Cheese Lovers Pizza Large
        self.l16 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Cheese Lovers",
                         font=("bald" + "Calibri", 11))
        self.l16.place(x=670, y=254)
        self.l17 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Large",
                         font=("bald" + "Calibri", 11))
        self.l17.place(x=860, y=254)
        self.l18 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Rs.1620.00",
                         font=("bald" + "Calibri", 11))
        self.l18.place(x=1000, y=254)
        self.l19 = Label(self.master, bg="LightSteelBlue2", fg="black", text="d290",
                         font=("bald" + "Calibri", 11))
        self.l19.place(x=1110, y=254)
        self.l20 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Available",
                         font=("bald" + "Calibri", 11))
        self.l20.place(x=1200, y=254)

        # Spicy Veggie Pizza Personal
        self.l16 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Spicy Veggie",
                         font=("bald" + "Calibri", 11))
        self.l16.place(x=670, y=280)
        self.l17 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Personal",
                         font=("bald" + "Calibri", 11))
        self.l17.place(x=860, y=280)
        self.l18 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Rs.460.00",
                         font=("bald" + "Calibri", 11))
        self.l18.place(x=1000, y=280)
        self.l19 = Label(self.master, bg="LightSteelBlue2", fg="black", text="d300",
                         font=("bald" + "Calibri", 11))
        self.l19.place(x=1110, y=280)
        self.l20 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Available",
                         font=("bald" + "Calibri", 11))
        self.l20.place(x=1200, y=280)

        # Spicy Veggie Pizza Medium
        self.l16 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Spicy Veggie",
                         font=("bald" + "Calibri", 11))
        self.l16.place(x=670, y=306)
        self.l17 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Medium",
                         font=("bald" + "Calibri", 11))
        self.l17.place(x=860, y=306)
        self.l18 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Rs.880.00",
                         font=("bald" + "Calibri", 11))
        self.l18.place(x=1000, y=306)
        self.l19 = Label(self.master, bg="LightSteelBlue2", fg="black", text="d350",
                         font=("bald" + "Calibri", 11))
        self.l19.place(x=1110, y=306)
        self.l20 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Available",
                         font=("bald" + "Calibri", 11))
        self.l20.place(x=1200, y=306)

        # Spicy Veggie Pizza Large
        self.l16 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Spicy Veggie",
                         font=("bald" + "Calibri", 11))
        self.l16.place(x=670, y=332)
        self.l17 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Large",
                         font=("bald" + "Calibri", 11))
        self.l17.place(x=860, y=332)
        self.l18 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Rs.1500.00",
                         font=("bald" + "Calibri", 11))
        self.l18.place(x=1000, y=332)
        self.l19 = Label(self.master, bg="LightSteelBlue2", fg="black", text="d390",
                         font=("bald" + "Calibri", 11))
        self.l19.place(x=1110, y=332)
        self.l20 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Available",
                         font=("bald" + "Calibri", 11))
        self.l20.place(x=1200, y=332)

        # Label for Dessert
        self.dessert = Label(self.master, bg="LightSteelBlue2", fg="SpringGreen3", text="Category: Dessert",
                              font=("bald" + "Calibri", 14))
        self.dessert.place(x=670, y=360)

        # Ice cream(Vanilla)
        self.l16 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Ice cream(Vanilla)",
                         font=("bald" + "Calibri", 11))
        self.l16.place(x=670, y=386)
        self.l17 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Medium",
                         font=("bald" + "Calibri", 11))
        self.l17.place(x=860, y=386)
        self.l18 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Rs.100.00",
                         font=("bald" + "Calibri", 11))
        self.l18.place(x=1000, y=386)
        self.l19 = Label(self.master, bg="LightSteelBlue2", fg="black", text="d600",
                         font=("bald" + "Calibri", 11))
        self.l19.place(x=1110, y=386)
        self.l20 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Available",
                         font=("bald" + "Calibri", 11))
        self.l20.place(x=1200, y=386)

        # Ice cream(Chocolate)
        self.l16 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Ice cream(Chocolate)",
                         font=("bald" + "Calibri", 11))
        self.l16.place(x=670, y=412)
        self.l17 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Medium",
                         font=("bald" + "Calibri", 11))
        self.l17.place(x=860, y=412)
        self.l18 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Rs.100.00",
                         font=("bald" + "Calibri", 11))
        self.l18.place(x=1000, y=412)
        self.l19 = Label(self.master, bg="LightSteelBlue2", fg="black", text="d650",
                         font=("bald" + "Calibri", 11))
        self.l19.place(x=1110, y=412)
        self.l20 = Label(self.master, bg="LightSteelBlue2", fg="black", text="Available",
                         font=("bald" + "Calibri", 11))
        self.l20.place(x=1200, y=412)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Order List Frame<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        left_frame = Frame(self.master, bd=5, width=640, height=620, padx=5, bg="LightSteelBlue3", relief=RIDGE).pack(side=LEFT)

        global code_info_1
        global code_info_2
        global code_info_3
        global code_info_4
        global code_info_5

        global quantity_info_1
        global quantity_info_2
        global quantity_info_3
        global quantity_info_4
        global quantity_info_5

        code_info_1 = StringVar()
        code_info_2 = StringVar()
        code_info_3 = StringVar()
        code_info_4 = StringVar()
        code_info_5 = StringVar()

        quantity_info_1 = StringVar()
        quantity_info_2 = StringVar()
        quantity_info_3 = StringVar()
        quantity_info_4 = StringVar()
        quantity_info_5 = StringVar()

        self.code = Label(self.master, bg="LightSteelBlue3", fg="purple", text="Code", font=("bald" + "Calibri", 13))
        self.code.place(x=10, y=60)
        self.food_type = Label(self.master, bg="LightSteelBlue3", fg="purple", text="Food Name", font=("bald" + "Calibri", 13))
        self.food_type.place(x=100, y=60)
        self.size = Label(self.master, bg="LightSteelBlue3", fg="purple", text="Size", font=("bald" + "Calibri", 13))
        self.size.place(x=340, y=60)
        self.quantity = Label(self.master, bg="LightSteelBlue3", fg="purple", text="Quantity", font=("bald" + "Calibri", 13))
        self.quantity.place(x=450, y=60)
        self.price = Label(self.master, bg="LightSteelBlue3", fg="purple", text="Price (Rs.)", font=("bald" + "Calibri", 13))
        self.price.place(x=540, y=60)

        # Code entries
        self.code_entry_1 = Entry(self.master, width="7", textvariable=code_info_1)
        self.code_entry_1.place(x=10, y=102)
        self.code_entry_2 = Entry(self.master, width="7", textvariable=code_info_2)
        self.code_entry_2.place(x=10, y=144)
        self.code_entry_3 = Entry(self.master, width="7", textvariable=code_info_3)
        self.code_entry_3.place(x=10, y=186)
        self.code_entry_4 = Entry(self.master, width="7", textvariable=code_info_4)
        self.code_entry_4.place(x=10, y=228)
        self.code_entry_5 = Entry(self.master, width="7", textvariable=code_info_5)
        self.code_entry_5.place(x=10, y=270)

        # Quantity entries
        self.quantity_entry_1 = Entry(self.master, width="7", textvariable=quantity_info_1)
        self.quantity_entry_1.place(x=450, y=102)
        self.quantity_entry_2 = Entry(self.master, width="7", textvariable=quantity_info_2)
        self.quantity_entry_2.place(x=450, y=144)
        self.quantity_entry_3 = Entry(self.master, width="7", textvariable=quantity_info_3)
        self.quantity_entry_3.place(x=450, y=186)
        self.quantity_entry_4 = Entry(self.master, width="7", textvariable=quantity_info_4)
        self.quantity_entry_4.place(x=450, y=228)
        self.quantity_entry_5 = Entry(self.master, width="7", textvariable=quantity_info_5)
        self.quantity_entry_5.place(x=450, y=270)

        # Table number and total label
        global table_number_info
        table_number_info = StringVar()

        self.table_number = Label(self.master, bg="LightSteelBlue3", fg="VioletRed3", text="Table Number: ",
                                  font=("bald" + "Calibri", 14)).place(x=10, y=400)
        self.table_number_entry = Entry(self.master, width="7", textvariable=table_number_info)
        self.table_number_entry.place(x=170, y=400)
        self.total_label = Label(self.master, bg="LightSteelBlue3", fg="VioletRed3", text="Total: ",
                                  font=("bald" + "Calibri", 14)).place(x=470, y=400)

        self.submit = Button(self.master, text="Submit", bg="yellow2", width="10", height="1",
                             font=("bald" + "Calibri", 13), command=self.submit)
        self.submit.place(x=20, y=620)
        self.comfirm = Button(self.master, text="Confirm", bg="green2", width="10", height="1",
                               font=("bald" + "Calibri", 13), command=self.confirm)
        self.comfirm.place(x=470, y=620)


    def back_to_home_page(self):
        from MainPage import Main

        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        ee = Main(self.newWindow)

    def submit(self):
        # code entries getters
        global code_1
        global code_2
        global code_3
        global code_4
        global code_5

        code_1 = code_info_1.get()
        code_2 = code_info_2.get()
        code_3 = code_info_3.get()
        code_4 = code_info_4.get()
        code_5 = code_info_5.get()

        # List of code getters
        global code_getters_list
        code_getters_list = [code_1, code_2, code_3, code_4, code_5]

        # quantity entries getters
        global quantity_1
        global quantity_2
        global quantity_3
        global quantity_4
        global quantity_5

        quantity_1 = quantity_info_1.get()
        quantity_2 = quantity_info_2.get()
        quantity_3 = quantity_info_3.get()
        quantity_4 = quantity_info_4.get()
        quantity_5 = quantity_info_5.get()

        # List of quantity getters
        global quantity_getters_list
        quantity_getters_list = [quantity_1, quantity_2, quantity_3, quantity_4, quantity_5]

        for x in range(len(code_getters_list)):
            if code_getters_list[x]=="" or code_getters_list[x]==" ":
                msg = messagebox.askyesno("Information", "Are you sure, you ordered all your food items!!!")
                if msg==YES:
                    messagebox.showinfo("Information", "Press the Confirm button!!!")
            break

        self.fill_name_from_db()

    def fill_name_from_db(self):
        global total

        connection = pymysql.connect(host="localhost", user="root", password="gvt123", db="ORDER_MANAGEMENT_DB")
        cur = connection.cursor()
        # entry code 1
        get_sql = "SELECT FOOD_NAME, SIZE, PRICE FROM ITEMS WHERE CODE=%s "
        values = (code_1)
        code_query = cur.execute(get_sql, values)
        result1 = cur.fetchone()
        a1 = StringVar()
        a2 = StringVar()
        a3 = StringVar()
        self.f_name_1 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=a1, font=("bald" + "Calibri", 12))
        self.f_name_1.place(x=100, y=102)
        a1.set(result1[0])
        self.f_size_1 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=a2, font=("bald" + "Calibri", 12))
        self.f_size_1.place(x=340, y=102)
        a2.set(result1[1])
        self.f_price_1 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=a3,
                              font=("bald" + "Calibri", 12))
        self.f_price_1.place(x=570, y=102)
        a4 = result1[2] * int(quantity_1)
        a3.set(a4)
        total = a4
        self.total()

        # entry code 2
        get_sql = "SELECT FOOD_NAME, SIZE, PRICE FROM ITEMS WHERE CODE=%s "
        values = (code_2)
        code_query = cur.execute(get_sql, values)
        result2 = cur.fetchone()
        b1 = StringVar()
        b2 = StringVar()
        b3 = StringVar()
        self.f_name_2 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=b1,
                              font=("bald" + "Calibri", 12))
        self.f_name_2.place(x=100, y=144)
        b1.set(result2[0])
        self.f_size_2 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=b2,
                              font=("bald" + "Calibri", 12))
        self.f_size_2.place(x=340, y=144)
        b2.set(result2[1])
        self.f_price_2 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=b3,
                               font=("bald" + "Calibri", 12))
        self.f_price_2.place(x=570, y=144)
        b4 = result2[2] * int(quantity_2)
        b3.set(b4)
        total = a4 + b4
        self.total()

        # entry code 3
        get_sql = "SELECT FOOD_NAME, SIZE, PRICE FROM ITEMS WHERE CODE=%s "
        values = (code_3)
        code_query = cur.execute(get_sql, values)
        result3 = cur.fetchone()
        c1 = StringVar()
        c2 = StringVar()
        c3 = StringVar()
        self.f_name_3 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=c1,
                              font=("bald" + "Calibri", 12))
        self.f_name_3.place(x=100, y=186)
        c1.set(result3[0])
        self.f_size_3 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=c2,
                              font=("bald" + "Calibri", 12))
        self.f_size_3.place(x=340, y=186)
        c2.set(result3[1])
        self.f_price_3 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=c3,
                               font=("bald" + "Calibri", 12))
        self.f_price_3.place(x=570, y=186)
        c4 = result3[2] * int(quantity_3)
        c3.set(c4)
        total = a4 + b4 + c4
        self.total()

        # entry code 4
        get_sql = "SELECT FOOD_NAME, SIZE, PRICE FROM ITEMS WHERE CODE=%s "
        values = (code_4)
        code_query = cur.execute(get_sql, values)
        result4 = cur.fetchone()
        d1 = StringVar()
        d2 = StringVar()
        d3 = StringVar()
        self.f_name_4 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=d1,
                              font=("bald" + "Calibri", 12))
        self.f_name_4.place(x=100, y=228)
        d1.set(result4[0])
        self.f_size_4 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=d2,
                              font=("bald" + "Calibri", 12))
        self.f_size_4.place(x=340, y=228)
        d2.set(result4[1])
        self.f_price_4 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=d3,
                               font=("bald" + "Calibri", 12))
        self.f_price_4.place(x=570, y=228)
        d4 = result4[2] * int(quantity_4)
        d3.set(d4)
        total = a4 + b4 + c4 + d4
        self.total()

        # entry code 5
        get_sql = "SELECT FOOD_NAME, SIZE, PRICE FROM ITEMS WHERE CODE=%s "
        values = (code_5)
        code_query = cur.execute(get_sql, values)
        result5 = cur.fetchone()
        e1 = StringVar()
        e2 = StringVar()
        e3 = StringVar()
        self.f_name_5 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=e1,
                              font=("bald" + "Calibri", 12))
        self.f_name_5.place(x=100, y=270)
        e1.set(result5[0])
        self.f_size_5 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=e2,
                              font=("bald" + "Calibri", 12))
        self.f_size_5.place(x=340, y=270)
        e2.set(result5[1])
        self.f_price_5 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=e3,
                               font=("bald" + "Calibri", 12))
        self.f_price_5.place(x=570, y=270)
        e4 = result5[2] * int(quantity_5)
        e3.set(e4)
        total = a4 + b4 + c4 + d4 + e4
        self.total()

        connection.close()

    def total(self):
        if table_number_info.get()=="":
            messagebox.showerror("Error", "You must enter your table number. Because we call table number")
        else:
            f1 = StringVar()
            self.total1 = Label(self.master, bg="LightSteelBlue3", fg="black", textvariable=f1,
                                  font=("bald" + "Calibri", 12))
            self.total1.place(x=570, y=400)
            f1.set(total)


    def coming(self):
        messagebox.showinfo("Alert", "This function will be coming soon!!!")

    def confirm(self):
        messagebox.showinfo("Alert", "If you change something after the submit please resubmit for the corrections")

        # Insert 1st row
        if code_info_1.get()!="":
            self.sql_1()

        # Insert 2nd row
        if code_info_2.get()!="":
            self.sql_2()

        # Insert 3rd row
        if code_info_3.get() != "":
            self.sql_3()

        # Insert 4th row
        if code_info_4.get() != "":
            self.sql_4()

        # Insert 5th row
        if code_info_5.get() != "":
            self.sql_5()

        messagebox.showinfo("Thank You our valuable customer!!!", "Please kindly wait 10min for the your order...")

    def sql_1(self):
        connection_1 = pymysql.connect(host="localhost", user="root", password="gvt123", db="ORDER_MANAGEMENT_DB")
        cur_1 = connection_1.cursor()
        table_number = table_number_info.get()
        insert_order_1 = "INSERT INTO ORDERS(CODE, QUANTITY, TABLE_NUMBER) VALUES (%s, %s, %s)"
        val_1 = (code_1, quantity_1, table_number)
        cur_1.execute(insert_order_1, val_1)
        connection_1.commit()
        connection_1.close()

    def sql_2(self):
        connection_2 = pymysql.connect(host="localhost", user="root", password="gvt123", db="ORDER_MANAGEMENT_DB")
        cur_2 = connection_2.cursor()
        table_number = table_number_info.get()
        insert_order_2 = "INSERT INTO ORDERS(CODE, QUANTITY, TABLE_NUMBER) VALUES (%s, %s, %s)"
        val_2 = (code_2, quantity_2, table_number)
        cur_2.execute(insert_order_2, val_2)
        connection_2.commit()
        connection_2.close()

    def sql_3(self):
        connection_3 = pymysql.connect(host="localhost", user="root", password="gvt123", db="ORDER_MANAGEMENT_DB")
        cur_3 = connection_3.cursor()
        table_number = table_number_info.get()
        insert_order_3 = "INSERT INTO ORDERS(CODE, QUANTITY, TABLE_NUMBER) VALUES (%s, %s, %s)"
        val_3 = (code_3, quantity_3, table_number)
        cur_3.execute(insert_order_3, val_3)
        connection_3.commit()
        connection_3.close()

    def sql_4(self):
        connection_4 = pymysql.connect(host="localhost", user="root", password="gvt123", db="ORDER_MANAGEMENT_DB")
        cur_4 = connection_4.cursor()
        table_number = table_number_info.get()
        insert_order_4 = "INSERT INTO ORDERS(CODE, QUANTITY, TABLE_NUMBER) VALUES (%s, %s, %s)"
        val_4 = (code_4, quantity_4, table_number)
        cur_4.execute(insert_order_4, val_4)
        connection_4.commit()
        connection_4.close()

    def sql_5(self):
        connection_5 = pymysql.connect(host="localhost", user="root", password="gvt123", db="ORDER_MANAGEMENT_DB")
        cur_5 = connection_5.cursor()
        table_number = table_number_info.get()
        insert_order_5 = "INSERT INTO ORDERS(CODE, QUANTITY, TABLE_NUMBER) VALUES (%s, %s, %s)"
        val_5 = (code_5, quantity_5, table_number)
        cur_5.execute(insert_order_5, val_5)
        connection_5.commit()
        connection_5.close()

    def log_out(self):
        msg1 = messagebox.askyesno("Log out","Thank You!!!, Do you want to log out and exit?")
        if msg1==YES:
            exit()