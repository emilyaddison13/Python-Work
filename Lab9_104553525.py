#Emily Addison
#104553525
#Lab 9

#Ask the user to input a value and save it as integer col
col = int(input("Enter a positive integer between 1 and 10: "))

#set row to the same value as col
row = col
i = 1

#While loop to compute the multiplication and format the table
while i <= row:
    j = 1
    while j <= col:
        print ('{:4d}'.format (i*j), end = '')
        j=j+1
    print()
    i = i+1