import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from PIL import ImageTk, Image
from tkinter import Label, PhotoImage, messagebox

def GoTo_Search_Car() :
    root.destroy()
    import SearchCar

def GoTo_Cars_List() :
    root.destroy()
    import CarsList
    
    
def GoTo_book() :
    
    root.destroy()
    import Booking

def Log_out() :
    confirm = messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?")
    if confirm:
     conn.close()
     root.destroy()
     import Login


root = tk.Tk()
root.title("Menu")
root.geometry("1000x800")
root.resizable(False, False)
root.configure(bg= '#fff')
img = PhotoImage(file="user.png")    
Label (root, image=img, bg= 'white').place(x=430,y=110)
img2 = PhotoImage(file="rabbit.png")    
Label (root, image=img2, bg= 'white').place(x=450,y=600)


# Create a Label widget to display the menu title
title_label = tk.Label(root, text="------------- Drive Your Dream Car - A Premium Car Rental System -----------", font=("Bauhaus 93", 20), bg="#393646", fg="#F4EEE0")
title_label.place(x=0, y=0, relwidth=1, height=90)

# Connect to SQLite database
conn = sqlite3.connect('cars.db')
c = conn.cursor()

# Create three buttons
button1 = tk.Button(root, text="-----SHOW ALL CARS INFORMATIONS----" , command=GoTo_Cars_List,fg="#393646",bg="#F4EEE0",font=("MingLiU_HKSCS-ExtB", 13, "bold"))
button1.place(x=330, y=350, width=350, height=50)

button2 = tk.Button(root, text="---------SEARCH FOR A CAR---------", command=GoTo_Search_Car,fg="#393646",bg="#F4EEE0",font=("MingLiU_HKSCS-ExtB", 13, "bold"))
button2.place(x=330, y=420, width=350, height=50)

button3 = tk.Button(root, text="------------BOOK A CAR------------",command=GoTo_book,fg="#393646",bg="#F4EEE0",font=("MingLiU_HKSCS-ExtB", 13, "bold"))
button3.place(x=330, y=490, width=350, height=50)

button4 = tk.Button(root, text=". LOG OUT .",command=Log_out,fg="#F4EEE0",bg="#6D5D6E",font=("MingLiU_HKSCS-ExtB", 13, "bold"))
button4.place(x=330, y=700, width=350, height=50)

# Start the main event loop
root.mainloop()

# Close the SQLite connection when the program exits
conn.close()
