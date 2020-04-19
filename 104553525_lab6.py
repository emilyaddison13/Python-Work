##Emily Addison
##104553525
## Lab 6
order = 0
cost = 0.0

order = int(input ("Amount of oil is? " ))

if (order < 150):
    cost = order *2.25
elif (order < 250): 
    cost = (150 *2.25)+ (order -150)*2.10
else:
    cost = (150*2.25)+(100*2.10) +(order - 250) *1.99

print("The cost of the oil is, %4.2f " %cost)
