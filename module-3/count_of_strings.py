"""Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings. """

str_list = ['applea', 'beetroot', 'banana', 'orange', 'kiwi', 'citrus', 'bob']

if len(str_list)>=2:
    for i in str_list:
        if i[0]== i[-1]:
            print("the string which has same first and last character:", i)
        else:
            pass
            # print("string has no same first and last character... ")
            
else:
    """Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings. """

str_list = ['applea', 'beetroot', 'banana', 'orange', 'kiwi', 'citrus', 'bob']

if len(str_list)>=2:
    for i in str_list:
        if i[0]== i[-1]:
            print("the string which has same first and last character:", i)
        else:
            pass
            # print("string has no same first and last character... ")
            
else:
     print("string is smaller than 2 character... ")
    