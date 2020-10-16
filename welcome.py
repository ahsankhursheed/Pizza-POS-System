import tkinter as tk
from tkinter import *
import os
from tkinter import messagebox
from PIL import Image,ImageTk




def welcome_GUI():
    
    global root
    root = tk.Tk()
    top = WelcomeGUI (root)
    root.mainloop()

class WelcomeGUI:
    def __init__(self, top=None):
        
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec'
        font11 = "-family {Segoe UI Black} -size 19 -weight bold"
        font12 = "-family {Segoe UI Black} -size 22 -weight bold"
        font14 = "-family {MS Sans Serif} -size 18 -weight bold"

        top.geometry("659x459+378+149")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Welcome")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=-0.03, rely=0.044, height=62, width=717)
        self.Label1.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font11,foreground="#000000",relief="raised",text='''WELCOME TO PIZZA POS SYSTEM''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.188, rely=0.196, height=61, width=408)
        self.Label2.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font12,foreground="#000000",relief="ridge",text='''Bigger Size, Beter Taste''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.091, rely=0.436, height=41, width=563)
        self.Label3.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font14,foreground="#000000",text='''Click Below Options to Proceed''')

        self.Button1_7 = tk.Button(top)
        self.Button1_7.place(relx=0.349, rely=0.85, height=54, width=197)
        self.Button1_7.configure(command=self.Logout,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 16 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Logout''')
 
        self.Button1_8 = tk.Button(top)
        self.Button1_8.place(relx=0.349, rely=0.697, height=54, width=197)
        self.Button1_8.configure(command=self.GoToInventory,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 16 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Go To Inventory''')
 
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.349, rely=0.545, height=54, width=197)
        self.Button1.configure(command=self.GoToOrders,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 16 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Go To Orders''')

    
    def GoToOrders(self):
        root.destroy()
        import orders
        orders.orders_GUI()

    def GoToInventory(self):
        root.destroy()
        import inventory
        inventory.inventory_GUI()
    
    def Logout(self):
        root.destroy()
        import login
        login.load_login_GUI()
 
if __name__ == '__main__':
    welcome_GUI()
 
 

