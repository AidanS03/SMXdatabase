from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def addRiderWindow():
    # Create popup window
    win = Toplevel()
    win.geometry("300x150")
    win.title("Enter Rider Name")
    win.grid()

    # Input field for rider name
    namelbl=Label(win, text="Name")
    namelbl.grid(column=0, row=0)
    input_field = Text(win, height=1, width=25)
    input_field.grid(column=0, row=1)

    # Function to handle the "Add" button
    def getText():
        rider_name = input_field.get(1.0, "end-1c").strip()  # Get text and strip extra spaces/newlines
        if rider_name:  # Check if input is not empty
            print(f"Rider name entered: {rider_name}")
            # Here, you can add the logic to insert the rider into the database
            try:
                mycursor.execute("INSERT INTO rider (Name) VALUES (%s)", (rider_name,))
                mydb.commit()
                messagebox.showinfo("Success", f"Rider '{rider_name}' added to the database!")
                win.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid name.")

    # Add button to trigger getText
    addButton = Button(win, text="Add", command=getText)
    addButton.grid(column=4, row=2)

# Function to list riders
def getRiders():
    # Use cursor to execute query
    mycursor.execute("SELECT * FROM rider")

    # Fetch results of query
    myresult = mycursor.fetchall()

    # Add header for rider info
    txt.insert(END, "RiderID | Name | Age | Class | Nationality | Points\n")
    txt.insert(END, "-" * 50 + "\n")

    # Print query results to tkinter window
    for x in myresult:
        txt.insert(END, " | ".join(map(str, x)) + "\n")

# Connect to a database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2024FAHickory",
    database="2024SMX")

# Create a cursor
mycursor = mydb.cursor()

# Set up tkinter window
root = Tk()
root.geometry("700x350")
root.title("2025 SMX Database")

frame = ttk.Frame(root, padding=10)
frame.grid()

# Add labels and buttons
ttk.Label(frame, text="2025 SMX Database Management").grid(column=0, row=0, columnspan=3)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=5, row=5)
ttk.Button(frame, text="Get Riders", command=getRiders).grid(column=1, row=1)
ttk.Button(frame, text="Add Rider", command=addRiderWindow).grid(column=0, row=1)

# Text widget to display rider information
txt = Text(root, height=10, width=60)
txt.grid(column=0, row=2, columnspan=3)

root.mainloop()
