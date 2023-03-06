# Outputs whether today is a weekday or not
# Author: Kirstin Barnett

from datetime import date
today = date.today()

day = today.strftime("%a")

if day == "Sun":
    print ("It is the weekend, yay!")

if day == "Sat":
    print ("It is the weekend, yay!")

print  ("Yes, unfortunately today is a weekday.")