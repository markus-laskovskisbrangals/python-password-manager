import logging
import logging.config
import mysql.connector
import yaml
import os
import time
import configparser
import random
from cryptography import fernet
from cryptography.fernet import Fernet
from datetime import datetime
from mysql.connector import Error
from configparser import ConfigParser

with open('manager_log.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

logging.config.dictConfig(config)

logger = logging.getLogger('root')

logger.info('Password manager started')

try:
    logger.info('Start reading from config file')
    config = configparser.ConfigParser()
    config.read('config.ini')
    user_password = config.get('user', 'user_password')
    key = config.get('user', 'user_key')
except:
    print('Error in config file!')
    logger.error('')
    exit()

logger.info('Cinfig file read successful')

uppder_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrdtuvwxyz'
numbers = '1234567890'
symbols = '.,!@#$%^&*()'
remaining_tries = 3

combined_string = uppder_case + lower_case + numbers + symbols
user_authenticated = False

while not user_authenticated:
    if remaining_tries == 0:
        print('You typed incorrect password 3 times in a row, access is denied!')
        logger.error('User entered wrong password 3 times')
        exit()
    auth_password = input('Please enter your password: ')
    if auth_password == user_password:
        logger.info('User logged in')
        print('Welcome back!')
        user_authenticated = True
    else:
        remaining_tries -= 1
        logger.error('User entered wrong password')
        print('Incorrect password! Remaining tries:', remaining_tries)

def encrypt_password(password):
    encoded_password = password.encode()
    f = Fernet(key)
    encrypted_password = f.encrypt(encoded_password)
    print(encrypted_password.decode())
    logger.info('New password encrypted')
    return encrypted_password

def decrypt_password(encrypted_password):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password)
    logger.info('User decrypted a password')
    print(decrypted_password.decode())

def generate_password(length):
    password = ''
    if length > 32:
        print('The maximum length of password can be 32 characters!')
        return
    for i in range(length):
        password += random.choice(combined_string)
    logger.info('New password generated')
    encrypted_password = encrypt_password(password)
    decrypt_password(encrypted_password)
    print(password)
    return password

try:
    length = int(input('Enter your desired password length: '))
    generate_password(length)
except:
    print('Only numbers are allowed!')
    logger.error('Ūser did not specify password length')
