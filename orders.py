import tkinter as tk
from tkinter import *
import datetime
from tkinter import messagebox
import random
from pathlib import Path

def orders_GUI():
   
   global root
   root = tk.Tk()
   top = OrdersGUI (root)
   root.mainloop()


class OrdersGUI:
    def __init__(self, top=None):

        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec' 
        font11 = "-family {Segoe UI Black} -size 20 -weight bold"
        font13 = "-family {Segoe UI Black} -size 16 -weight bold"
        font14 = "-family {Segoe UI Black} -size 17 -weight bold"

        top.geometry("802x582+300+85")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Order")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.261, rely=0.019, height=61, width=369)
        self.Label1.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",relief="groove",text='''ORDERS''')

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.611, rely=0.155, height=42, width=301)
        self.Label2_1.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 20 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",relief="raised",text='''BILLING COUNTER''')

        self.Label2_9 = tk.Label(top)
        self.Label2_9.place(relx=0.05, rely=0.223, height=52, width=80)
        self.Label2_9.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font=font11,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",text='''ITEM''')

        self.Label2_10 = tk.Label(top)
        self.Label2_10.place(relx=0.012, rely=0.378, height=42, width=144)
        self.Label2_10.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font=font11,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",text='''QUANTITY''')
    
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.362, rely=0.808, height=74, width=187)
        self.Button1.configure(command=self.GenerateBill,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font=font14,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''GENERATE BILL''')
    
        self.Button1_17 = tk.Button(top)
        self.Button1_17.place(relx=0.187, rely=0.808, height=74, width=127)
        self.Button1_17.configure(command=self.Reset,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font=font14,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''RESET''')
    
        self.Button1_18 = tk.Button(top)
        self.Button1_18.place(relx=0.012, rely=0.808, height=74, width=127)
        self.Button1_18.configure(command=self.Back,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font=font14,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''BACK''')
    
        self.Text2 = tk.Text(top)
        self.Text2.place(relx=0.616, rely=0.225, relheight=0.756, relwidth=0.363)
        self.Text2.configure(background="white",font="-size 12 -weight bold",foreground="black",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")

        self.Entry1_4 = tk.Entry(top)
        self.Entry1_4.place(relx=0.2, rely=0.223,height=60, relwidth=0.367)
        self.Entry1_4.configure(background="white",disabledforeground="#a3a3a3",font="26",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white")

        self.Entry1_1 = tk.Entry(top)
        self.Entry1_1.place(relx=0.2, rely=0.361,height=60, relwidth=0.367)
        self.Entry1_1.configure(background="white",disabledforeground="#a3a3a3",font="26",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white")

        self.Button1_2 = tk.Button(top)
        self.Button1_2.place(relx=0.175, rely=0.498, height=64, width=157)
        self.Button1_2.configure(command=self.AddToCart,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font=font13,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''ADD TO CART''')
    
        self.Button1_3 = tk.Button(top)
        self.Button1_3.place(relx=0.387, rely=0.498, height=64, width=157)
        self.Button1_3.configure(command=self.ViewCart,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font=font13,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''VIEW CART''')

    def Back(self):
        
        import welcome
        file_path = Path("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt")
        if (file_path.stat().st_size == 0) == True:
            root.destroy()
            welcome.welcome_GUI()
        
        else:
            a=messagebox.askyesno("Attention", "Order in process. Do you want to discard current order ?")
            if a>0:
                self.Text2.delete("1.0", "end")
                
                infile = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt", "w")
                infile.close()

                root.destroy()
                welcome.welcome_GUI()

            else: 
                return

    def AddToCart(self):
        

        try:
            int(self.Entry1_1.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid Quantity!")
            return

        if self.Entry1_4.get()=="" or self.Entry1_1.get()=="":
            messagebox.showerror("Error", "Both fields are required.")
        else:
            infile = open("StockItems.txt", "r")
            con = infile.read().split("\n")
            infile.close()
            con.pop()
            cart_file = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt", "r")
            con2 = cart_file.read().split("\n")
            cart_file.close()
            con2.pop()
            cart_file1 = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt", "a")
            if self.Entry1_4.get() not in con:
                messagebox.showinfo("Attention", "Item not available.")
            elif int(self.Entry1_1.get()) > con.count(self.Entry1_4.get()):
                messagebox.showinfo("Attention", "Stock not availabe in required quantity.")
            elif self.Entry1_4.get().strip() not in con:
                messagebox.showinfo("Attention", "Item not available.")
            elif (con2.count(self.Entry1_4.get().strip()) + int(self.Entry1_1.get())) > con.count(self.Entry1_4.get().strip()):
                messagebox.showinfo("Attention","Some of the items are already in your cart. The additional required items are not enough in stock.")
            else:
                for i in range(int(self.Entry1_1.get())):
                    cart_file1.write(self.Entry1_4.get().strip()+"\n")
                messagebox.showinfo("Notification", "Successfully Added items to the Cart")
            cart_file1.close()
            self.Entry1_4.delete(0, "end")
            self.Entry1_1.delete(0, "end")


  

    def GenerateBill(self):

        
        file2_path = Path("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt")
        if (file2_path.stat().st_size == 0) == True:
            messagebox.showinfo("Attention", "Cart Empty! Add some items to the cart to generate the bill.")

        else:
            self.Text2.delete("1.0", "end")
            bill_number=StringVar()
            num=random.randint(3400,9999)
            bill_number.set(str(num))  
            self.Text2.insert(END, "===============================\n                 CALIFORNIA PIZZA ===============================\n       || BILLING RECEIPT     S# {} ||\n===============================\n".format(bill_number.get()))
            timing = datetime.datetime.now()
            order_date = timing.strftime(" %Y-%m-%d")
            order_time= timing.strftime("%H:%M:%S")
            self.Text2.insert(END," Date:{}       Time: {}".format(order_date,order_time))
            self.Text2.insert(END,"\n\n           ITEMS                       QUANTITY\n\n")
            


            cart_set = set()
            infile = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\StockItems.txt", "r")
            con = infile.read().split("\n")
            infile.close()
            infile2 = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt", "r")
            con2 = infile2.read().split("\n")
            infile2.close()
            con.pop(), con2.pop()
            for j in con2:
                con.remove(j)
                cart_set.add(j)
            outfile = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\StockItems.txt", "w")
            for k in con:
                outfile.write(k+"\n")
            outfile.close()
            open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\CartItems.txt", "w").close()
            for l in cart_set:
                self.Text2.insert(END, "{}\t\t|\t{}\n".format(l, con2.count(l)))

            a=messagebox.askyesno("Save Bill", "Do you want to save the billing information ?")
            if a>0:
                bill_data= self.Text2.get("1.0",END)
                infile=open("bills/"+str(bill_number.get())+" .txt","w")
                infile.write(bill_data)
                infile.close()
            else:
                pass    
            

    def ViewCart(self):
        root.destroy()
        import cart
        cart.cart_GUI()


    def Reset(self):

        self.Text2.delete("1.0", "end")
        self.Entry1_4.delete(0,"end")
        self.Entry1_1.delete(0,"end")

if __name__ == '__main__':
    orders_GUI()
 
 

