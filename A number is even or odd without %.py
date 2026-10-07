#Check whether a number is even or odd without %.
number=int(input("Enter a number:"))
if (number & 1)==0:
    print("The number is even.")
else:
    print("The number is odd.")