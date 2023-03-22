# Outputs whether today is a weekday or not and prints out appropriate text
# Author: Kirstin Barnett

from datetime import date
today = date.today()
day = today.weekday()

if day > 4:
    print ("It is the weekend, yay!")

else:
    print ("Yes, unfortunately today is a weekday.")