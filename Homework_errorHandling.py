password = input('Please enter a password longer than 8 characters')

class InvalidPasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg

try:
    assert len(password) > 8, 'You have enter a password not longer than 8 characters'
except AssertionError:
    print(InvalidPasswordException('Password need to be longer equal or longer than 8'))
else:
    print('Password Validated : Password requierements are complited')