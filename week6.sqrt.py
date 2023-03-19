# Finds an approximation of the square root of a positive float number
# Author: Kirstin Barnett

def square_root(number,tolerance):
    guess = number
        
    while True:
        better_guess = (guess + number/guess)/2
        if abs (better_guess - guess) < tolerance:
            return better_guess
        guess = better_guess


number = float(input ("Enter a number: "))
tolerance = float(input("Enter the tolerance: "))

best_guess = square_root(number,tolerance)
print (f"The Newton approximation of the sqare root of {number} is {best_guess}")