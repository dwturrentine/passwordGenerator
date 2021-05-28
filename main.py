import random

print('Welcome to Password Generator!')

chars = "/[a-zA-Z0-9!@#$%^&*()?]*$/"

number = input('Amount of Passwords to Generate: ')
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\n Here are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

