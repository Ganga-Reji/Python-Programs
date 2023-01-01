str1=input("enter the string:")
print("text before changes:"+str(str1))
symbol='$'
str2=str1[0]+str1[1:].replace(str1[0],symbol)
print("string after the changes :"+str(str2))







