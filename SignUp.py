from tkinter import *
from PIL import Image, ImageTk             
from tkinter import messagebox
import sqlite3
import tkinter as tk 
import tkinter.ttk as ttk
from tqdm import tqdm
import threading
import time

conn=sqlite3.connect('Voitures.db')
conn.execute('''CREATE TABLE IF NOT EXISTS user
             (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,password TEXT);''')

def login():
    window.destroy()
    import Login
    
def save_user_data():
     
     username = user.get()
     password = code.get()
     conform_password =code2.get()

     if not (username and password and conform_password):
        messagebox.showerror("Error", "Please Complete All Fields")
        return

    # Vérification si le mot de passe et le mot de passe de confirmation sont identiques
     if password != conform_password:
        messagebox.showerror("Error", "Please Make Sure That The Passwords Match")
        return
        
    # Insertion des données dans la base de données
    
     conn.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
     conn.commit()
      
    # Affichage d'un message de confirmation
     messagebox.showinfo("Confirmation", "Registration Successful")   
    
thread = threading.Thread(target=save_user_data)
thread.start()    
    
window=Tk()
window.title("SignUp")
window.geometry('925x500+300+300')
window.configure(bg= '#fff')
window.resizable(False, False)
img = PhotoImage(file="signupp.png")    

Label (window, image=img, bg= 'white').place(x=235,y=40)


frame=Frame (window, width=800,height=900,bg="white")
frame.place(x=300,y=55)



heading=Label(frame,text="Sign Up And Drive Into The Future",fg="#7AA874",bg="white",font=('Bauhaus 93',17,'bold'))
heading.place(x=5,y=0)

def on_enter(e):
         user.delete(0,'end')

def on_leave(e):
        if user.get()=='':
         user.insert(0,"Username")
     

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Arial",10))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
Frame(frame, width=295,height=2,bg='#42855B').place(x=25,y=107)

    #password input
 
def on_enter(e):
      code.delete(0,'end')

def on_leave(e):
        if code.get()=='':
         code.insert(0,"Password")
    
     

code=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Arial",10))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)
Frame(frame, width=295,height=2,bg='#42855B').place(x=25,y=177)
Button(frame,width=39,pady=7,text="Sign Up",bg="#42855B",fg="white",border=0,command=save_user_data ).place(x=0,y=290)
label=Label(frame,text="I have an account",fg='black',bg="white",font=("Microsoft Yahei UI Light",10,"bold"))
label. place(x=68, y=360)
    #password 2 input
def on_enter(e):
         code2.delete(0,'end')

def on_leave(e):
        if code2.get()=='':
         code2.insert(0,"Conform Password")
     

code2=Entry(frame,width=25,fg='black',border=0,bg='white',font=("Arial",10))
code2.place(x=30,y=220)
code2.insert(0,"Conform Password")
code2.bind("<FocusIn>",on_enter)
code2.bind("<FocusOut>",on_leave)
Frame(frame, width=295,height=2,bg='#42855B').place(x=25,y=247)

login_i_have_account=Button(frame,width=6,text='Log In',border=0,bg="white",cursor='hand2',fg='#42855B',command=login )
login_i_have_account. place(x=200,y=355)
label=Label(window,text="© 2023  Mohamed Adaze-Yassine Amal-Walid Karkouri.All Rights Reserved.",fg='black',bg='white',font=('Microsoft YaHei UI Light',9,"bold"))
label.place(x=240, y=470)    
window.mainloop()  

