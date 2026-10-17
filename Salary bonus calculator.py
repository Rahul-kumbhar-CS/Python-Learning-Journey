#Create a salary bonus calculator  based on years of service.
years_of_service=int(input("Enter the number of years of service:"))
salary=float(input("Enter the salary:"))
if(years_of_service>=10):
    bonus=salary*0.1
else:
    bonus=salary*0.05
print("The bonus is:",bonus)