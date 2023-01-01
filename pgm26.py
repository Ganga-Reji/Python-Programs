num=int(input("enter your number: "))
n1=0
n2=1
count=0

if num<=0:print("enter positive integer:")
elif num==1:
	print("Fibonacci Series upto",num,":")
	print(n1)
else:print("Fibonacci series:")

while count<num:
	print(n1)
	n=n1+n2
	n1=n2
	n2=n
	count+=1

