#Q8. Input the day number (1–7) and print the day of the week 
day_num = int(input("Enter day number (1-7): "))

if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")
