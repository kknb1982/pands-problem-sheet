# Outputs whether today is a weekday or not
# Author: Kirstin Barnett

from datetime import date
today = date.today()

day = today.strftime("%a")

if day == "Sun":
    print ("It is the weekend, yay!")

elif day == "Sat":
    print ("It is the weekend, yay!")

else:
    print ("Yes, unfortunately today is a weekday.")
