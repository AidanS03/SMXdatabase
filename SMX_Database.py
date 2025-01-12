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

    # print query results
    for x in myresult:
        print(x)

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
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Hello World").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=2, row=0)
ttk.Button(frame, text="Get Riders", command=getRiders).grid(column=1, row=0)
root.mainloop()

