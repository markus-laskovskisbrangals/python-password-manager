import configparser
import os
import mysql.connector

from configparser import ConfigParser

print('-------------------Configuration test script------------------')

#Checking if config file exists
print('Čhecking if config file exists')
assert os.path.isfile('config.ini') == True
print('Test OK')
print('-----------------------------------------------------------------------------')

#Checking if data exist in config file

config = ConfigParser()
config.read('config.ini')

print('Checking if data exist in config file')
assert config.has_option('user', 'user_password') == True
assert config.has_option('user', 'user_key') == True
assert config.has_option('database', 'db_host') == True
assert config.has_option('database', 'db_name') == True
assert config.has_option('database', 'db_user') == True
assert config.has_option('database', 'db_password') == True
print('Test OK')
print('-----------------------------------------------------------------------------')

#Testing connection to database
print('Tedting connection to database')
db_host = config.get('database', 'db_host')
db_name = config.get('database', 'db_name')
db_user = config.get('database', 'db_user')
db_pass = config.get('database', 'db_password')

connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
assert connection.is_connected() == True
print('Test OK')
print('-----------------------------------------------------------------------------')

#Testing if required files exist
print('Checking if yaml files exist')
assert os.path.isfile('manager_log.yaml') == True
assert os.path.isfile('migration_log.yaml') == True
print('Test OK')
print('-----------------------------------------------------------------------------')

print('Checking if required directories exist')
assert os.path.isdir('log') == True
assert os.path.isdir('migrations') == True
print('Test OK')
print('-----------------------------------------------------------------------------')

print('SUCCESS')
print('All tests has been passed')