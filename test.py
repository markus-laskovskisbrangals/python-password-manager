from logging import error
from generator import *

#Testing for encryption function
print('testēju paroles šifrēšanu ar string')
assert encrypt_password('sdqeasdq.rae13')
print('testēju paroles šifrēšanas atgriezto datu tipu (jābūt bytearray')
assert type(encrypt_password('sdqeasdq.rae13')) == bytes
print('testēju paroles šifrēšanu ar skaitli')
assert encrypt_password(12) == 'bad'

#Testing for decryption function
print('Testēju paroles atšifrēšanu.')
assert decrypt_password('gAAAAABhWKiDIw0qABLW2E5bP-egsfNkb3JOfxAhb3gn-gEfHua116wQrH9unbdk7E477FGY6RBh-cgBp3LSEzhg51XATFsxpA=='.encode()) == 'wYtxdg.3RLoB'
print('Testēju paroles atšifrēšanu ar skaitli')
assert decrypt_password(1234) == 'bad'