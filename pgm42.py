def sumOfSeries(num):
	res=0
	fact=1
	for i in range(1,num+1):
		fact*=i
		res=res+(i**i/fact)
		print(f"{i**i}/{i}!+")
	return res
n=int(input("Enter number: "))
print("sum: ",sumOfSeries(n))
