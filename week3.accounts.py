# A program that reads in an account number and only shows the last 4 digits the rest replaced by x
# If a number shorter than 5 digits is entered the full number will be shown and this will be insecure
# Author: Kirstin Barnett

bank_account_number = input("Please enter an account number: ")

# Strips the last 4 digits from the bank account number
last_4_digits = bank_account_number[-4:]

# Calculates the length of the bank account number and therefore the number of xs to be used in the masking
length_account_number = len(bank_account_number)
number_of_xs = length_account_number - 4
masked_digits = number_of_xs * 'x'

# Prints out the masked account number
print (f"{masked_digits}{last_4_digits}")