list1=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
	a=int(input("enter element i: "))
	list1.append(a)
print("list1:",list1)
for i in range(n):
	if (list1[i]>100):
		list1[i]='over'

print("the list1 after changes:",list1)






