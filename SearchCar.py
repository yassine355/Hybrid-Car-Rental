import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image
import sqlite3

# create database and table
conn = sqlite3.connect('Voitures.db')
cursor = conn.cursor()

# create a tkinter window
root = tk.Tk()
root.title("Available Cars")
root.geometry("1500x900")
root.resizable(False,False)


title_label = tk.Label(root, text="-------- Available CARS --------", font=("Bauhaus 93", 30), bg="#99A98F", fg="white")
title_label.pack(side=tk.TOP, fill=tk.X)
title_label.config(height=10)


# create a label for the ComboBox
attributes_label = tk.Label(root, text="Attribute:", font=("Broadway", 20, "bold"), bg="#99A98F", fg="white")
attributes_label.place(x=250, y=16)

# create a ComboBox for selecting the attribute
attributes = ttk.Combobox(root, font=("MingLiU_HKSCS-ExtB", 13,"bold"), width=15)
attributes['values'] = ("marque", "modele", "carburant", "places", "transmission", "prix", "disponible")

attributes.place(x=450, y=24)
attributes.current(0)

# create a label for the input box
input_label = tk.Label(root, text="Value:", font=("Broadway", 20, "bold"), bg="#99A98F", fg="white")
input_label.place(x=700, y=16)

# create an input box for entering the value
input_box = tk.Entry(root, font=("MingLiU_HKSCS-ExtB", 13,"bold"), width=15)
input_box.place(x=830, y=25)


# change the background color
root.configure(bg='blue')

# set the window size


# create a canvas to display the cars
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

# set the canvas width and height
canvas_width = 600
canvas_height = 400
canvas.config(width=canvas_width, height=canvas_height,background="#FFF8DE")





# create a list to store the car image objects
car_images = []

# function to filter cars based on attribute and value
def filter_cars():
    # get the selected attribute and value from the input box
    
    attribute = attributes.get()
    value = input_box.get()
    if not value:
        messagebox.showwarning("Error", "Please Enter a Value!")
        return  # exit the function if input is empty

    # fetch car details from database
    cursor.execute(f"SELECT * FROM voiture WHERE {attribute} = ?", (value,))
    cars = cursor.fetchall()

    # delete all the previous car frames from the canvas
    canvas.delete("all")

    # create a frame to hold the car frames
    cars_frame = tk.Frame(canvas)

    # add a scrollbar to the canvas
    scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # display each car with its attributes that match the filter
    for i, car in enumerate(cars):
        # create a frame for the car
        car_frame = tk.Frame(cars_frame, padx=25, pady=30,background="#FFF8DE")
        car_frame.pack(side="top", fill="x", pady=10, padx=10)

        # load the car image and resize it
        image = Image.open(car[3])
        image = image.resize((500, 300), Image.LANCZOS)
        car_image = ImageTk.PhotoImage(image)

        # create a label to display the car image
        image_label = tk.Label(car_frame, image=car_image)
        image_label.image = car_image  # keep a reference to prevent the image from being garbage collected

        # create a label to display the car attributes
        attributes_label = tk.Label(car_frame, text=f"Marque: {car[1]}\n\nModèle: {car[2]}\n\nCarburant: {car[4]}\n\nPlaces: {car[5]}\n\nTransmission: {car[6]}\n\nPrix: {car[7]}\n\nDisponible: {car[8]}", fg='black', font=("bookman", 13, "bold"))

        # add the car image and attributes labels to the frame
        image_label.grid(row=0, column=0, sticky="w")
        attributes_label.grid(row=0, column=1, sticky="e")

        # add the car image to the list of car image objects
        car_images.append(car_image)

    # add the cars frame to the canvas
    canvas.create_window((0, 0), window=cars_frame)

    # update the canvas scroll region
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


Fiter_button= tk.Button(root, text="Search" ,command=filter_cars, fg="white",font=("Bauhaus 93", 15, "bold"),bg="#99A98F")
Fiter_button.place(x=1150, y=15)

def Go_back():
    root.destroy()
    import Menu 
    
back_butt=tk.Button(root, text="<< Back To Menu", command=Go_back, width=15, height=1,bg="#99A98F",fg="white",font=("MingLiU_HKSCS-ExtB",15,"bold"))
back_butt.place(x=5,y=860)
root.mainloop()


