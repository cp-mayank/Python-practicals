
# -> Generate a random password with a mix of letters, numbers, and special characters.

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

passLength = int(input("Enter pass length : "))

print(generate_password(passLength)) 


