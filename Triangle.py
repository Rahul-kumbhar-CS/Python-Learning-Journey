#Check whether three sides can form a triangle or not.
a=int(input("Enter the first side of the triangle:"))
b=int(input("Enter the second side of the triangle:"))
c=int(input("Enter the third side of the triangle:"))
if(a+b>c and b+c>a and c+a>b):
    print("The three sides can form a triangle.")
else:
    print("The three sides cannot form a triangle.")