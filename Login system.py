#Create a simple login system using python. The system should have a predefined username and password.
username="rahul kumbhar"
password=12345678
print("Welcome to the login system!")
username_input=input("enter your username:")
password_input=int(input("enter your password:"))
if(username_input==username and password_input==password):
    print("Login successful!")
else:
    print("Login failed! Please check your username and password.")