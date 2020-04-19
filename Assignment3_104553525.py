#Emily Addison
#104553525
#Assignment 3

# Function to decipher if the number is prime or composite
def prime_or_composite(n):  
    has_divisor = False
    i =2
    for i in range(2, n):
        if ((n % i) == 0):
            has_divisor = True
            break

    if(has_divisor == True):
        print(n,"is composite")
    else:
        print(n, "n is prime")


#Main function that asks the user to enter in an integer and calls the function to decipher if its a prime or composite number
user_num = int(input("Enter an integer greater than 1: "))
if (user_num>1):
    numbers = []
    for count in range (2,user_num+1):
        numbers.append(count)


    
    for i in range(0, len(numbers)):
        prime_or_composite(numbers[i])






