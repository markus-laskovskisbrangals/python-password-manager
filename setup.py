import pip
import importlib

print('-----------Python password manager setup-----------')

print('Checking and installing required packeages.')
#Installing required packages
def install_package(package):
    try:
        importlib.import_module(package)
        print('Package already installed', package)
    except:
        print(package, 'Package not found. Installing...')
        pip.main(['install', package])
        print('Package installed.')

install_package('configparser')
install_package('logger')
install_package('mysql-connector')
install_package('yaml')
install_package('cryptography')

import configparser
from configparser import ConfigParser
import cryptography
from cryptography import fernet
from cryptography.fernet import Fernet

#User input for configuration info

print('Now, lets create a password for your manager')
passwords_match = False

while not passwords_match:
    password = input('Plase enter your password: ')
    password_retype = input('Please re-enter your password: ')
    if password != password_retype:
        passwords_match = False
        print('Passwords doesnt match. Please try again!')
    else:
        passwords_match = True
        print('Ģret! Your password is', password)
        print('Please save your password')

print('--------------------------------')
print('Now we will generate a new key to encrypt and decrypt your passwords in database.')

key = Fernet.generate_key().decode()
print('Your key is', key)
print('Dont share it with anyone.')
print('---------------------------------')

print('Now we need details about database')
db_host = input('Enter an IP address of your database: ')
db_name = input('Please enter yor database name: ')
db_user = input('Please enter username of your database user: ')
db_pass = input('Please enter the password of your database: ')

#Config creation
config = configparser.ConfigParser()

config['user'] = {'user_password': password,
                'user_key': key}

config['database'] = {'db_host': db_host,
                        'db_name': db_name,
                        'db_user': db_user,
                        'db_password': db_pass}

with open('config2.ini', 'w') as configfile:
    config.write(configfile)

print('-----------------------------------------------')
print('Config file created')
print('Setup cpmplete!')
print('-----------------------------------------------')