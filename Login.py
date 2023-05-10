import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


# create database and table
conn = sqlite3.connect('Voitures.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
conn.commit()


def signup():
    root.destroy()
    import SignUp



# create login function
def login():
    username = user.get()
    password = code.get()
    if not(username and password ):
        messagebox.showerror('Error', 'Please Complete All Fields')
        return
        # check if user exists in database
    cursor = conn.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
    rows = list(cursor)
    
    if len(rows) > 0:
        messagebox.showinfo("Success", "Login Successful.")

        if user:
            root.destroy()
        import Menu
    else:
            # show error message
            error_message = messagebox.showerror("Error", "Invalid Username Or Password!")


def Log_As_Admin():
    username = user.get()
    password = code.get()
    if username == "" or password == "":
        messagebox.showerror('Error', 'Please Complete All Fields')
    else:
        if username == "admin" and password == "123":
            
            root.destroy()
            import AdminMenu
        else:
            messagebox.showerror('Error', 'Private Access - Only For Admins!')


# create main window
root =tk.Tk()
root.title("Login Page")
root.geometry('925x500+300+300')
root.configure(bg="#fff")
root.resizable(False,False)
img = PhotoImage(file="electric-carr.png")    
img2= PhotoImage(file="green-technology.png")  
img3= PhotoImage(file="leaf.png")    
img4= PhotoImage(file="world.png")     
frame1=Frame(root,width=800,height=900,bg="white")
frame1.place(x=300,y=55)


heading=Label(frame1,text=' Rent Your Hybrid Car',fg='#2A2F4F' ,bg="white",font=('Bauhaus 93',25,'bold'))
heading. place(x=11, y=0)

Label (root, image=img, bg= 'white').place(x=250,y=40)
Label (root, image=img2, bg= 'white').place(x=655,y=42)      
Label (root, image=img3, bg= 'white').place(x=680,y=303)  
Label (root, image=img4, bg= 'white').place(x=40,y=200)    
      ##### User input
def on_enter(e):
          user.delete(0,'end')
def on_leave(e):
          name=user.get()
          if name=='':
              user.insert(0,'Username')
global user       
user = Entry(frame1,width=25, fg='black' ,border=0,bg="white",font=('Microsoft YaHei UI Light',13))
user.place(x=30, y=90)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame1,width=295,height=2, bg='black').place(x=25,y=120)
    
      ##### password
      
def on_enter(e):
          code.delete(0,'end')
def on_leave(e):
          name=code.get()
          if name=='':
              code.insert(0,'Password')
global code        
code = Entry(frame1,width=25, fg='black',border=0,bg="white", font=('Microsoft YaHei UI Light',13),show="*") 
code.place(x=30,y=160) 
code.insert(0,"Password")
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>', on_leave)
      
Frame(frame1,width=295,height=2, bg='black').place(x=25,y=190)
      #####Button Login
Button(frame1,width=35, pady=7,text='Log In' ,bg='#917FB3' ,fg='white',border=0,command=login, font=('Cooper',13)).place(x=15, y=235)
Button(frame1,width=35, pady=7,text='As Admin' ,bg='#E5BEEC' ,fg='white',border=0,command=Log_As_Admin, font=('Cooper',13)).place(x=15, y=290)

      ####Button Signup
sign_up1= Button(frame1,width=6,text='Sign up' ,border=0,bg='white',cursor='hand2',fg='#0A4D68',command=signup )
sign_up1.place(x=220,y=344)
      
label=Label(frame1,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9,"bold"))
label.place(x=60, y=350)
label=Label(root,text="© 2023  Mohamed Adaze-Yassine Amal-Walid Karkouri.All Rights Reserved.",fg='black',bg='white',font=('Microsoft YaHei UI Light',9,"bold"))
label.place(x=240, y=470)
root.mainloop()  