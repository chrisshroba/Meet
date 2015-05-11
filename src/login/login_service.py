__author__ = 'chrisshroba'

import random
import hashlib
from login_exception import LoginException

from flask import session

def login(username, password):
    user = login_dao.get_from_username(username)
    if user is None:
        raise LoginException(type=LoginException.USERNAME_NOT_FOUND)
    password_to_check = encrypt(username, user.salt, password)
    if password == user.password:
        # User is valid.
        return user
    else:
        # Incorrect password
        raise LoginException(type=LoginException.USERNAME_NOT_FOUND)



def encrypt(username, salt, password):
    concat = username + salt + password
    return hash(concat)

def hash(string):
    hash = hashlib.sha256()
    hash.update(string)
    return hash.hexdigest()


ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def generate_random_salt(salt_length):
    salt = ""
    for i in range(salt_length):
        salt += random.choice(ALPHABET)
    return salt