import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox


# create database and table
mydb = sqlite3.connect("Voitures.db")
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS voiture (id INTEGER PRIMARY KEY, marque TEXT, modele TEXT, image TEXT, carburant TEXT, places INTEGER, transmission TEXT, prix REAL, disponible INTEGER)")

def Add_Car():
    marque=marque_entry1.get()
    modele=modele_entry1.get()
    image=image_entry1.get()
    carburant=Carb_combobox.get()
    place=place_entry1.get()
    transmission=trans_combobox.get()
    prix=prix_entry1.get()

    if marque=="" or modele=="" or image=="" or carburant=="" or place=="" or transmission=="" or prix=="":
        messagebox.showerror('Error' , 'Please Complete All Fields')

    else:     
        mycursor = mydb.cursor()
 
        # insert data into table
        sql = "INSERT INTO voiture (marque,modele, image, carburant, places, transmission, prix,disponible) VALUES (?, ?,?,?,?,?,?,?)"
        val = (marque ,modele, image ,carburant ,place, transmission, prix, 1)
        mycursor.execute(sql, val)
        mydb.commit()

        # show success message
        messagebox.showinfo("Succes", "Car Added Successfully.")


    

##window add Car

root2 = tk.Tk()
root2.title("Add Car")
root2.geometry("600x800")
root2.resizable(False, False)
root2.config(bg="#fff")
# create labels

AddCar=tk.Label(root2,text="Add A New Car To Your Collection",font=('OCR A', 25, 'bold'),fg='#FFF3E2',bg="#245953")

AddCar.pack(side=tk.TOP, fill=tk.X)
label_marque=tk.Label(root2, text="Marque: ",fg='#245953',bg="#fff",font=('Iceberg', 15, 'bold'))
label_marque.place(x=115, y=138)

label_modele=tk.Label(root2, text="Modele: ",fg='#245953',bg="#fff",font=('Iceberg', 15, 'bold'))
label_modele.place(x=115, y=199)

label_image=tk.Label(root2, text="Image (path): ",fg='#245953',bg="#fff",font=('Iceberg', 15, 'bold'))
label_image.place(x=115, y=260)

label_carburant=tk.Label(root2, text="Carburant: ",fg='#245953',bg="#fff",font=('Iceberg', 15, 'bold'))
label_carburant.place(x=115, y=321)

label_places=tk.Label(root2, text="Places: ",fg='#245953',bg="#fff",font=('Iceberg', 15, 'bold'))
label_places.place(x=115, y=382)

label_transmission=tk.Label(root2, text="Transmission: ",fg='#245953',bg="#fff",font=('Iceberg', 15, 'bold'))
label_transmission.place(x=110, y=433)

label_prix=tk.Label(root2, text="Prix: ",fg='#245953',bg="#fff",font=('Iceberg', 15, 'bold'))
label_prix.place(x=112, y=504)


# create entries
marque_entry1 = tk.Entry(root2,fg='black',font=('Iceberg', 15, 'bold'))
modele_entry1 = tk.Entry(root2,fg='black',font=('Iceberg', 15, 'bold'))
image_entry1 = tk.Entry(root2, fg='black',font=('Iceberg', 15, 'bold'))
Carb_combobox = ttk.Combobox(root2, values=['Gasoline', 'Hybrid', 'électrique'], font=('Iceberg', 15, 'bold'), foreground='white', style='TCombobox')
place_entry1 = tk.Entry(root2, fg='black',font=('Iceberg', 15, 'bold'))
trans_combobox = ttk.Combobox(root2, values=['Automatic', 'Manual'], font=('Iceberg', 15, 'bold'), foreground='white', style='TCombobox')
prix_entry1 = tk.Entry(root2, fg='black',font=('Iceberg', 15, 'bold'))



marque_entry1.place(x=270, y=138)
modele_entry1.place(x=270, y=199)
image_entry1.place(x=270, y=260)
Carb_combobox.place(x=270, y=321)
place_entry1.place(x=270, y=382)
trans_combobox.place(x=270, y=433)
prix_entry1.place(x=270, y=504)



# create submit button
AddBtn=tk.Button(root2, text="    Add +  ", command=Add_Car,fg='white',bg="#E49393",font=('Stencil', 17, 'bold'),width=10)
AddBtn.place(x=250, y=620)

def Go_back():
     root2.destroy()
     import AdminMenu 
      
      

back=tk.Button(root2, text="<< Back To Admin Menu", command=Go_back, width=20, height=1,font=("Stencil"),bg="#E49393",fg="white")
back.place(x=10,y=760)

root2.mainloop()


