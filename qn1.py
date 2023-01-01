a=int(input("enter first number no:"))
b=int(input("enter second no:"))
c=int(input("enter third no:"))
if(a>=b)and(a>=c):
	largest=a
elif(b>=a)and(b>=c):
	largest=b
else:
	largest=c
print("largest among three numbers: ",largest)



