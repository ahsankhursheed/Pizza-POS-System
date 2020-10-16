import tkinter as tk
from tkinter import *
import os
from tkinter import messagebox
from PIL import Image,ImageTk



def load_login_GUI():

    global root
    root = tk.Tk()

    # canvas=Canvas(root,width=1580,height=1424)
    # image=ImageTk.PhotoImage(Image.open("your_pic.jpg"))
    # canvas.create_image(0,0,anchor=NW,image=image)
    # canvas.pack()
    
    top = LoginGUI (root)
    root.mainloop()



class LoginGUI:
    def __init__(self, top=None):

       _bgcolor = '#d9d9d9'  
       _fgcolor = '#000000' 
       _compcolor = '#d9d9d9' 
       _ana1color = '#d9d9d9' 
       _ana2color = '#ececec'

       top.geometry("498x349+463+234")
       top.minsize(120, 1)
       top.maxsize(1370, 749)
       top.resizable(1, 1)
       top.title("Login Page")
       top.configure(relief="raised")
       top.configure(background="#d9d9d9")
       top.configure(highlightbackground="#f0f0f0f0f0f0")
       top.configure(highlightcolor="black")

       self.Label1 = tk.Label(top)
       self.Label1.place(relx=-0.08, rely=0.029, height=51, width=571)
       self.Label1.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 20 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#f0f0f0f0f0f0",highlightcolor="#646464646464",relief="raised",text='''PIZZA POS SYSTEM''')

       self.Label2 = tk.Label(top)
       self.Label2.place(relx=0.141, rely=0.43, height=31, width=126)
       self.Label2.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 16 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",text='''USERNAME''')

       self.Label3 = tk.Label(top)
       self.Label3.place(relx=0.207, rely=0.229, height=41, width=306)
       self.Label3.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI Black} -size 18 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",relief="groove",text='''ADMINSTRATOR LOGIN''')

       self.Label2_1 = tk.Label(top)
       self.Label2_1.place(relx=0.141, rely=0.602, height=31, width=126)
       self.Label2_1.configure(activebackground="#f9f9f9",activeforeground="black",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 16 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",text='''PASSWORD''')

       self.Button1 = tk.Button(top)
       self.Button1.place(relx=0.442, rely=0.774, height=44, width=97)
       self.Button1.configure(command=self.ConfirmLogin, activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 16 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''LOGIN''')

       self.Button1_3 = tk.Button(top)
       self.Button1_3.place(relx=0.663, rely=0.774, height=44, width=97)
       self.Button1_3.configure(command=self.Exit,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",font="-family {Segoe UI} -size 16 -weight bold -slant roman -underline 0 -overstrike 0",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''EXIT''')

       self.Entry1 = tk.Entry(top)
       self.Entry1.place(relx=0.422, rely=0.43,height=40, relwidth=0.45)
       self.Entry1.configure(background="white",disabledforeground="#a3a3a3",font="18",foreground="#000000",insertbackground="black")

       self.Entry1_1 = tk.Entry(top)
       self.Entry1_1.place(relx=0.422, rely=0.602,height=40, relwidth=0.45)
       self.Entry1_1.configure(background="white",disabledforeground="#a3a3a3",font="18",foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",insertbackground="black",selectbackground="blue",selectforeground="white",show="*")
       


    def Exit(self):
        root.destroy()

    def ConfirmLogin(self):
        infile = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\username.txt", "r")
        con1 = infile.read()
        con11 = con1.split()
        infile2 = open("C:\\Users\\ahsan\\Desktop\\Pizza POS System\\password.txt", "r")
        con2 = infile2.read()
        con22 = con2.split()
        infile.close()
        if self.Entry1.get() == "" or self.Entry1_1.get() == "":
            messagebox.showerror("", "Both Fields are required to login")
        elif self.Entry1.get() == con11[0] and self.Entry1_1.get() == con22[0]:
            messagebox.showinfo("Authentication", "Logged in Successfully, Click Ok to continue")
            root.destroy()
            import welcome
            welcome.welcome_GUI()
        elif self.Entry1.get() == con11[1] and self.Entry1_1.get() == con22[1]:
            messagebox.showinfo("Authentication", "Logged in Successfully, Click Ok to continue")
            root.destroy()
            import welcome
            welcome.welcome_GUI()
        elif self.Entry1.get() == con11[2] and self.Entry1_1.get() == con22[2]:
            messagebox.showinfo("Authentication", "Logged in Successfully, Click OK to continue")
            root.destroy()
            import welcome
            welcome.welcome_GUI()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")



if __name__ == '__main__':
    load_login_GUI()
    
    


