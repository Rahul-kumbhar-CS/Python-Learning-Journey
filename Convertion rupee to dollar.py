#Convert Dollars to Rupees using a given exchange rate. 
exchange_rate=float(input("Enter the exchange rate (1 Dollar=?rupees): "))
amount=float(input("Enter the amount in Dollars:"))
Rupees=exchange_rate*amount
print(f"Amount in Rupees: {Rupees}")