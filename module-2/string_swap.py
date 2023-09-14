
str1 = "abhi"
str2 = "shek"

print("Before Swap :",str1,str2)
new_str1 = str1[1:2] + str1[:1] + str1[2:]  
new_str2 = str2[1:2] + str2[:1] + str2[2:]
print("After Swap :",new_str1, new_str2)