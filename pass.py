import random
import string

def generate_password(length):
    charactersofpassword = string.digits + string.punctuation + string.ascii_letters 
    password = ''.join(random.choice(charactersofpassword) for i in range(length))
    
    return password

while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        break
    except ValueError:
        print("Please enter a  integer.")

password = generate_password(length)
print("Generated password:", password)
