import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image
import importlib

# create database and table
mydb = sqlite3.connect("Voitures.db")
mycursor = mydb.cursor()
mycursor.execute("""CREATE TABLE IF NOT EXISTS voiture 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                marque TEXT, 
                modele TEXT, 
                image TEXT, 
                carburant TEXT, 
                places INTEGER, 
                transmission TEXT, 
                prix REAL, 
                disponible INTEGER)""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS user 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT, 
                password TEXT)""")


mycursor.execute("""CREATE TABLE IF NOT EXISTS factures 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                renter_id INTEGER, 
                Renter_Name TEXT, 
                Type_payement TEXT,
                Car_id INTEGER,
                Montant REAL,
                Car_Name TEXT,
                Car_Model TEXT,
                date_debut TEXT,
                date_fin TEXT,
                FOREIGN KEY (renter_id) REFERENCES user(id),
                FOREIGN KEY (Car_id) REFERENCES voiture(id))""")


mydb.commit()

# fetch car details from database
mycursor.execute("SELECT * FROM voiture")
cars = mycursor.fetchall()

mycursor.execute("PRAGMA table_info(voiture)")
columns = mycursor.fetchall()
column_names = [col[1] for col in columns]
if "Renter_id" not in column_names:
    mycursor.execute("ALTER TABLE voiture ADD COLUMN Renter_id INTEGER")
   
import datetime

def book_car():
    
    
    
    # Get the selected item from the treeview
    selected_item = tree.selection()[0]
    values = tree.item(selected_item)['values']
    if values[1] == '':
         messagebox.showerror('Error', 'Please select a valid car')
         return
    # If the car is not available, show an error message
    if not values[6]:
        messagebox.showerror('Error', 'This car is unavailable')
        return
    price = values[5]
    # Prompt the user for their username and password
    username = simpledialog.askstring('Login', 'Confirm Your Username:', parent=root)
    password = simpledialog.askstring('Login', 'Confirm Your Password:', parent=root, show='*')

    # Check if the username and password match a user in the database
    sql = "SELECT id FROM user WHERE username = ? AND password = ?"
    val = (username, password)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result is None:
        messagebox.showerror('Error', 'Invalid Username Or Password')
        return

    # Get the id of the matching user
    user_id = result[0]

    # Prompt the user for the payment type
    payment=''
    payment_type = simpledialog.askinteger('Payment', 'Enter Payment Type (1: Cash, 2: Credit Card, 3: Paypal):', parent=root)
    if payment_type == 1 :
        payment = 'Cash'
    elif payment_type == 2 :
        payment = 'Credit Card'
    elif payment_type == 3 :
        payment = 'Paypal'
    
    # Prompt the user for the end date of the booking
    end_date = simpledialog.askstring('Booking End Date', 'Enter The End Date Of The Booking (YYYY-MM-DD):', parent=root)
    try:
        end_datetime = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        if end_datetime < datetime.datetime.now():
            messagebox.showerror('Error', 'End date must be in the future')
            return
    except ValueError:
        messagebox.showerror('Error', 'Invalid date format')
        return

    # Convert the end date to a string in the correct format
    date_fin = end_datetime.strftime('%Y-%m-%d')

    # Update the car's availability and renter_id in the database
    car_id = int(tree.item(selected_item)['text'])
    sql = "UPDATE voiture SET disponible = 0, Renter_id = ? WHERE id = ?"
    val = (user_id, car_id)
    mycursor.execute(sql, val)
    
    # Insert the booking into the factures table
    sql = "INSERT INTO factures ('Renter_id', 'Renter_Name', 'Car_id', 'Car_Name', 'Car_Model', 'Montant', 'Type_payement') VALUES (?, ?, ?, ?, ?, ?, ?)"
    val = (user_id, username, payment, car_id,price,values[0],values[1])
    mycursor.execute(sql, val)

    # Insert the booking into the contrats table
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    # Convert the end date to a Date object
    date_fin = end_datetime.date()

    mydb.commit()  # commit the changes to the database

    # Update the treeview
    selected_item = tree.selection()[0]
    values = tree.item(selected_item)['values']
    tree.item(selected_item, values=(values[0], values[1], values[2], values[3], values[4], values[5], False, user_id, date_fin))

    messagebox.showinfo("Success", "Success! Your Car Reservation is Complete! Enjoy Your Ride!")


# create tkinter window
root = tk.Tk()
root.geometry("1000x800")
root.resizable(False,False)



# Create a Label widget to display the menu title
title_label = tk.Label(root, text="------------- DriveNow - Book Your Car in Seconds ------------", font=("Bauhaus 93", 24), bg="#472D2D", fg="white",height=5)
title_label.pack(side=tk.TOP, fill=tk.X)

# Define custom colors
bg_color = 'white'
fg_color = 'white'
heading_bg_color = '#553939'
heading_fg_color = 'white'
style = ttk.Style(root)
style.theme_use('default')
style.configure('Custom.Treeview', background='#FFF5E4',fg_color="#704F4F" ,font=('bookman', 13), rowheight=30)

tree = ttk.Treeview(root, columns=('marque', 'modele', 'carburant', 'places', 'transmission', 'prix', 'disponible'), style='Custom.Treeview')

tree.heading('#0', text='ID', anchor='center')
tree.heading('#1', text='Marque', anchor='center')
tree.heading('#2', text='Modele', anchor='center')
tree.heading('#3', text='Carburant', anchor='center')
tree.heading('#4', text='Places', anchor='center')
tree.heading('#5', text='Transmission', anchor='center')
tree.heading('#6', text='Prix ($)', anchor='center')
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
tree.tag_configure('Custom.Treeview', background="#FFF5E4", foreground="#FFF5E4")
tree.tag_configure('Custom.Treeview.Heading', background="#FFF5E4", foreground="#FFF5E4", font=('bookman', 14, 'bold'))

# Add the treeview to the main window
tree.pack(fill='both', expand=True)


# populate the table with car details
for car in cars:
    tree.insert('', 'end', text=car[0], values=(car[1], car[2], car[4], car[5], car[6], car[7], car[8]))
    tree.insert('', 'end', text='', values=('', '', '', '', '', '', ''))

tree.pack(side=tk.TOP, pady=10, padx=10)

# create button to add car to database
add_button = tk.Button(root, text='Book Car', command=book_car,fg='#704F4F',  bg='#FFF5E4',font=('Ravie', 20, 'bold'))
add_button.pack(side=tk.BOTTOM, pady=10)

def Go_back():
    root.destroy()
    import Menu


back=tk.Button(root, text="<< Back To Menu", command=Go_back,bg="#704F4F",fg="#FFF5E4",font=('Ravie') ,width=15 ,height=2)
back.place(x=5,y=728)
root.mainloop()




