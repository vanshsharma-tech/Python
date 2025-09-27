# Q7.  Find the largest of three numbers without using if or max().
a = 5
b = 10
c = 3
largest = (a > b) * a + (b >= a) * b # Compare a and b (5 > 10) => 10 
largest = (largest > c) * largest + (c >= largest) * c
print("The largest number is:", largest)