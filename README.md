# pands-problem-sheet

# Contents
|Week|File name|Description|
|--|-------|--------|
|01||wee2.bank.py| Adds to user entered integers and ouputs them in euro and cents|
|03|week3.accounts.py|Hiding part of bank account numbers|
|04|week4.collatz.py|Coding the collatz conjecture|


# Projects
## Week 1
### Description
### Using the code
### References

## week 2 - Adds two user entered amounts and prints them in a readable format
### Description
This program requests that the user enters two amounts in cents, adds these two numbers together and outputs them as €xxx.xx.

### The code
The program uses `input` to request the user enter the amounts and uses `int` to ensure these entries (`amount1` and `amount2` are recorded as integers. These integers are added together and then divided by 100 to make it euros and cents:
`sum = amount1 + amount2
total = int(sum)/100`
F string is used to format what is printed to the screen:
`print (f"The sum of these is €{total}")`

### References

## Week 3 - Hiding part of bank account numbers
### Description
This program reads in an account number and only shows the last 4 digits the rest replaced by x. If the entered account number is less than 5 digits then all the digits will be shown, foir security in real-life you would probably ensure an account number of at least 5 digits was entered.

### The code
The user is asked to enter an account number. 
`bank_account_number = input("Please enter an account number: ")`

The last four digits of the account number are then sliced from the entered account number and stored in a new variable called last_4_digits:
`last_4_digits = bank_account_number[-4:]`

To match the number of digits to display to the masked account number the code uses `len` to find the lenght of the bank account number and then takes 4 from this number to find the number of 'x's required.
`number_of_xs = length_account_number - 4
masked_digits = number_of_xs * 'x'`

An f string is used to print the correctly masked bank account number.
`print (f"{masked_digits}{last_4_digits}")`

### References
https://www.w3schools.com/python/python_strings_slicing.asp 

## Week 4 - Coding the collatz conjecture
### Description
The programe codes the Collatz conjecture by defining a function to run the Collatz conjecture and uses a while loop to record the numbers tested and stop the function once an output of 1 is calculated. The numbers run through the function are recorded in a list and printed once the script has completed.

### Using the code
First an empty list is recorded to store the outputs from the script:
`numbers = []`

The a new function called collatz is defined. This function uses an `if` statement to divide an even number by 2 and odd numbers to be multiplied by 3 then 1 added. If for some reason the calculation cannot be completed then "Something went wrong will be printed".
`def collatz(number):
    if number  % 2 == 0:
        return number //2
    elif number % 2 != 0:
        return number *3 + 1
    else:
        print ('Something went wrong')`
        
The user is prompted to input a positive integer.
`number = int(input ("Please enter a positive integer?: "))`

Then a while loop is created to exit the function once the number being tested in the function is 1. If the number is not equal to 1 then it is added to the numbers list and that number is then put through the collatz function.
`while number != 1:
    numbers.append(number)
    number = collatz(number)`
    
There is an else statement to ensure that the number 1 is added to the list of numbers.
`else:
    numbers.append(number)`

Once the number 1 is reached all the numbers in the list are printed:
`print(*numbers)`

### References

## Week 5
### Description
### Using the code
### References

## Week 6
### Description
### Using the code
### References

## Week 7
### Description
### Using the code
### References

## Week 8
### Description
### Using the code
### References
2: Project Description
- What the program/application is going does
- Why you used certain codes (similar to the comments in the file - explain why you wrote it that way - shows you understand what code you used too)
- What was difficult and what you would like to add in the future.
3: Table of Contents (only if its very long code - eg: End of Semester Project)
4: How to Run or Install the code - we dont need this probably until later
5: How to use the code - Screenshots of the program running eg: picture of the code and what it results in
6: References - any links from what you found when googling for help with code or when looking to see how things are coded. - Even qualified programmers/data analysts google a lot, and were not being told how to do everything because they're trying to teach us how to research as well.
