def armstrong(num):
#num=int(input("enter a number: "))
	order = len(str(num))
	sum=0
	k=num
	while(k>0):
		digit=k%10
		sum+=digit**order
		k//=10
	if num==sum:
		return num "is an armstrong number"
	else:
		return num "is not an Armstrong number"
