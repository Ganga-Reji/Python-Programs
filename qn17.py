
dict={}
num=int(input("enter the limit:"))
for i in range(0,num):
        k=input("enter key:")
        v=int(input("enter value: "))
        dict.update({k:v})
print(dict)

#a={'Abel':40,'Renold':3,'Sarah':4}
l=list(dict.items())
l.sort()
print('Ascending order is: ',l)
l=list(dict.items())
l.sort(reverse=True)
print('Descending order is ',l)
dict=dict(l)
print("dictionary",dict)

