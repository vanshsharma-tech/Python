# Q9. Input the month number (1–12) and print the number of days in that month.  

month = int(input("Enter month number (1-12): "))

if month == 1:
    print("January has 31 days")
elif month == 2:
    print("February has 28 or 29 days (Leap Year)")
elif month == 3:
    print("March has 31 days")
elif month == 4:
    print("April has 30 days")
elif month == 5:
    print("May has 31 days")
elif month == 6:
    print("June has 30 days")
elif month == 7:
    print("July has 31 days")
elif month == 8:
    print("August has 31 days")
elif month == 9:
    print("September has 30 days")
elif month == 10:
    print("October has 31 days")
elif month == 11:
    print("November has 30 days")
elif month == 12:
    print("December has 31 days")
else:
    print("Invalid input! Please enter a number between 1 and 12.")
