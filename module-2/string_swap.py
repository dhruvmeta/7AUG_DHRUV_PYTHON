str1 = input ("enter the first word :")
str2 = input ("enter the second word :")

print ("string is :",str1 +" "+ str2)
swapped_string1 =str2[:2] + str1[:1]
swapped_string2 =str1[:2] + str1[:1]

result_string = swapped_string1 +' '+ swapped_string2

print("result:",result_string)