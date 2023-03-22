# Program to open a file and count the number of occurrences of the character e within it
# Author: Kirstin Barnett

character = "e"
FILENAME = input(f"What file would you like to count occurences of '{character}' in?: ")

def number():
    with open(FILENAME) as f:
        data = f.read()
        lower_case = data.lower()
        occurences = lower_case.count(character)
        return occurences

number_of_es = number()
print (f"In the file {FILENAME} there are {number_of_es} occurences of the character '{character}'.")

