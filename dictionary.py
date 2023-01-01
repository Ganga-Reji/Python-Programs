dict1={}
num=int(input("how many elements in first dictionary?:"))
for i in range(num):
	k=input("enter key: ")
	v=input("enter value:")
	dict1.update({k:v})
dict2={}
num=int(input("how many elements in second dictionary?: "))
for i in range(num):
	k=input("enter key: ")
	v=input("enter value: ")
	dict2.update({k:v})
for i in dict1.keys():
	dict[i]=dict2[i]
print("merged dictionary:",dict)

