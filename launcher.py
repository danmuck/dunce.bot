# client import
# from cli.tools import BIC
from lib.client import client

from logging import debug

# .env import
import os
from dotenv import load_dotenv
load_dotenv()
VERSION = 'dev'

def BIC(cmd):
    cmd = input(f'BIC: ')

    # run bot ---
    if cmd == 'run bot':
        client.run(VERSION)

    elif cmd == 'test':
        test = input(f'TESTING [:] ')
        if test == 'exit':
            BIC('')
        if test == 'ftest':
            input(f'F-TEST [:] ')
            if 'exit':
                BIC('')
        else: BIC('')

    elif cmd == 'db.man ':
        db_man = input(f'DB.MAN [:] ')
        if db_man == 'exit':
            BIC('')
        else: BIC('')

    elif cmd == 'mess':
        mess = input(f'MESS [:] ')
        if mess == 'exit':
            BIC('')

    else: BIC('')






# login ---
print(f'\n\t-[ submit credentials ]-\n\n')
print(f'Big Idiot Console [ LOGIN ]\n')
login = input('username: ')
password = input('password: ')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
if login == LOGIN and password == PASSWORD:
    print(f'\n\n\n\t-[ WELCOME TO DUNCE.BOT ({VERSION}) ]-\n\n')
    BIC('')

else:
    print(f'\n\n\n\t-[ ACCESS DENIED ]-\n\n\n\n\n\nexiting program...\n\n\n')
    quit()


