#Q4. Input a character and check whether it is a vowel or consonant 
character = input("Enter a character: ")

if character.lower() in ["a", "e", "i", "o", "u"]:
    print("yes, it is a vowel or consonant")
else:
    print("No, it is not a vowel or consonant")
