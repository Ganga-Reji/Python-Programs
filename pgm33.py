num=int(input("enter a number: "))
sum=0
k=num
while k>0:
	digit=k%10
	sum+=digit**3
	k//=10
if num==sum:
	print(num,"is an  Arnstrong number")
else:
	print(num,"is not an armstrong numbwe")

