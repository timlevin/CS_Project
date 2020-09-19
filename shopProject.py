import sqlite3
from sqlite3 import Error
from tkinter import *
from PIL import Image, ImageTk


def create_connection(db_file):
    conn= None
    try:
        conn= sqlite3.connect(db_file)
        print("Connection to database succesful. SQLite version:",sqlite3.version)
    except Error as e:
        print(e)
    return conn

conn= create_connection(r"shopData.db")
        
def create_table(conn, create_table_sql):
    try:
        c= conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        

def main():
    sql_storage_creation= """CREATE TABLE IF NOT EXISTS storage (
        id integer PRIMARY KEY,
        name text,
        quantityRemaining integer,
        retailPrice float,
        factoryPrice float
        );"""

    sql_finances_creation= """CREATE TABLE IF NOT EXISTS finances (
        id integer PRIMARY KEY,
        month integer,
        year integer,
        totalRevenue float,
        totalCost float,
        totalProfit float
        );"""

    if conn is not None:
        create_table(conn, sql_storage_creation)
        create_table(conn, sql_finances_creation)

    else:
        print("Unable to connect to database.")

main()
        
def add_item(conn, item):
    sql= """INSERT INTO storage(name,quantityRemaining,retailPrice,factoryPrice)
            VALUES(?,?,?,?)"""
    cur= conn.cursor()
    cur.execute(sql,item)
    conn.commit()
    

def new_month(conn, month):
    sql= """INSERT INTO finances(month,year,totalRevenue,totalCost,totalProfit)
            VALUES(?,?,?,?,?)"""
    cur= conn.cursor()
    cur.execute(sql,month)
    conn.commit()

def getNewSubmit(a, b, c, d):
    newItem= (a,b,c,d)
    add_item(conn,newItem)
    popup= Tk()
    popup.title("!")
    label= Label(popup,text="Item added to database.",font=("Arial",12))
    label.pack(side="top",pady=10)
    okay= Button(popup,text="Okay", command=popup.destroy)
    okay.pack()
    popupWidth= popup.winfo_reqwidth()
    popupHeight= popup.winfo_reqheight()
    screenWidth= popup.winfo_screenwidth()
    screenHeight= popup.winfo_screenheight()
    posX= int(screenWidth/2-popupWidth/2)
    posY= int(screenHeight/3-popupHeight/2)
    popup.geometry("+{}+{}".format(posX, posY))
    popup.mainloop()

def newPressed():
    newWindow= Tk()
    newWindow.title("New Items")
    newWindow.geometry("500x300")
    newWindow["background"]= "green"
    title= Label(newWindow, text="Add New Items to Store Database:",foreground="white",background= "green", font=("Candara",22,"bold"))
    title.grid(column=0,row=0, columnspan=5, pady= (0,20))

    nameText= Label(newWindow, text="Item Name:",foreground="white",background= "green", font=("Calibri",16)).grid(column=0,row=1)
    nameEntry= Entry(newWindow)
    nameEntry.grid(column=1,row=1)

    quantityText= Label(newWindow, text="Quantity Bought:",foreground="white",background= "green", font=("Calibri",16)).grid(column=0,row=2)
    quantityEntry= Entry(newWindow)
    quantityEntry.grid(column=1,row=2)

    retailPriceText= Label(newWindow, text="Retail Unit Price (£):",foreground="white",background= "green", font=("Calibri",16)).grid(column=0,row=3)
    retailPriceEntry= Entry(newWindow)
    retailPriceEntry.grid(column=1,row=3)

    factoryPriceText= Label(newWindow, text="Factory Unit Price (£):",foreground="white",background= "green", font=("Calibri",16)).grid(column=0,row=4)
    factoryPriceEntry= Entry(newWindow)
    factoryPriceEntry.grid(column=1,row=4)

    newSubmit= Button(newWindow, text="Submit", cursor= "hand2",
                      command= lambda: [getNewSubmit(nameEntry.get(),quantityEntry.get(),retailPriceEntry.get(),factoryPriceEntry.get()),clear_Text()])
    newSubmit.grid(column=1,row=5)

    newWindow.mainloop()

def clear_Text():
    nameEntry.delete(1, END)

mainWindow= Tk()
mainWindow.title("Main Screen")
mainWindow.geometry("940x500")
mainWindow["background"]= "spring green"
titleFrame= Frame(mainWindow)
titleFrame.grid(row=0,column=0,columnspan=5)
title= Label(titleFrame, text="Interactive Shop Database Programme",fg="white",bg="spring green",font=("Candara",42,"bold"))
title.pack()

image= Image.open("addPic.png")
image= image.resize((150,150), Image.ANTIALIAS)
my_img= ImageTk.PhotoImage(image)
addPic= Button(mainWindow, image= my_img, cursor="hand2", command=newPressed)
addPic.grid(row=1,column=0, pady=(60,15))

addPicText= Label(mainWindow,text="Add New Item", fg= "white",bg="spring green",font= ("Helvetica",20,"bold"))
addPicText.grid(row=2,column=0)


mainWindow.mainloop











