# pands-problem-sheet

# About me
My name is Kirstin Barnett and I am currently studying a part-time course on Computer Science and Data Analytics with ATU Galway. Prior to this course I had written basic VBA scripts in Excel and down a small amount of online learning about Python. This repository and readme relates to my coursework with ATU Galway.

# File contents
|File name | Summary          |
|---------:|------------------|
|lab1.1.1.helloworld.py [# |Simple program that prints out "Hello World!"|
|lab2.2.1.hello.py|Prints out Kirstin  |
|lab2.2.2.multiply.py| Simple multiplier |
lab2.2.3.hello2.py| input a name and says hello |
|lab2.2.4.addOne.py|  |
|lab2.2.5.nameAndAge.py|  |
|lab2.2.6.bank.py| |
|accounts.py|Reads in an account number but only shows the last 4 digits|
|lab3.1.div.py|Divides one number by another and gives the integer and remainder |
|lab3.1.randomGenerator.py| |
|lab3.1.sub.py| |
|lab3.1.testTypes.py| |
|lab3.2.absolute.py| |
|lab3.2.absolutedollars.py| |
|lab3.2.floor.py| |
|lab3.2.round.py| |
|lab3.3.length.py| |
|lab3.3.normalise.py| |
|lab4.1.1.is_even.py| |
|lab4.1.2.grade.py| |
|lab 4.2.1.evens.py|uses a while loop to print even numbers from 2 to 100|
|lab4.2.2.guess.py| prompts a user to guess a number until they get it right|
|lab4.2.3.guess2.py|prompts a user to guess a number until they get it right with too high and too low prompts|
|lab4.2.4.guess3.py|prompts a user to guess a random number between 1 and 100 until they get it right with too high and too low prompts|

# Week01: Introduction
Setting up our working environment and learning to write our first small program 
## lab1.1.1.helloworld.py: Prints out "Hello World!" 
  Simple program introducing the print command.

# Week02
## lab2.2.1.hello.py:Prints out Kirstin
    Simple program learning to change the command to print out a required value, in this case my name.

## lab2.2.2.multiply.py: Simple multiplier

## lab2.2.3.hello2.py: input a name and says hello
 
## lab2.2.4.addOne.py

## lab2.2.5.nameAndAge.py

## lab2.2.6.bank.py

# Week03
<details>
  <summary>  accounts.py: Reads in an account number but only shows the last 4 digits</summary>
  A program that reads in an account number and only shows the last 4 digits the rest replaced by x. 
  
line 5: Requests an account number. If the account number is less than 5 digits the full account number would show so the program could be altered with an if statement to say, if the number entered is less than, say, 6 digits say "please enter an account number of 6 digits or greater".
line 6: The program uses a negative slice to slice the characters 4 digits from the end to the end [-4: ] from the string. 
line 8: The len function is used to count the number of characters in the account number string. 
line 9: The number of masking 'X's is calculated by taking 4 away from the length of the string.
line 10: creates the correct number of "x" to mask all the numbers in the strong bar the final 4.
line 12: prints out 'X' instead of the first numbers in the string and only shows the final four digits.
</details>

<details>
  <summary> lab3.1.div.py:Divides one number by another and gives the integer and remainder  </summary>
  Divides one number by another and gives the integer and remainder
</details>

<details>
  <summary> lab3.1.randomGenerator.py </summary>
</details>

<details>
  <summary> lab3.1.sub.py  </summary>
</details>

<details>
  <summary> lab3.1.testTypes.py  </summary>
</details>

<details>
  <summary> lab3.2.absolute.py </summary>
</details>

<details>
  <summary>  lab3.2.absolutedollars.py </summary>
</details>

<details>
  <summary> lab3.2.floor.py </summary>
</details>

<details>
  <summary> lab3.2.round.py </summary>
</details>

<details>
  <summary> lab3.3.length.py  </summary>
</details>

<details>
  <summary> lab3.3.normalise.py  </summary>
</details>

# Week04

<details>
  <summary> lab4.1.2.grade.py: Reads in a percentage and outputs the corresponding grade  </summary>
 line 4: Asks for the score to be input
  line 6: Checks if the number input is between 0 and 100. If not line 7 is run.
  line 7: Requests a score between 0 and 100.
  lines 9 to 18 are run on any number between 0 and 100. Once an elif function (else if is met) the program stops.
  lines 9 and 10: if the number is less than 40 then line 10 is run to show a fail score.
  lines 11 and 12: if the number is >= 40 and <50 then line 12 is run to show a pass score
  lines 13 and 14: if the number is >= 50 and <60 then line 14 is run to show a merit 2 score
  lines 15 and 16: if the number is >= 60 and <70 then line 16 is run to show a merit 1 score
  lines 17 and 18: for all numbers >=70 then line 18 is run to show a distinction.
  
 When the code is run on a decimal percent the programme does not round so a score of 69.5 shows a merit 1 grade.  
</details>

<details> 
  <summmary> lab.4.2.1.evens.py: uses a while loop to print even numbers from 2 to 100 </summary>
 line 5: creates a variable to limit the while loop. This variable will set when the loop ends.
 line 6: creates the variable on which the loop iterates.
 line 8: create the while loop to say whilst the even_number variable is less than the number_to variable complete the operation which is described in lines 9 and 10.
 line 9: print the value of the even number variable.
 line 10: increase the value of even_number by 2.
 Lines 8 to 10 will re-run until the value of number_to variable is met.
</details>

<details>
  <summary> lab4.2.2.guess: Asks the user to guess the number until they get it right </summary>
  line 5: sets the variable for the number to guess
  line 7: asks the user to input a number a stores it as an integer
  lines 8 to 10 creates the while loop.
  line 8: sets the loop to run whilst the guess does not equal the set number run lines 9 and 10
  line 9: print wrong
  line 10: requests a new number.
  The loop will stop once the correct number is guessed
 </details>
 
 <details>
   <summary> lab4.2.3.guess2.py: Asks the user to guess the number until they get it right, they get told if each guess is too high or too low. </summary>
   line 6: sets the number to guess
   line 8: asks the user to insert the next guess
   lines 9 to 14: is the while loop with nested if and else functions.
   line 9: if the guess does not equal the number_to_guess variable carry out the while loop, if it does, move to line 16.
   line 10: if the guess is too low print line 11
   line 12: we know the guess cannot equal or be less than the number_to_guess variable so we use the else function to say "too high".
   line 14: requests a new number
   line 16: when a correct guess is entered this line is printed.
   </details>
  
  <details>
   <summary> lab4.2.4.guess3.py: Prompts a user to guess a random number between 1 and 100 until they get it right with too high and too low prompts </summary>
   repeats the code in lab.4.2.3.guess2.py but includes a change at lines 6 and 7 to create a random number between 1 and 100 as the number to guess.
   line 6: imports to random module
   line 7: asks random to call a random integer between 1 and 100.
   </details>
