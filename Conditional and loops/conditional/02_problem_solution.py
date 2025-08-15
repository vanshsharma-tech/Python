#Q2. Take a user’s age as input and check:  
#    - `< 13` → "Child"  
#    - `13–19` → "Teenager"  
#    - `20–59` → "Adult"  
#    - `60+` → "Senior Citizen"

age = int(input("Enter Your Age: "))

if age < 13:
    print("You are child")
elif (age >= 13) and (age <= 19):
    print("You are Teenager")
elif age >= 20 and age <= 59:
    print("You are Adult")
elif age >= 60:
    print("You are Senior Citizen")
