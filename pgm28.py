print("\nList of four digit numbers.")
li=[]
l=int(input("enter lower limit:"))
u=int(input("enter upper limit:"))
for i in range(l,u):
	for j in range(32,100):
		if i==j*j:
			string=str(i)
			if int(string[0])%2==0 and int(string[1])%2==0 and int(string[2])%2==0 and int(string[3])%2==0:
				li.append(i)
print(li) 

									


