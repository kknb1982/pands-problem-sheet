# Coding the collatz conjecture
# A positive integer is inputted
# If the number is even this is divided by 2
# If the number is odd it is multiplied by 3 and 1 added
# This cycle continues until 1 is reached

# Author: Kirstin Barnett

# Opens a list to store the solutions
numbers = []

# Asks for a positive integer to be input
number = int(input ("Please enter a positive integer: "))

# While number is not 1 this code is run to divide even numbers by 2 and odd numbers are multiplied by 3 plus 1. 
# The outputs are added to the numbers list and stored as integers
while number != 1:
    if number % 2 == 0:
        number = number / 2
        numbers.append(int(number))
    
    else:
        number = number *3 +1
        numbers.append(int(number))

# When 1 is reached this is printed
print(*numbers)
