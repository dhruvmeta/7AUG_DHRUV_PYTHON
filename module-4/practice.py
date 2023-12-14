import sqlite3
import tkinter as tk
from tkinter import ttk



try:
        dbcon = sqlite3.connect("mydb3.db")
        print("Database connected")
except Exception as e:
        print(e)


tbl_create = "create table stud_info(id integer primary key autoincrement, name text, city text)"
try:
        dbcon.execute(tbl_create)
        print("Table created sucessfully")
except Exception as e:
        print(e)


def insert():
        n = int(input("enter number of records you want to insert:"))
        for i in range(n): 
                stnm = input("enter name:")
                stct = input("enter city:")

                insert_dt = f"insert into stud_info(name,city)values('{stnm}','{stct}')"
                try:
                        dbcon.execute(insert_dt)
                        dbcon.commit()
                        print("record inserted")
                except Exception as e:
                        print(e)

def update():
        column_name = input("select column to update:")
        new_value = input("enter new value:")
        which = int(input("enter id of the column:"))


        up_dt = f"update stud_info set {column_name}='{new_value}' where id={which}"
        print(up_dt)
        try:        
                dbcon.execute(up_dt)
                dbcon.commit()
                print("record update successfully!")
        except Exception as e:
                print(e)

def delete():
        select = input("select column to delete:")
        dl_dt = f"delete from stud_info where id ={select}"
        try:
                dbcon.execute(dl_dt)
                dbcon.commit()
                print("record deleted successfully!")
        except Exception as e:
                print(e)

operation = input("select a dml operation you want to perform(insert,update,delete):")



if operation == "insert":
        insert()
elif operation =="update":
        update()
elif operation == "delete":
        delete()
    