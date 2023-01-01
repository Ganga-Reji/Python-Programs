def my_min(*args):
	'''This function will return the minimum value'''
	result=args[0]
	for num in args:
		if num<result:
			result=num
	return result
min=my_min(4,5,6,7,2)
print(min)
print(my_min.__doc__)

