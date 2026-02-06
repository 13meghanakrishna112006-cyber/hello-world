item_name = "Laptops"
quantity = 2
price = 500
in_stock = True
print("Item:",item_name,"Qty:",quantity,"Price:",price,"Available:",in_stock)
total_cost = quantity*price
print("Total cost:",total_cost)

name = input("Enter your name:")
age = int(input("Enter your age:"))
age=age + 4
print("Hey",name,"you will be",age,"years old in 2030")

total_bill = float(input("Enter total bill amount:"))
people = int(input("Enter number of people:"))
share_per_person = total_bill / people
print("Total Bill:",total_bill,"\nEach person pays:",share_per_person)

print(type(total_bill))
print(type(people))
print(type(share_per_person))