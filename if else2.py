#Check whether a character is vowel or consonant
char=input("Enter a character:").lower()
if(char in 'aeiou'):
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")

#Check whether a character is uppercase or lowercase
char=input("Enter a character:")
if(char.isupper()):
    print(f"{char} is uppercase.")
else:
    print(f"{char} is lowercase.")