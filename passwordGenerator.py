import secrets
import string
import random

def generatePassword():
    """
    generate a secure random password for a user
    Password length is 10;
    Should contain at least a number;
    Should contain at least a special character (such as !,@,+,#,%,etc);
    Should not contain space(s).
    """
    password_picks = string.ascii_letters + string.digits + string.punctuation
    user_password = secrets.choice(string.digits)
    user_password += secrets.choice(string.punctuation)
    user_password += ''.join(secrets.choice(password_picks) for i in range(8))
    password = list(user_password)
    secrets.SystemRandom().shuffle(password)#
    print('Your password is', ''.join(password))

generatePassword()