#Create an ATM withdrawal check based on account balance and withdrawal amount.
AccountHolderName="Rahul Kumbhar"
AccountNumber=9986763106
PIN=886709
Balance=5000
AccountHolderNameInput=input("Enter your name:")
AccountNumberInput=int(input("Enter account number:"))
PINInput=int(input("Enter your pin:"))
if(AccountHolderName==AccountHolderNameInput and AccountNumber==AccountNumberInput and PIN==PINInput):
    print("Your current balance is:",Balance)
    print("1.deposit money")
    print("2.withdraw money")
    option=int(input("Enter your option:"))
else:
    print("Invalid credentials! Please check your name, account number and pin.")
if(option==1):
    deposit_amount=int(input("Enter amount to deposit:"))
    Balance+=deposit_amount
    print("Deposit successful! Your new balance is:",Balance)
elif(option==2):
    withdraw_amount=int(input("Enter amount to withdraw:"))
    if(withdraw_amount<=Balance):
        Balance-=withdraw_amount
        print("Withdrawal successful! Your new balance is:",Balance)
    else:
        print("Insufficient balance! Your current balance is:",Balance)
print("Thank you for using our ATM service!")

