#Check whether a number is single digit, double digit or larger digit.
number=int(input("Enter a number:"))
if(number<10):
    print(f"{number} is a single digit number.")
elif(number<100):
    print(f"{number} is a double digit number.")
else:
    print(f"{number} is a larger digit number.")