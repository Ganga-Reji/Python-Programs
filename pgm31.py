num=int(input("enter the positive integer number: "))
i=1
print("the factors of the",num,"are: ",end="")
while i<=num:
	if num%i==0:
		print(i,end=" ")
	i+=1
print(end="\n")
