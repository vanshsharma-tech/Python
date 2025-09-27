# Q8. Check whether a character is a vowel or consonant using a single line of code.
char = input("Enter a character: ").lower()
print(f"{char} is a {'vowel' if char in 'aeiou' else 'consonant'}.")
