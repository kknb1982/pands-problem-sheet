# Outputs whether today is a weekday or not and prints out appropriate text
# Author: Kirstin Barnett

# To work out the day of the week as a number
from datetime import date
today = date.today()
day = today.weekday()

# Saturday and Sunday are 5 and 6
if day > 4:
    print ("It is the weekend, yay!")

else:
    print ("Yes, unfortunately today is a weekday.")