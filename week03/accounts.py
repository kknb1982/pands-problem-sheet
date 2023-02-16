# A program that reads in an account number and only shows the last 4 digits the rest replaced by x
# Author: Kirstin Barnett

bank_account_number = input("Please enter a 10 digit account number: ")
last_4_digits = bank_account_number[-4:]

print (f"xxxxxx{last_4_digits}")