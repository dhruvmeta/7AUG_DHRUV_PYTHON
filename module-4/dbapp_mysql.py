import pymysql


try:
    db=pymysql.connect(host='local host', user='root', password='',database='temp')
    print("data base connected !")
except Exception as e :
    print("error!")
