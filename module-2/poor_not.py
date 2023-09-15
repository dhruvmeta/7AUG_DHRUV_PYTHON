'''Write a Python program to find the first appearance of the substring 'not' 
and 'poor' from a given string, if 'not' follows the 'poor', replace the whole
 'not'...'poor' substring  with 'good'. Return the resulting string.'''

para = '''the poor means is having not enough money to meet basic necessities in life such as food, 
        shelter, clothing, healthcare & education poor.'''

string_not = para.find("not")
string_poor = para.find("poor")

print(string_not)
print(string_poor)

#if string_not>string_poor:
not_replace = para.replace("not", "poor")
good_replace = para.replace("poor", "good")
print(good_replace)
print(not_replace)