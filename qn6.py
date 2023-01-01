l1=[]
n1=int(input("enter the number of items:"))
for i in range(0,n1):
	a=int(input())
	l1.append(a)

print("list1:",l1)
l2=[]
n2=int(input("enter the number of items:"))
for j in range(0,n2):
        b=int(input())
        l2.append(b)
print("list2:",l2)

len1=len(l1)
len2=len(l2)
if(len1==len2):
	print("yes both are of the same length")
else:
	print("no,both are not of the same length")

sum1=0
for i in l1:
	sum1=sum1+i
print(sum1)
sum2=0
for j in l2:
	sum2=sum2+i
print(sum2)

if(sum1==sum2):
	print("yes lists sums to same value")
else:
	print("no lists does not sum to same value")

flag=0
for i in l1:
	if(i in l1):
		flag=1
		break
if(flag==1):
	print("atleast one element in both list are same")
else:
	print("no ,there are no common elements between two lists")

