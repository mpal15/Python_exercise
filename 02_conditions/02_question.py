age=int(input("enter teh age:"))

day= input("enter the day:")

price = 12 if age >=18 else 8

if day == "Wednesday":
    price-=2

print("Ticket price for you is $",price)