 

str = input ("enter word :")


if len(str)>2:
    if str [-3:]!='ing':
        str+='ing'
        ptint(str)
    elif str [-3:]=='ing':
        str +='ly'
        print(str)   
else :
    print(str)        