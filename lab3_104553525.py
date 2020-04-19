#Emily Addison
#104553525
#January 29th, 2020

wattage = int(input("Enter in the wattage: "))
hours = int(input("Enter in the hours used: "))
price = float(input("Enter price per KWh in cents: "))

cost = ( wattage * hours)/(1000 * price)

print("The cost of electricity is ", cost)