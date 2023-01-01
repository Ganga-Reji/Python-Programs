import Graphics
from Graphics import circle,rectangle
from Graphics.3DGraphics import cuboid,sphere
from Graphics.circle import*

rad1=float(input("Enter the radiusof the circle:"))
print("Area of a circle with radius",rad1,"is:",circle.area_circle(rad1))
print("Perimeter of circle with radius",rad1,"is:",circle.perimeter_circle(rad1))

len1=float(input("enter the length of the rectangle"))
breadth1=float(input("enter the breadth of the rectangle"))
print("Area of a rectangle with length",len1,"and breadth",breadth1,"is:",rectangle.area_rec(len1,breadth1))
print("Perimeter of a rectangle with length",len1,"and breadth",breadth1,"is:",rectangle.perimeter_rec(len1,breadth1))

len2=float(input("enter the length of the cuboid"))
breadth1=float(input("enter the breadth of the rectangle"))
print("Area of a rectangle with length",len1,"and breadth",breadth1,"is:",rectangle.area_rec(len1,breadth1))
print("Perimeter of a rectangle with length",len1,"and breadth",breadth1,"is:",rectangle.perimeter_rec(len1,breadth1))




