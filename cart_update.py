import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image,ImageTk

def Cart_GUI():

    global root
    root = tk.Tk()

    # canvas=Canvas(root,width=1370,height=749)
    # image=ImageTk.PhotoImage(Image.open("pizza5.1.jpg"))
    # canvas.create_image(0,0,anchor=NW,image=image)
    # canvas.pack()
        
    top = CartGUI (root)
    root.mainloop()

class CartGUI:
    def __init__(self, top=None):
        
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000' 
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'
        font9 = "-family {Segoe UI Black} -size 14 -weight bold"

        top.geometry("478x338+439+175")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Update")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=-0.257, rely=0.03, height=61, width=723)
        self.Label1.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 20 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",relief="raised",text='''UPDATE CART''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.081, rely=0.355, height=41, width=99)
        self.Label2.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 20 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",text='''ITEM''')

        self.Label2_2 = tk.Label(top)
        self.Label2_2.place(relx=0.038, rely=0.533, height=41, width=143)
        self.Label2_2.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 20 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",text='''QUANTITY''')
 
        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.343, rely=0.355,height=50, relwidth=0.594)
        self.Entry1.configure(background="white",disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 18 -weight normal -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white")
 
        self.Entry1_3 = tk.Entry(top)
        self.Entry1_3.place(relx=0.343, rely=0.533,height=50, relwidth=0.594)
        self.Entry1_3.configure(background="white",disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 17 -weight normal -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white")
 
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.341, rely=0.74, height=54, width=87)
        self.Button1.configure(command=self.AddCart,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''ADD''')
 
        self.Button1_4 = tk.Button(top)
        self.Button1_4.place(relx=0.753, rely=0.74, height=54, width=87)
        self.Button1_4.configure(command=self.Back,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''BACK''')
 
        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.538, rely=0.74, height=54, width=97)
        self.Button1_1.configure(command=self.Remove,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''REMOVE''')


    def AddCart(self):

        try:
            int(self.Entry1_3.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid Quantity!")
            return

        if self.Entry1.get()=="" or self.Entry1_3.get()=="":
            messagebox.showerror("Error", "Both fields are required to update Cart.")
        else:

            infile = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\StockItems.txt", "r")
            con = infile.read().split("\n")
            infile.close()
            con.pop()
            cart_file = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt", "r")
            con2 = cart_file.read().split("\n")
            cart_file.close()
            con2.pop()
            cart_file1 = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt", "a")
            if self.Entry1.get() not in con:
                messagebox.showinfo("Attention", "Item not available.")
            elif int(self.Entry1_3.get()) > con.count(self.Entry1.get()):
                messagebox.showinfo("Attention", "Stock not availabe in required quantity.")
            elif self.Entry1.get().strip() not in con:
                messagebox.showinfo("Attention", "Item not available.")
            elif (con2.count(self.Entry1.get().strip()) + int(self.Entry1_3.get())) > con.count(self.Entry1.get().strip()):
                messagebox.showinfo("Attention","Some of the items are already in your cart. The additional required items are not enough in stock.")
            else:
                for i in range(int(self.Entry1_3.get())):
                    cart_file1.write(self.Entry1.get().strip()+"\n")
                messagebox.showinfo("Notification", "Successfully Added items to the Cart")
            cart_file1.close()
        self.Entry1.delete(0,"end")
        self.Entry1_3.delete(0,"end")

    def Remove(self):

        try:
            int(self.Entry1_3.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid Quantity!")
            return

        if self.Entry1.get() == "" or self.Entry1_3.get() == "":
            messagebox.showerror("Error", "Both fields are required to update Cart.")
        else:
            infile = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt", "r")
            con = infile.read().split("\n")
            con.pop()
            infile.close()
        for i in range(int(self.Entry1_3.get())):
            con.remove(self.Entry1.get().strip())
            outfile = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt", "w")
        messagebox.showinfo("Notification", "Successfully Removed items from the Cart")    
        for i in con:
            outfile.write(i+"\n")
        outfile.close()
        self.Entry1.delete(0,"end")
        self.Entry1_3.delete(0,"end")
        

    def Back(self):
        root.destroy()
        import cart
        cart.cart_GUI()

if __name__ == '__main__':
    Cart_GUI()
 
 

