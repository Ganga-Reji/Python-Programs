list1=[int(x) for x in input("enter the list of numbers:" ).split(',')]
print("original list: ",list1)

for i in list1:
	if(i%2==0):
		list1.remove(i)
print("after removing even numbers: ",list1)
