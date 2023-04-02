# pands-problem-sheet

# Contents
|Week|File name|Description|
|--|-------|--------|
|[01](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-1---prints-out-hello-world)| week1.helloworld.py|Prints out "Hello World!"|
|[02](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-2---adds-two-user-entered-amounts-and-prints-them-in-a-readable-format)|week2.bank.py| Adds two user entered integers and ouputs them in euro and cents|
|[03](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-3---hiding-part-of-bank-account-numbers)|week3.accounts.py|Hiding part of bank account numbers|
|[04](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-4---coding-the-collatz-conjecture)|week4.collatz.py|Coding the collatz conjecture|
|[05](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-5---using-import-to-work-out-if-today-is-a-weekday)|week5.weekday.py|Outputs whether today is a weekday or not and prints out appropriate text|
|[06](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-6---finds-an-approximation-of-the-square-root-of-a-positive-float-number)|week6.sqrt.py|Finds an approximation of the square root of a positive float number|
|[07](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-7---counting-the-occurence-of-a-character-in-a-file)|week7.files.py|Counting the occurence of a character in a file|
|[08](https://github.com/kknb1982/pands-problem-sheet/edit/main/README.md#week-8)|week8.plottask.py|Plot of the normal distribution and a cubing function|


# Projects
## Week 1 - Prints out Hello World!
### Description
This is a simple program to print out "Hello World!" when the script is run.
`print("Hello World!")`

### References
https://www.w3schools.com/python/ref_func_print.asp

## Week 2 - Adds two user entered amounts and prints them in a readable format
### Description
This program requests that the user enters two amounts in cents, adds these two numbers together and outputs them as €xxx.xx.

### The code
The program uses `input` to request the user enter the amounts and uses `int` to ensure these entries (`amount1` and `amount2` are recorded as integers. These integers are added together and then divided by 100 to make it euros and cents:

    amount1 = int(input("Enter the first amount in cents: "))
    amount2 = int(input ("Enter the second amount in cents: "))
    sum = amount1 + amount2
    total = int(sum)/100

F string is used to format what is printed to the screen:
    print (f"The sum of these is €{total}")

### References
https://www.geeksforgeeks.org/python-input-function/

## Week 3 - Hiding part of bank account numbers
### Description
This program reads in an account number and only shows the last 4 digits, the rest replaced by x. If the entered account number is less than 5 digits then all the digits will be shown, for security, in real-life you would probably ensure an account number of at least 5 digits was entered.

### The code
The user is asked to enter an account number. The last four digits of the account number are then sliced from the entered account number and stored in a new variable called last_4_digits
    bank_account_number = input("Please enter an account number: ")
    last_4_digits = bank_account_number[-4:]`

To match the number of digits to display to the masked account number the code uses `len` to find the length of the bank account number and then takes 4 from this number to find the number of 'x's required.
    number_of_xs = length_account_number - 4
    masked_digits = number_of_xs * 'x'

An f string is used to print the correctly masked bank account number.
    print (f"{masked_digits}{last_4_digits}")

### References
https://www.w3schools.com/python/python_strings_slicing.asp 

## Week 4 - Coding the collatz conjecture
### Description
The Collatz conjecture states that if you start with a positive integer and divide even numbers by 2 and odd number are multiplied by 3 and 1 added and each solution is submitted to the same rules then you will eventually reach 1. The program does this using a while loop to keep iterating through the numbers until 1 is reched and then the solutions are printed.

### The code
First an empty list is recorded to store the outputs from the script.
    numbers = []
        
The user is prompted to input a positive integer. An integer greater than 1 is specifically requested as 1 is the stop point for the Collatz Conjecture.
    number = int(input ("Please enter a positive integer greater than 1?: "))
    
Code could be inserted at this point to ensure the entered number is not <1 or a float.

The script then starts a while loop to work through the Collatz Conjecture until the answer 1 is reached. If the number is even `number % 2 == 0` then the number is divided by 2 and the resulting output stored in the numbers list. If the number is odd (basically not even in the code) then the number is multiplied by 3 and 1 added, the resulting output is stored in the list numbers. The number cycles through this code until it equals 1.

    while number != 1:
        if number % 2 == 0:
            number = number / 2
            numbers.append(int(number))
    
        else:
            number = number *3 +1
            numbers.append(int(number))

Once the number 1 is reached all the numbers in the list are printed. An asterisk is added before the list name to print the list without brackets.
    print(*numbers)

### References
https://en.wikipedia.org/wiki/Collatz_conjecture
https://www.w3schools.com/python/python_lists.asp
[https://medium.com/the-art-of-python/the-collatz-sequence-in-python-eb7e1f1b4f9e](https://www.w3schools.com/python/python_while_loops.asp)
https://www.w3schools.com/python/python_conditions.asp
https://www.javatpoint.com/how-to-print-a-list-without-brackets-in-python

## Week 5 - Using import to work out if today is a weekday
### Description
The program imports the date from the python module datetime, calucates the day of the week from this and outputs whether today is a weekend day or not.

### The code
First the date is imported from the Python module datetime 
`from datetime import date`

The today's date is recorded in a variable called today.
`today = date.today()`

The day is then recorded in a variable called today. 
`day = today.weekday()`

This outputs the day as a number, Saturday is day 5 and Sunday is day 6. Therefore, if the variable day is greater than 4 it must be a weekend. An if statement is used to print a message if it is the weekend.
`if day > 4:
    print ("It is the weekend, yay!")`
    
Otherwise the program prints "Yes, unfortunately today is a weekday."
`else:
    print ("Yes, unfortunately today is a weekday.")`

### References
https://www.w3schools.com/python/python_datetime.asp

## Week 6 - Finds an approximation of the square root of a positive float number
### Description
This programe uses the Newton method to estimate the square root of a number to a defined tolerance. The user is asked to input both the number to estimate the square root of and the tolerance.

### The code
number = float(input ("Enter a number: "))
tolerance = float(input("Enter the tolerance: "))

while number < 0:
    print (f"The number {number} is less than 0, please enter a positive number")

`def square_root(number,tolerance):
    guess = number
        
    while True:
        better_guess = (guess + number/guess)/2
        if abs (better_guess - guess) < tolerance:
            return better_guess
        guess = better_guess




best_guess = square_root(number,tolerance)
print (f"The Newton approximation of the sqare root of {number} is {best_guess}")`

### References

## Week 7 - Counting the occurence of a character in a file
### Description
This program opens a text file specificied by the user in the command line and counts the number of occurrences of the character e within it. The programme only works with text-based files. The file name can be used only when it exists in the same directory as the python program file, otherwise the full address of the file should be inserted.

### The code
This program starts by importing the sys module and then bringing in the file name to be searched from the command line. `sys.argv[1]` denotes the second argument as the file to assign to the variable FILENAME.
 `import sys
FILENAME = sys.argv[1]`

The character to be searched for is set in the variable character.
`character = "e"`

Then the function number is defined:
`def number():
    with open(FILENAME) as f:
        data = f.read()
        lower_case = data.lower()
        occurences = lower_case.count(character)
        return occurences`
        
This function opens the file to be searched, reads in the text, converts it to lower case and then counts the number of times the variable `character` occurs.

When opening the file to be searched a number of errors may be encountered so a series of try and except statements have been written. The `try` statement chacks that the file can be opened and read. If it can the program moves to the else statement. 

`try:
    with open(FILENAME) as f:
        data = f.read()`

If the file cannot be found some helpful information is printed out to remind the user that if the file is not in same folder as programme the full address of the file is needed.

`except FileNotFoundError:
     print ("Check the spelling of the file name. \nIf the file is not in the same folder as the sys.py program please enter the full address of the file.")`
     
If a different type of error occurs the detail of the error is printed to the user:
`except Exception as e:
    print (f"Something has gone wrong. Here is the error information: \n{e}")`

If the file can be opened and read the else statement is run. This runs the `number` function and prints out the number of types the requested character occurs in the file.

`else:
    number_of_es = number()
    print (f"In the file {FILENAME} there are {number_of_es} occurences of the character '{character}'.")`

### References
https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/
https://stackoverflow.com/questions/1483429/how-do-i-print-an-exception-in-python

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
