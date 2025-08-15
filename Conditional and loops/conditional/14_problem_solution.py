#Q14. Input electricity units consumed and calculate the bill.

units = int(input("Enter the units of the bill: "))

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print(f"Total Electricity Bill = ₹{bill}")
