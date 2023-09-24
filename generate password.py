import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@'
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

length = int(input('Enter the length of the password you want to generate: '))
password = generate_password(length)
print(f'Your generated password is: {password}')
