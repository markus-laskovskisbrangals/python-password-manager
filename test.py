from logging import error
from generator import *

if __name__ == '__main__':
    assert encrypt_password(12)
    assert encrypt_password(0)
    assert encrypt_password(-3)
    assert encrypt_password('a')
    assert encrypt_password([1]) == error, 'Should be error'