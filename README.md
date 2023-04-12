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
The program uses `input` to request the user enter the amounts and uses `int` to ensure these entries (`amount1` and `amount2` are recorded as integers). These integers are added together and then divided by 100 to make it euros and cents:

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
[1] https://en.wikipedia.org/wiki/Collatz_conjecture

[2] https://www.w3schools.com/python/python_lists.asp

[3] [https://medium.com/the-art-of-python/the-collatz-sequence-in-python-eb7e1f1b4f9e](https://www.w3schools.com/python/python_while_loops.asp)

[4] https://www.w3schools.com/python/python_conditions.asp

[5] https://www.javatpoint.com/how-to-print-a-list-without-brackets-in-python


## Week 5 - Using import to work out if today is a weekday
### Description
The program imports the date from the python module datetime, calculates the day of the week from this and outputs whether today is a weekend day or not.

### The code
First the date is imported from the Python module `datetime` and `date.weekday()` is used to output the day of the week as an integer.  

    from datetime import date
    today = date.today()
    day = today.weekday()

Then `if` and `else` statements are used to print different statements depending on if it is a week day or the weekend. A Saturday or Sunday would give a `today.weekday()` value of a 5 or a 6. Therefore, if it is a Saturday or Sunday the first statement is printed otherwise the other statement in the `else` statement is printed.

    if day > 4:
        print ("It is the weekend, yay!")

    else:
        print ("Yes, unfortunately today is a weekday.")

### References
[1] https://www.w3schools.com/python/python_datetime.asp

[2] https://pynative.com/python-get-the-day-of-week/

[3] https://www.w3schools.com/python/python_conditions.asp


## Week 6 - Finds an approximation of the square root of a positive float number
### Description
This programe uses the Newton method to estimate the square root of a number to a defined tolerance. The user is asked to input both the number to estimate the square root of and the tolerance.

### The code
Newton's method for estimating a square root says that the square root of any number (N) can be found by:

> root = (X + (N / X)) / 2 where X is any guess which can be assumed to be N or 1. 

This code uses `while` loops to iterate through "guesses" of the square root until the tolerance is met. This is done by defining a function called `square_root` which accepts two arguments the number to investigate the square root and the tolerance. The first step in the funcation sets the initial guess as the user entered number. Then a `while` loop is entered that iterates through the guesses. Each guess in turn is subjected to the Newton estimation method `(guess + number/guess)/2`. The output of this is then tested against the tolerance, if the tolerance is met or exceeded the `while` loop stops and the current estimate is returned.

    def square_root(number,tolerance):
        guess = number     
        
        while True: 
            better_guess = (guess + number/guess)/2
            if abs(better_guess - guess) < tolerance:
                return better_guess
            guess = better_guess

Now the function has been created the user is asked to input the arguments for the function. First the user is asked to enter a number to find the square root of. There is a `while` loop to ensure that re-prompts the user enters a number greater than 0 until an appropriate number is entered.

    number = float(input ("Enter a number: "))
    
    while number < 0:
        print(f"The number {number} is less than 0, please enter a positive number: ")
        number = float(input ("Enter a number: "))
  
The same process is followed when getting the user to enter the tolerance. This time the while loop checks that a number less than 1 has been entered:

    tolerance = float(input("Enter the tolerance: "))

    while tolerance >= 1:
        print("The tolerance must be less than 1.")
        tolerance = float(input("Enter the tolerance: "))  

When all the conditions are met an `else` statement calls the function with the correct arguments and prints out the result:
    else:
        best_guess = square_root(number,tolerance)
        print (f"The Newton approximation of the square root of {number} is {best_guess}")

### References
[1] https://en.wikipedia.org/wiki/Newton%27s_method

[2] https://www.w3schools.com/python/python_while_loops.asp

[3] https://www.w3schools.com/python/ref_func_abs.asp

## Week 7 - Counting the occurence of a character in a file
### Description
This program opens a text file specificied by the user in the command line and counts the number of occurrences of the character e within it. The programme only works with text-based files. The file name can be used only when it exists in the same directory as the python program file, otherwise the full address of the file should be inserted.

### The code
This program starts by importing the sys module and then bringing in the file name to be searched from the command line. `sys.argv[1]` denotes the second argument as the file to assign to the variable FILENAME.

    import sys
    FILENAME = sys.argv[1]

The character to be searched for is set in the variable character.

    character = "e"

Then the function number is defined:
    def number():
        with open(FILENAME) as f:
            data = f.read()
            lower_case = data.lower()
            occurences = lower_case.count(character)
            return occurences
        
This function opens the file to be searched, reads in the text, converts it to lower case and then counts the number of times the variable `character` occurs.

When opening the file to be searched a number of errors may be encountered so a series of try and except statements have been written. The `try` statement checks that the file can be opened and read. If it can the program moves to the else statement. 

    try:
        with open(FILENAME) as f:
            data = f.read()

If the file cannot be found some helpful information is printed out to remind the user that if the file is not in same folder as programme the full address of the file is needed.

    except FileNotFoundError:
        print ("Check the spelling of the file name. \nIf the file is not in the same folder as the sys.py program please enter the full address of the file.")
     
If a different type of error occurs the detail of the error is printed to the user:
    except Exception as e:
        print (f"Something has gone wrong. Here is the error information: \n{e}")

If the file can be opened and read the `else` statement is run. This runs the `number` function and prints out the number of types the requested character occurs in the file.

    else:
        number_of_es = number()
        print (f"In the file {FILENAME} there are {number_of_es} occurences of the character '{character}'.")`

### References
[1] https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/

[2] https://stackoverflow.com/questions/1483429/how-do-i-print-an-exception-in-python

## Week 8 - Creates a histogram and a line graph on one set of axes 
### Description
Creates a histogram of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function  h(x)=x ** 3 in the range [0, 10], on one set of axes.

### Using the code
In order to create a plot first the `numpy` and `matplotlib` libraries are imported.

    import numpy as np
    import matplotlib.pyplot as plt

Then the values for the histogram are entered and the `normal` function from `numpy` used to create 1,000 random entries in a nomrl distribution with a mean of 5 and a standard deviation of 2. I chose to define the variables for this function to make future modifications easier. These numbers could have been entered directly into the arguments field for `np.random.normal`. This data is 

    hist_mean = 5
    hist_st_dev = 2
    number_of_values = 1000

    normal_data = np.random.normal(hist_mean, hist_st_dev, number_of_values)

    plt.hist (normal_data)

The arguments for plotting "X^3" are then entered. The arguments in `range` in Python are the start value and the number before which to stop, therefore, the max value was increased by 1 to ensure that an x value of 10 was plotted. The plot was created with an array fitting the described range against x^3
    min = 0
    max = 11

    xpoints = np.array(range(min,max))
    ypoints = xpoints ** 3
    
To help this data show up better on the chart (as they are sharing axes) the argument "color = 'r'" was added, making the plotted line red.

    plt.plot(xpoints, ypoints, color = 'r')

The plot was then altered to show explanatory text on the axes, a legend and the chart title.

    plt.title("Weekly task 8 - histogram of a normal distribution and line of x^3")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(['x to the power 3', 'normal distribution'])
    plt.show()
    
### References
[1] https://www.w3schools.com/python/matplotlib_histograms.asp

[2] https://www.w3schools.com/python/ref_func_range.asp

[3] https://www.w3schools.com/python/matplotlib_plotting.asp

[4] https://www.w3schools.com/python/matplotlib_labels.asp
