

str = input ("enter  your string :")



if len(str)>2:
    new_str =str[0:2] + str[-2:]
    print(new_str)
else:
    print("the string is empty :")
