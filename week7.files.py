# Program to open a file and count the number of occurrences of the character e within it
# Author: Kirstin Barnett

import sys

character = "e"
FILENAME = sys.argv[1]

def number():
    with open(FILENAME) as f:
        data = f.read()
        lower_case = data.lower()
        occurences = lower_case.count(character)
        return occurences

try:
    with open(FILENAME) as f:
        data = f.read()

except FileNotFoundError:
     print ("Check the spelling of the file name. \nIf the file is not in the same folder as the sys.py program please enter the full address of the file.")

except Exception as e:
    print (f"Something has gone wrong. Here is the error information: \n{e}")

else:
    number_of_es = number()
    print (f"In the file {FILENAME} there are {number_of_es} occurences of the character '{character}'.")g

