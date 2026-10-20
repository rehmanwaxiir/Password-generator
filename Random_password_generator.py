"""
Password generator
Create a random password with letters,numbers and symbols
"""
import secrets
import string
print("===Welcome here! generate secure passwords===")

try:

    length=int(input("Enter your password length."))
    if length<4:
        print("password length must be at least 4.",length)
    else:
        characters=(
            string.ascii_letters
            +string.digits
            +string.punctuation
        )
        password=''.join(
            secrets.choice(characters)
            for _ in range(length)
        )
        print("Your password is.",password)
except ValueError:
    print("Please enter a valid numbers.")    