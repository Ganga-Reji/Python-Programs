list=input('enter words: ')
list=list.split(',')
max=len(list[0])
item=list[0]
for i in list:
	if len(i)>max:
		max=len(i)
		item=i
print(f'The longest item is {item} & the length of words is {max}')

