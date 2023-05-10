import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image
import sqlite3
from docxtpl import DocxTemplate
# create database and table
conn = sqlite3.connect('Voitures.db')
cursor = conn.cursor()

# create voiture table
cursor.execute("""CREATE TABLE IF NOT EXISTS voiture (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                marque TEXT,
                modele TEXT,
                carburant TEXT,
                places INTEGER,
                prix REAL
               
                )""")

# create tkinter window
root1 = tk.Tk()
root1.geometry("1000x800")
root1.resizable(False,False)
# Create a Label widget to display the menu title
title_label = tk.Label(root1, text="---------- Factures List ----------", font=("Bauhaus 93", 30), bg="#F39189", fg="white",height=5)
title_label.pack(side=tk.TOP, fill=tk.X)

# Define custom colors
bg_color = '#DC143C'
fg_color = 'peru'
heading_bg_color = '#34495E'
heading_fg_color = 'peru'
style = ttk.Style(root1)
style.theme_use('default')
style.configure('Custom.Treeview', background='#BB8082', font=('MingLiU_HKSCS-ExtB', 12,"bold"), rowheight=30)

# create table
tree = ttk.Treeview(root1, columns=('Renter id', 'Renter Name', 'Car id', 'Car Name', 'Car Model', 'Price($)', 'Type payement'), style='Custom.Treeview')
tree.heading('#0', text='ID facture', anchor='center')
tree.heading('#1', text='Renter id', anchor='center')
tree.heading('#2', text='Renter Name', anchor='center')
tree.heading('#3', text='Type Payement', anchor='center')
tree.heading('#4', text='Car Id', anchor='center')
tree.heading('#5', text='Price($)', anchor='center')
tree.heading('#6', text='Car Name', anchor='center')
tree.heading('#7', text='Car Model', anchor='center')

# Set column width
tree.column('#0', width=50, anchor='center')
tree.column('#1', width=100, anchor='center')
tree.column('#2', width=100, anchor='center')
tree.column('#3', width=100, anchor='center')
tree.column('#4', width=100, anchor='center')
tree.column('#5', width=100, anchor='center')
tree.column('#6', width=100, anchor='center')
tree.column('#7', width=100, anchor='center')

# Apply custom styles
tree.tag_configure('Custom.Treeview', background=bg_color, foreground=fg_color)
tree.tag_configure('Custom.Treeview.Heading', background="#BB8082", foreground=heading_fg_color, font=('bookman', 10, 'bold'))

# Add the treeview to the main window
tree.pack(fill='both', expand=True)

# fetch facture details from database
cursor.execute("SELECT * FROM factures")
factures = cursor.fetchall()

# populate the table with facture details
for facture in factures:
    tree.insert('', 'end', text=facture[0], values=(facture[1], facture[2], facture[3], facture[4], facture[5], facture[6], facture[7]))
    tree.insert('', 'end', text='', values=('', '', '', '', '', '', ''))

tree.pack(side=tk.TOP, pady=10, padx=10)

def Go_back():
    root1.destroy()
    import AdminMenu

back=tk.Button(root1, text="<< Back To Menu", command=Go_back,bg="#6E7582",fg="#FFF5E4",font=('Ravie') ,width=15 ,height=2)
back.place(x=9,y=728)
root1.mainloop()
