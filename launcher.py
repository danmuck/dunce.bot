# client import
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
    client.run(VERSION)
else:
    password = input('try again: ')
    if password == PASSWORD and login == LOGIN:
        client.run(VERSION)
    else:
        print(f'\n\n\n\t-[ ACCESS DENIED ]-\n\n\n\n\n\nexiting program...\n\n\n')
        quit()