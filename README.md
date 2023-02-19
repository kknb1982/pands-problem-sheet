# pands-problem-sheet

## About me
My name is Kirstin Barnett and I am currently studying a part-time course on Computer Science and Data Analytics with ATU Galway. Prior to this course I had written basic VBA scripts in Excel and down a small amount of online learning about Python. This repository and readme relates to my coursework with ATU Galway.

## File contents
|File name | Summary          |
|---------:|------------------|
|helloworld.py |Simple program that prints out "Hello World!"|
|addOne.py|  |
|bank.py|  |
|hello.py|  |
|hello2.py|  |
|multiply.py|  |
|nameAndAge.py|  |
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
|lab 4.2.1.evens.py|uses a while loop to pring even numbers from 2 to 100

## Week01: Introduction
Setting up our working environment and learning to write our first small program 
 <details>
  <summary>  helloworld.py </summary>
</details>

## Week02
<details>
  <summary>  addOne.py </summary>
</details>

 <details>
  <summary>  bank.py </summary>
</details>

 <details>
  <summary>  hello.py </summary>
</details>

 <details>
  <summary>  hello2.py </summary>
</details>

 <details>  <summary>  multiply.py </summary>
</details>

 <details>
  <summary>  nameAndAge.py </summary>
</details>


## Week03
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

## Week04

<details>
  <summary>   </summary>
</details>


<details>
  <summary>   lab4.1.2.grade.py: Reads in a percentage and outputs the corresponding grade</summary>
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
 ## Week 04
 <details> <summmary> lab.4.2.1.evens.py: uses a while loop to print even numbers from 2 to 100 <\summary>
 line 5: creates a variable to limit the while loop. This variable will set when the loop ends.
 line 6: creates the variable on which the loop iterates.
 line 8: create the while loop to say whilst the even_number variable is less than the number_to variable complete the operation which is described in lines 9 and 10.
 line 9: print the value of the even number variable.
 line 10: increase the value of even_number by 2.
 Lines 8 to 10 will re-run until the value of number_to variable is met.
 line 9
 
