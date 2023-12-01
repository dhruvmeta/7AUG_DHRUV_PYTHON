import random
import datetime


n=int(input("enter the nuber of student :"))

for i in range (n):
    stid = random.randint(2222,3333)
    stnam =input("enter the student name :")
    stsub = input("enter the subject name :")
    stlog= datetime.datetime.now()
    print(f"{stid}\n {stnam}\n{stsub}\n{stlog}")

    fl =open("student data.txt",'a')
    fl.write(f"data&time:{stlog}\nstudentid:{stid}\nstudentname:{stnam}\nstudentsub:{stsub}\n-------------------\n")
    