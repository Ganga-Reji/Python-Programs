def simple_interest(p,t,r):
	print('The principal is: ',p)
	print('The time period is:',t)
	print('Th rate of interest is',r)
	si=(p*t*r)/100
	print('The simple interest is: ',si)

p=int(input('Enter the principal amount: '))
t=int(input('Enter the time period: '))
#r=int(input('Enter the rate of interest: '))

res=input("Is the amount holder a senior citizen (above 50years)?(Y/N): ")
if(res=='Y' or res=='y'):
	simple_interest(p,t,12)
elif(res=='N' or res=='n'):
	simple_interest(p,t,10)

