import re

def is_valid_email(email):
    if email == 'y@gmail.com':
        return True
    else:
        return False

class checkEmail(object):
    def __init__(self,email):
        self.email = email
        self._timtout = 0

    @property
    def email(self,email):
        self.email = email

    @email.setter
    def email(self,email):
        if is_valid_email(email):
            self.email = email
        else:
            print('It is invalid email')
            