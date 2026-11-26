#Create a simple login system using python. The system should have a predefined username and password.

#2:
def Login():
    username="rahul kumbhar"
    password=12345678
    print("Welcome to the login system!")
    username_input=input("enter your username:")
    password_input=int(input("enter your password:"))
    if(username_input==username and password_input==password):
        print("Login successful!")
    else:
        print("Login failed! Please check your username and password.")
print("Welcome to the login system!")
print("1.New User\n2.Existing User")
choice=int(input("Enter your choice:"))
if choice==1:
    new_username=input("Enter your new username:")
    new_password=int(input("Enter your new password:"))
    print("New user created successfully!")
    print("\nPlease login with your new credentials.")
    username_input=input("Enter your username:")
    password_input=int(input("Enter your password:"))
    if(username_input==new_username and password_input==new_password):
        print("Login successful!")
    else:
        print("Login failed! Please check your username and password.")
elif choice==2:
    Login()
else:
    print("Invalid choice!")