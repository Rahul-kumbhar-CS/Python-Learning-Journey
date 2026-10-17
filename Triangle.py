#Check whether three sides can form a triangle or not.
a=int(input("Enter the first side of the triangle:"))
b=int(input("Enter the second side of the triangle:"))
c=int(input("Enter the third side of the triangle:"))
if(a+b>c and b+c>a and c+a>b):
    print("The three sides can form a triangle.")
else:
    print("The three sides cannot form a triangle.")


#Chjeck whether the triangle is equilateral, isosceles or scalene.
if(a==b and a==c and b==c):
    print("The triangle is equilateral.")
elif(a==b or b==c or c==a):
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
