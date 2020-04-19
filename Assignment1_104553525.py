#Emily Addison
#104553525
#Assignment 1
#January 30th, 2020

r = float(input("Enter in the length of the row, in feet: ")) #The user enters the length in variable r and it is saved as a float 
e = float(input("Enter in the amount of space, in feet used by an end post assembly: "))#The user enters the amount of space in variable e and it is saved as a float 
s = float(input("Enter the distance, in feet, betweeneach vine: "))#The user enters the distance in variable s and it is saved as a float 
v = (r-2*e)/s #The amount of grapvines that can be planted is calculated
print ("You have enough space for", v,"vines")#The output of how many can be planted is displayed 