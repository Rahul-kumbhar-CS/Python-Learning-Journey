#WAP to perform traffic light operation using if else statement
light_color=input("Enter the traffic light color (red, yellow, green):").lower()
if(light_color=="red"):
    print("Stop! The light is red.")
elif(light_color=="yellow"):
    print("BE Ready! The light is yellow.")
elif(light_color=="green"):
    print("Go! The light is green.")
else:
    print("Invalid traffic light color.")

#2:
print("The traffic light operation:")
print("1.Red\n2.Yellow\n3.Green\n4.Exit")
choice=int(input("Enter your choice:"))
match choice:
    case 1:
        print("Stop the vehicle")
    case 2:
        print("Get ready to move")
    case 3:
        print("Move the vehicle")
    case 4:
        exit(0)
    case _:
        print("Invalid light signal")