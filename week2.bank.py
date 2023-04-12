# A program that adds two user entered amounts and prints them in a readable format
# Author: Kirstin Barnett

# Request user inputs amounts to be summed
amount1 = int(input("Enter the first amount in cents: "))
amount2 = int(input ("Enter the second amount in cents: "))

#Sums the amount
sum = str(amount1 + amount2)

# Converts the sum in euros and cents and outputs in €xxx.xxx
cents = sum[-2:]
euros = sum[:(len(sum)-2)]
print (f"The sum of these is €{euros}.{cents}")
