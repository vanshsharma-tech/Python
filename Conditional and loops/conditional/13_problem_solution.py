#Q13. Check whether the entered character is uppercase, lowercase, digit, or special character.

user_input = input("Enter a character: ")

if user_input.isdigit():
    print("Entered character is a digit.")
elif user_input.islower():
    print("Entered character is lowercase.")
elif user_input.isupper():
    print("Entered character is uppercase.")
else:
    print("Entered character is a special character.")
