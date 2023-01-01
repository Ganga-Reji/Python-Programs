def compare(s1,s2,n):
	if(n<=len(s1) and n<=len(s2)):
		flag=0
		for i in range(n):
			if(s1[i]==s2[i]):
				pass
				#return true
			else:
				pass
				flag=i+1
			return flag
	else:print(f'n does not match with string lengths.')

s1=input('Enter the first  string:')
s2=input('Enter the second string:')
n=int(input("enter the number upto which  the comparison is to be made:"))
flag=-1
res=compare(s1,s2,n)
if(res==0):
	print(f'The strings are same upto n terms')
else:
	print('The strings are not same')
