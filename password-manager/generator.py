import configparser
from os import close
import random

config = configparser.ConfigParser()
config.read('password-manager/config.ini')

user_password = config.get('user', 'user_password')

uppder_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrdtuvwxyz'
numbers = '1234567890'
symbols = '.,!@#$%^&*()'
password = ''
remaining_tries = 3

combined_string = uppder_case + lower_case + numbers + symbols
user_authenticated = False

while not user_authenticated:
    if remaining_tries == 0:
        print('You typed incorrect password 3 times in a row, access is denied!')
        close()
    auth_password = input('Please enter your password: ')
    if auth_password == user_password:
        print('welcome back!')
        user_authenticated = True
    else:
        remaining_tries -= 1
        print('Incorrect password! Remaining tries:', remaining_tries)

length = int(input('Enter your desired password length: '))

for i in range(length):
    password += random.choice(combined_string)

#print(user_password)
print(password)