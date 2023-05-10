import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image
import sqlite3

# create database and table
conn = sqlite3.connect('Voitures.db')
c = conn.cursor()



def Delete_car():
    # Get the selected item from the treeview
    selected_item = tree.selection()[0]
    values = tree.item(selected_item)['values']
    if values[1] == '':
        messagebox.showerror('Error', 'Please select a valid car')
        return
    # Check if the car is available
    if values[6] == 0:
        messagebox.showerror("", "Cannot delete this car because it is currently rented. Please cancel the contract first.")
        return

    # Ask the user if they are sure they want to delete the car
    answer = messagebox.askquestion("Delete Car", f"Are you sure you want to delete car {values[0]} {values[1]}?")

    if answer == "yes":
        # Update the car's availability and renter_id in the database
        car_id = int(tree.item(selected_item)['text'])
        c.execute("DELETE FROM voiture WHERE id= ?", (car_id,))
        conn.commit()  # commit the changes to the database

        # Remove the car from the treeview
        tree.delete(selected_item)

        messagebox.showinfo("", "Car deleted successfully.")

# create tkinter window
root = tk.Tk()
root.geometry("1000x800")


# Create a Label widget to display the menu title
title_label = tk.Label(root, text="Delete a car", font=("Helvetica", 24), bg="#CD5C5C", fg="white")
title_label.pack(side=tk.TOP, fill=tk.X)

# Define custom colors
bg_color = '#DC143C'
fg_color = 'peru'
heading_bg_color = '#34495E'
heading_fg_color = 'peru'
style = ttk.Style(root)
style.theme_use('default')
style.configure('Custom.Treeview', background='#F08080', font=('bookman', 10), rowheight=30)

# create table
tree = ttk.Treeview(root, columns=('marque', 'modele', 'carburant', 'places', 'transmission', 'prix', 'disponible'), style='Custom.Treeview')
tree.heading('#0', text='ID', anchor='center')
tree.heading('#1', text='Marque', anchor='center')
tree.heading('#2', text='Modele', anchor='center')
tree.heading('#3', text='Carburant', anchor='center')
tree.heading('#4', text='Places', anchor='center')
tree.heading('#5', text='Transmission', anchor='center')
tree.heading('#6', text='Prix', anchor='center')
tree.heading('#7', text='Disponible', anchor='center')

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
tree.tag_configure('Custom.Treeview.Heading', background=heading_bg_color, foreground=heading_fg_color, font=('bookman', 10, 'bold'))

# Add the treeview to the main window
tree.pack(fill='both', expand=True)

# fetch car details from database
c.execute("SELECT * FROM voiture")
cars =c.fetchall()

# populate the table with car details
for car in cars:
    tree.insert('', 'end', text=car[0], values=(car[1], car[2], car[4], car[5], car[6], car[7], car[8]))
    tree.insert('', 'end', text='', values=('', '', '', '', '', '', ''))


tree.pack(side=tk.TOP, pady=10, padx=10)
def Go_back():
    root.destroy()
    import AdminMenu
# create button to add car to database
add_button = tk.Button(root, text='Delete Car', command=Delete_car,fg='floralwhite',  bg='#CD5C5C',font=('bookman', 20, 'bold'))
add_button.pack(side=tk.BOTTOM, pady=10)
add_button = tk.Button(root, text='<< Back To Admin Menu', command=Go_back,fg='floralwhite',  bg='#CD5C5C',font=('bookman', 20, 'bold'))
add_button.place(x=5,y=735)


root.mainloop()
