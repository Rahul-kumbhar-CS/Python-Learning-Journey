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