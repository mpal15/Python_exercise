distance = int(input("enter the distance:"))

if distance <3:
  transport = 'Walk'
elif distance<=15:
  transport = "Bike"
else:
  transport = "Car"

print("Al recommend you the transport of :", transport)

    