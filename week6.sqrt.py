# Finds an approximation of the square root of a positive float number
# Author: Kirstin Barnett

number = float(input ("Enter a number: "))
tolerance = float(input("Enter the tolerance: "))

# Checks a positive number has been entered
while number < 0:
    print (f"The number {number} is less than 0, please enter a positive number")

#Defines the square root function
def square_root(number,tolerance):
    guess = number      # set initial guess for the square root
        
    while True: # iterates through guesses until tolerance is met
        better_guess = (guess + number/guess)/2
        if abs (better_guess - guess) < tolerance:
            return better_guess
        guess = better_guess

# runs the square root function and outputs the answer
best_guess = square_root(number,tolerance)
print (f"The Newton approximation of the sqare root of {number} is {best_guess}")