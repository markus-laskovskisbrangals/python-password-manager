import logging
import logging.config
import mysql.connector
from mysql.connector import connection
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

    db_host = config.get('database', 'db_host')
    db_name = config.get('database', 'db_name')
    db_user = config.get('database', 'db_user')
    db_pass = config.get('database', 'db_password')
except:
    print('Error in config file!')
    logger.error('')
    exit()

logger.info('Cinfig file read successful')

upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrdtuvwxyz'
numbers = '1234567890'
symbols = '.,!@#$%^&*()'
remaining_tries = 3

combined_string = upper_case + lower_case + numbers + symbols
user_authenticated = True
connection = None
connected = False

def db_connect():
    global connection
    connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_pass)

db_connect()

def get_cursor():
    global connection
    try:
	    connection.ping(reconnect=True, attempts=1, delay=0)
	    connection.commit()
    except mysql.connector.Error as err:
	    logger.error("No connection to db " + str(err))
	    connection = db_connect()
	    connection.commit()
    return connection.cursor()

logger.info('Connecting to database')

try:
	cursor = get_cursor()
	if connection.is_connected():
		db_Info = connection.get_server_info()
		logger.info('Connected to MySQL database. MySQL Server version on ' + str(db_Info))
		cursor = connection.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		logger.debug('Your connected to - ' + str(record))
		connection.commit()
except Error as e :
	logger.error('Error while connecting to MySQL' + str(e))

# Insert generated password into database
def insert_data(pass_name, password, date):
    cursor = get_cursor()
    try:
        cursor = connection.cursor()
        result  = cursor.execute("INSERT INTO `user_passwords` (`name`, `password`, `created_at`) VALUES ('" + str(pass_name) + "', '" + str(password) + "', '" + str(date) + "');")
        connection.commit()
        logger.info('Password inserted into database')
    except Error as e:
        logger.error("INSERT INTO `user_passwords` (`name`, `password`, `created_at`) VALUES ('" + str(pass_name) + "', '" + str(password) + "', '" + str(date) + "');")
        logger.error('Problem with inserting into database: ' + str(e))
        pass

def run():
    main_menu_active = True
    print('What do you want to do?\n')
    print('Generate new password - 1')
    print('Retreive password from database - 2')
    print('Exit - 3\n')
    while main_menu_active == True:
        try:
            option = int(input('Enter 1, 2 or 3: ')) 
        except:
            print('Only numbers are allowed')
        if option == 1:
            main_menu_active = False
            generate_password()
        elif option == 2:
            print('This feature is not implemented yet')
        elif option == 3:
            exit()
        else:
            print('Answer not recognized!')

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
    logger.info('New password encrypted')
    return encrypted_password

def decrypt_password(encrypted_password):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password)
    logger.info('User decrypted a password')
    print(decrypted_password.decode())

def generate_password():
    password_name = input('Enter the name of your password: ')
    try:
        length = int(input('Enter your desired password length: '))
    except:
        print('Only numbers are allowed!')
        logger.error('User did not specify password length')
        run()
    password = ''
    if length > 32:
        print('The maximum length of password can be 32 characters!')
        return
    for i in range(length):
        password += random.choice(combined_string)
    logger.info('New password generated')
    encrypted_password = encrypt_password(password)
    current_time = datetime.now()
    insert_data(password_name, encrypted_password.decode(), current_time)
    print('Your password for', password_name, 'is', password, 'copy your password to use it.')
    run()

run()