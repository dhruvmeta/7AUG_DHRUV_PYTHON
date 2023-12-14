import sqlite3

dbcon=sqlite3.connect("newdb.db")

tbl_cteate="create tbl studinfo ( id=integer primary key autoincrement , name=text ,city=text )"

try: 
    dbcon.execute(tbl_cteate)
    print("table create succesfulluy !")
except Exception as e :
    print(e)

insert_data="insert into studinfo (name,city) values ('dhurv','amreli')"

try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("record insert!")
except Exception as e :
    print(e)   