list=[]
n=int(input("enter total no of elements in list :"))
for i in range(0,n):
        num=int( input("enter list of integers: "))
        list.append(num)
print("list of numbers entered by user: ",list)

list2=[]
for i in list:
	if i>0:
		list2.append(i)
print(list2)
#anser b
num=int(input("enter the limit: "))
sq=[i*i for i in range(0,num+1)]
print(f"squares upto {num}: ",sq)

#answr c
vowel=['a','e','i','o','u']
str=input('enter a string: ')
vowel_list=[i for i in set(str) if i in vowel]
print(vowel_list)

#answ D
str=input('enter a string: ')
ordinal=[ord(i) for i in str]
print(ordinal)
