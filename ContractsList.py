import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image
import sqlite3


conn = sqlite3.connect('Voitures.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS voiture
(id INTEGER PRIMARY KEY AUTOINCREMENT,
marque VARCHAR(255),
modele VARCHAR(255),
image VARCHAR(255),
carburant VARCHAR(255),
places INTEGER,
transmission VARCHAR(255),
prix FLOAT,
disponible BOOLEAN)''')

#create tkinter window
root = tk.Tk()
root.geometry("1000x400")

#Create a Label widget to display the menu title
title_label = tk.Label(root, text="Contracts List", font=("black", 24), bg="#F0FFFF", fg="grey")
title_label.pack(side=tk.TOP, fill=tk.X)

#Define custom colors
bg_color = '#DC143C'
fg_color = 'peru'
heading_bg_color = '#34495E'
heading_fg_color = 'peru'
style = ttk.Style(root)
style.theme_use('default')
style.configure('Custom.Treeview', background='#F0FFFF', font=('bookman', 10), rowheight=30)

#create table
tree = ttk.Treeview(root, columns=('Renter id', 'Car id', 'Car Name', 'Car Model', 'Num facture','Date','Date fin'), style='Custom.Treeview')
tree.heading('#0', text='Contract Id', anchor='center')
tree.heading('#1', text='Renter id', anchor='center')
tree.heading('#2', text='Car id', anchor='center')
tree.heading('#3', text='Car Name', anchor='center')
tree.heading('#4', text='Car Model', anchor='center')
tree.heading('#5', text='Num Facture', anchor='center')
tree.heading('#6', text='Date de début', anchor='center')
tree.heading('#7', text='Date de fin', anchor='center')

##Set column width
tree.column('#0', width=50, anchor='center')
tree.column('#1', width=100, anchor='center')
tree.column('#2', width=100, anchor='center')
tree.column('#3', width=100, anchor='center')
tree.column('#4', width=100, anchor='center')
tree.column('#5', width=100, anchor='center')
tree.column('#6', width=100, anchor='center')
tree.column('#7', width=100, anchor='center')

#Apply custom styles
tree.tag_configure('Custom.Treeview', background=bg_color, foreground=fg_color)
tree.tag_configure('Custom.Treeview.Heading', background=heading_bg_color, foreground=heading_fg_color, font=('bookman', 10, 'bold'))

#Add the treeview to the main window
tree.pack(fill='both', expand=True)

#fetch contract details from database
c.execute("SELECT * FROM contrats")
contrats = c.fetchall()

#populate the table with contract details
for contract in contrats:
 tree.insert('', 'end', text=contract[0], values=(contract[1], contract[2], contract[3], contract[4], contract[5], contract[6],contract[7]))
tree.insert('', 'end', text='', values=('', '', '', '', '', '', ''))

tree.pack(side=tk.TOP, pady=10, padx=10)

root.mainloop()

conn.close()