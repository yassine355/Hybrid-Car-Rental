
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from PIL import ImageTk, Image
from tkinter import Label, PhotoImage, messagebox

def GoTo_AddCar():
    root.destroy()
    import AddCar

    
def GoTo_Delete():
    import Delete

def GoTo_Factures():
    import FacturesList

def GoTo_Contracts():
    import ContractsList

def Log_out():
    confirm = messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?")
    if confirm:
     conn.close()
     root.destroy()
     import Login
    
   

# Connect to the database
conn = sqlite3.connect('cars.db')
c = conn.cursor()


root = tk.Tk()
root.title("Menu")
root.geometry("1000x800")
root.resizable(False, False)
root.config(bg="white")
img = PhotoImage(file="settings.png")    
Label (root, image=img, bg= 'white').place(x=455,y=210)
img2 = PhotoImage(file="panda.png")    
Label (root, image=img2, bg= 'white').place(x=430,y=595)

title_label = tk.Label(root, text="----------- Cars Management System -----------", font=("Bauhaus 93", 24), bg="#2C3639", fg="white")
title_label.place(x=0, y=0, relwidth=1, height=200)

button1 = tk.Button(root, text="------------ ADD CAR ------------" ,command=GoTo_AddCar, bg="#3F4E4F",fg="#F4EEE0",font=("MingLiU_HKSCS-ExtB", 13, "bold"))
button1.place(x=330, y=350, width=350, height=40)


button3 = tk.Button(root, text="---------- DELETE CAR ----------",command=GoTo_Delete,bg="#3F4E4F",fg="#F4EEE0",font=("MingLiU_HKSCS-ExtB", 13, "bold"))
button3.place(x=330, y=400, width=350, height=40)

button4 = tk.Button(root, text="------ SHOW FACTURES LIST ------",command=GoTo_Factures,bg="#3F4E4F",fg="#F4EEE0",font=("MingLiU_HKSCS-ExtB", 13, "bold"))
button4.place(x=330, y=450, width=350, height=40)

button4 = tk.Button(root, text="----- SHOW CONTRACTS LIST -----",command=GoTo_Contracts,bg="#3F4E4F",fg="#F4EEE0",font=("MingLiU_HKSCS-ExtB", 13, "bold"))
button4.place(x=330, y=500, width=350, height=40)

button5 = tk.Button(root, text=". LOG OUT . ",command=Log_out,bg="black",fg="white",font=("MingLiU_HKSCS-ExtB", 13, "bold"))
button5.place(x=330, y=700, width=350, height=40)


root.mainloop()


conn.close()
