def getdata (id,name,sub,city):
    print("id:",id)
    print("name:",name)
    print("sub:",sub)
    print("city:",city)

n = int(input("enter the number of student: "))

for n in range(n):
    stid = input("enter the id: ")
    stnm = input("enter the name:")
    stsub =input("enter the sub :")
    stcity =input("enter the city :")

    print("----------------------------")

    getdata(stid,stnm,stsub,stcity)

    print("**********************************")

