import tkinter as tk
from tkinter import *
import os
from tkinter import messagebox
from PIL import Image,ImageTk

def inventory_GUI():
    
    global root
    root = tk.Tk()
    top = InvetoryGUI (root)
    root.mainloop()


class InvetoryGUI:
    def __init__(self, top=None):
            
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec'

        top.geometry("773x586+289+80")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Inventory")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.207, rely=0.034, height=74, width=452)
        self.Label1.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",relief="groove",text='''INVENTORY''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.013, rely=0.256, height=74, width=137)
        self.Button1.configure(command=self.ViewStock,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 16 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''VIEW''')
 
        self.Button1_5 = tk.Button(top)
        self.Button1_5.place(relx=0.013, rely=0.41, height=74, width=137)
        self.Button1_5.configure(command=self.AddStock,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 16 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''UPDATE''')
 
        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.207, rely=0.239, relheight=0.575, relwidth=0.746)
        self.Text1.configure(background="white")
        self.Text1.configure(font="-family {Segoe UI} -size 18",foreground="black",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")
        
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.Text1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Text1.yview)

        self.Button1_6 = tk.Button(top)
        self.Button1_6.place(relx=0.246, rely=0.853, height=64, width=137)
        self.Button1_6.configure(command=self.Reset,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 16 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''RESET''')
 
        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.44, rely=0.853, height=64, width=137)
        self.Button1_1.configure(command=self.Back, activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 16 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''BACK''')
        

    def ViewStock(self):
        self.Text1.delete("1.0", "end")
        self.Text1.insert(END, "===================================\n")
        self.Text1.insert(END, "     ITEMS (SIZE)               |       QUANTITY\n")
        self.Text1.insert(END, "===================================\n\t\t         |\n")
        conset = set()
        p_list = []
        infile = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\StockItems.txt", "r")
        con = infile.read()
        infile.close()
        con2 = con.split("\n")
        con2.pop()
        for i in con2:
            conset.add(i)
            p_list.append(i)
        for j in conset:
            self.Text1.insert(tk.END,"{}\t\t         |             {}\n".format(j,p_list.count(j)))
        

    def AddStock(self):
        root.destroy()
        import stock
        stock.stock_GUI()

    def Reset(self):
        self.Text1.delete("1.0",END)

    def Back(self):
        root.destroy()
        import welcome
        welcome.welcome_GUI()

 
if __name__ == '__main__':
    inventory_GUI()
