import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image,ImageTk

def cart_GUI():
    
    global root
    root = tk.Tk()
    top = CartGUI (root)
    root.mainloop()

class CartGUI:
    def __init__(self, top=None):

        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec' 
        font10 = "-family {Segoe UI Black} -size 24 -weight bold"
        font11 = "-family {Segoe UI} -size 15"
        font12 = "-family {Segoe UI Black} -size 18 -weight bold"

        top.geometry("583x533+399+121")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Cart")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.343, rely=0.019, height=72, width=156)
        self.Label1.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font10,foreground="#000000",relief="ridge",text='''CART''')

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.257, rely=0.206, relheight=0.758, relwidth=0.707)
        self.Text1.configure(background="white",font=20,foreground="black",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")

        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.Text1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Text1.yview)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.034, rely=0.225, height=64, width=117)
        self.Button1.configure(command=self.ViewCart,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font=font12,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''VIEW''')
 
        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.034, rely=0.375, height=64, width=117)
        self.Button1_1.configure(command=self.Update_Cart,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 18 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''UPDATE''')
 
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
 
        self.Button1_2 = tk.Button(top)
        self.Button1_2.place(relx=0.034, rely=0.844, height=64, width=117)
        self.Button1_2.configure(command=self.Back,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 18 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''BACK''')
 
        self.Button1_3 = tk.Button(top)
        self.Button1_3.place(relx=0.034, rely=0.525, height=64, width=117)
        self.Button1_3.configure(command=self.Discard,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 18 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''DISCARD''')

    def ViewCart(self):
        self.Text1.delete("1.0", "end")
        self.Text1.insert(END, "=============================================\n")
        self.Text1.insert(END, "      ITEMS (SIZE)               |       QUANTITY\n")
        self.Text1.insert(END, "=============================================\n\t\t         |\n")
        conset = set()
        p_list = []
        infile = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt", "r")
        con = infile.read()
        infile.close()
        con2 = con.split("\n")
        con2.pop()
        for i in con2:
            conset.add(i)
            p_list.append(i)
        for j in conset:
            self.Text1.insert(tk.END,"{}\t\t         |             {}\n".format(j,p_list.count(j)))
    
    def Update_Cart(self):
        root.destroy()
        import cart_update
        cart_update.Cart_GUI()

    def Discard(self):

        a=messagebox.askyesno("Attention", "Do you want to discard the current cart items ?")
        if a>0:
            self.Text1.delete("1.0", "end")
            infile=open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt","w")
            infile.close()
        else:
            pass

    def Back(self):
        root.destroy()
        import orders
        orders.orders_GUI()
 
if __name__ == '__main__':
    cart_GUI()
 
 

