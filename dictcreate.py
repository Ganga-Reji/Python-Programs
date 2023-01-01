dict={}
num=int(input("enter the limit:"))
for i in range(0,num):
	k=input("enter key:")
	v=int(input("enter value: "))
	dict.update({k:v})
print(dict)
