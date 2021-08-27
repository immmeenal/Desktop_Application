from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()

def get_data(name,age,address):
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="7284559",host="localhost",port="5432")
    cur = conn.cursor()
    query = '''insert into stud (name, age, address) values (%s,%s,%s);'''
    cur.execute(query,(name,age,address))
    print("Data Inserted")
    conn.commit()
    conn.close()

def search(id):
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="7284559",host="localhost",port="5432")
    cur = conn.cursor()
    query='''select * from stud where id=%s'''
    cur.execute(query,(id))
    row=cur.fetchone()
    display_search(row)
    conn.commit()
    conn.close()

def display_search(row):
    listbox=Listbox(frame,width=20,height=1)
    listbox.grid(row=9,column=1)
    listbox.insert(END,row)

def display_ALL():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="7284559",host="localhost",port="5432")
    cur = conn.cursor()
    query = ''' select * from stud '''
    cur.execute(query)
    row=cur.fetchall()

    listbox=Listbox(frame,width=20,height=5)
    listbox.grid(row=12,column=1)
    for x in row:
        listbox.insert(END,x)



canvas = Canvas(root, height= 480, width=900) #initialise the canvas obj
canvas.pack() #add canvas to windows

frame = Frame()
frame.place(relx=0.3,rely=.1,relwidth=0.8,relheight=0.8)#place an element on top of other element

label = Label(frame,text = "Add Data")
label.grid(row=0,column=1)

label = Label(frame,text = "Enter student name : ")
label.grid(row=1,column=0)
entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

label = Label(frame,text = "Enter student age : ")
label.grid(row=2,column=0)
entry_age = Entry(frame)
entry_age.grid(row=2,column=1)

label = Label(frame,text = "Enter student address : ")
label.grid(row=3,column=0)
entry_address = Entry(frame)
entry_address.grid(row=3,column=1)

button = Button(frame,text= "Submit", command=lambda : get_data(entry_name.get(),entry_age.get(),entry_address.get()))
button.grid(row=4,column=1)

#search functionality

label = Label(frame, text= "Search Record")
label.grid(row=5,column=1)

label = Label(frame, text= "Search By ID")
label.grid(row=6,column=0)
Id_search = Entry(frame)
Id_search.grid(row=6,column=1)

button = Button(frame,text="search",command=lambda:search(Id_search.get()))
button.grid(row=6,column=2)

#display all record

label = Label(frame, text= "Display List")
label.grid(row=10,column=1)

button = Button(frame,text="Display",command=lambda:display_ALL())
button.grid(row=11,column=1)

root.mainloop()