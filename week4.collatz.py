# Coding the collatz conjecture

# Author: Kirstin Barnett

numbers = []

def collatz(number):
    if number  % 2 == 0:
        return number //2
    elif number % 2 != 0:
        return number *3 + 1
    else:
        print ('Something went wrong')

number = int(input ("Please enter a positive integer?: "))

while number != 1:
    numbers.append(number)
    number = collatz(number)
else:
    numbers.append(number) 

print(*numbers)
