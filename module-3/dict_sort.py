# Write a Python script to concatenate following dictionaries to create a new one. 

dic1={'ID':'101', 'sub':'python'}
dic2={'city':'rajkot', 'centre':'Gujarat'}
dic3={'male':'Abhi','Female':'ZZZZZ'}
dic4 = {}
for d in (dic1, dic2, dic3): 
    dic4.update(d)
print(dic4)