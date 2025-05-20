import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_symbols=True):

    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("--- Password Generator ---")

try:
    length = int(input("Enter the desired password length: "))

    upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (e.g., !@#$%) (y/n): ").lower() == 'y'

    password = generate_password(length, upper, digits, symbols)
    print(f"\nGenerated Password: {password}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
