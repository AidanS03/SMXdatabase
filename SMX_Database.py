import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# function to list riders
def getRiders():
    # use cursor to execute query
    mycursor.execute("SELECT * FROM rider")

    # fetch results of query
    myresult = mycursor.fetchall()

    # Add header for rider info
    txt.insert(END, "RiderID Number Name Age Class Nationality Points\n")

    # print query results to tkinter window
    for x in myresult:
        txt.insert(END, x)
        txt.insert(END, "\n")

# connect to a database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2024FAHickory",
    database="2024SMX")

# create a cursor
mycursor = mydb.cursor()

# set up tkinter window
root = Tk()
root.geometry("700x350")
root.title("2025 SMX Database")

frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Hello World").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=2, row=0)
ttk.Button(frame, text="Get Riders", command=getRiders).grid(column=1, row=0)

txt = Text(root, height=10, width=60)
txt.grid(column=2, row=1)
root.mainloop()

