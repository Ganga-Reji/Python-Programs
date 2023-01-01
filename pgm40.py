x=input("enter the desired shape(rec,sq,tri):")
Triarea=lambda s,a,b,c:(s*(s-a)*(s-b)*(s-c))**0.5
square=lambda j:j**2
Rectarea=lambda l,b:l*b
if(x=="tri" or x=="Tri"):
	a=float(input('Enter first side: '))
	b=float(input('Enter second side: '))
	c=float(input('Enter third side: '))
	s=(a+b+c)/2
	print("Area of Triangle:",Triarea(s,a,b,c))

elif(x=="rec" or x=="Rec"):
	a=float(input('Enter length: '))
	b=float(input('Enter breadth: '))
	print("Area of Rectangle:",Rectarea(a,b))

elif(x=="sq" or x=="Sq"):
	a=float(input('Enter a side: '))
	print("Area of square: ",square(a))



