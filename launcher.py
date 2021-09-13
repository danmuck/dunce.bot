# client import
from logging import debug
from lib.client import client
# .env import
import os
from dotenv import load_dotenv
load_dotenv()
VERSION = 'dev'



# login ---
print(f'\n\t-[ submit credentials ]-\n\n')
print(f'Big Idiot Console [ LOGIN ]\n')
login = input('username: ')
password = input('password: ')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
if login == LOGIN and password == PASSWORD:
    print(f'\n\n\n\t-[ WELCOME TO DUNCE.BOT ({VERSION}) ]-\n\n')

    # run bot ---
    BIC = input('BIC: ')
    if BIC == 'run bot':
        client.run(VERSION)
    elif BIC == 'test':
        print(f'TESTING')
    elif BIC == 'db man':
        print(f'testing db man')
    else: pass


else:
    print(f'\n\n\n\t-[ ACCESS DENIED ]-\n\n\n\n\n\nexiting program...\n\n\n')
    quit()
