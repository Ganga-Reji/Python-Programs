color_list1=[]
n1=int(input("enter total no of elements in list one:"))
for i in range(0,n1):
	value=input("enter a colour: ")
	color_list1.append(value)
print("colour list1 :",color_list1)

color_list2=[]
n2=int(input("enter total no of elements in list two: "))
for i in range(0,n2):
	value_2=input("enter a colour: ")
	color_list2.append(value_2)
print("color list2 is:",color_list2)

list3=[]
for i in color_list1:
	if i not in color_list2:
		list3.append(i)
print(" final list of colours: ",list3)
