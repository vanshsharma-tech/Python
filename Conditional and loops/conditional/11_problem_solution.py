#Q11. Program to print greeting based on time

time = int(input("Enter the time in 24-hour format (0-23): "))

if 0 <= time < 12:
    print("Good Morning 🌅")
elif 12 <= time < 17:
    print("Good Afternoon ☀️")
elif 17 <= time < 21:
    print("Good Evening 🌇")
elif 21 <= time <= 23:
    print("Good Night 🌙")
else:
    print("Invalid input! Please enter time between 0 and 23.")
