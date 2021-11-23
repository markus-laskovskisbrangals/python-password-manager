from logging import error
from generator import *


print('--------------------Password Generator test script--------------------------')
#Testing for encryption function
print('Testing encryption with string')
assert encrypt_password('sdqeasdq.rae13')
print('Test OK')
print('-----------------------------------------------------------------------------')
print('Testing encryption returned data type (must be byte)')
assert type(encrypt_password('sdqeasdq.rae13')) == bytes
print('Test OK')
print('-----------------------------------------------------------------------------')
print('Testing password encryption with number')
assert encrypt_password(12) == 'bad'
print('Test OK')
print('-----------------------------------------------------------------------------')

#Testing for decryption function
print('Testing password decryption')
assert decrypt_password('gAAAAABhWKiDIw0qABLW2E5bP-egsfNkb3JOfxAhb3gn-gEfHua116wQrH9unbdk7E477FGY6RBh-cgBp3LSEzhg51XATFsxpA=='.encode()) == 'wYtxdg.3RLoB'
print('Test OK')
print('-----------------------------------------------------------------------------')
print('Testing password decryption with numbers')
assert decrypt_password(1234) == 'bad'
print('Test OK')
print('-----------------------------------------------------------------------------')
print('SUCCESS')
print('All tests has been passed')