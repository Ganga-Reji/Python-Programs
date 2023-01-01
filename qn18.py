dict1={'a':1,'b':2,'c':3,'d':4}
dict2={'e':1,'f':8,'g':9,'h':7}
for i in dict2.keys():
	dict1[i]=dict2[i]
print(dict1)

