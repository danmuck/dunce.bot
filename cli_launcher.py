# client import
from lib.db import db
from logging import debug
from lib.client import client
from sqlite3 import Cursor
# .env import
import os
from dotenv import load_dotenv
load_dotenv()
VERSION = 'BIC'


import re
from re import search

def BIC(cmd):
    cmd = input(f'BIC: ')

    # run bot ---
    if cmd == 'run':
        client.run(VERSION)
    elif cmd == 'help':
        print(f''' \n\n\n      -[ BIC cmds ]-                  ?? ???
                \n       ___     ___                  ??      ??
                \n      [BIC]   [FIT]                         ??
                \n       TTT     TTT                       ???
                \n-------------------------               ??
                \n   :run         :db man                 ??
                \n                                        ??
                \n   :view        :game                   
                \n                                        ??
                \n   :new user    :                
                \n                                 
            \n''')
        BIC('')

    elif cmd == 'test':
        test = input(f'TESTING [:] ')
        if test == 'exit':
            BIC('')
        elif test == 'ftest':
            input(f'F-TEST [:] ')
            if 'exit':
                BIC('')
        else: BIC('')

    elif cmd == 'db man':
        db_man = input(f'DATABASE.MGMT [:] ')
        if db_man == 'exit':
            BIC('')
        elif db_man == 'view':
            search_db = input(f'SEARCH:')
            if search_db == 'links':
                db.cur.execute("SELECT * FROM links ORDER BY ChannelID")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ links ]\n')
                for row in rows:
                    print(f'{row}\n')
                BIC('')
            # input('SEARCH: ')
            elif search_db == 'exp':
                db.cur.execute("SELECT * FROM exp ORDER BY XP DESC")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ exp ]\n')
                for row in rows:
                    print(f'{row}\n')
                BIC('')
            elif search_db == 'guilds':
                db.cur.execute("SELECT * FROM guilds ORDER BY GuildID")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ guilds ]\n')
                for row in rows:
                    print(f'{row}\n')
                BIC('')
                print(f'BROKEN')
            elif search_db == 'items':
                db.cur.execute("SELECT * FROM items ORDER BY ItemID")
                items = db.cur.fetchall()
                for item in items:
                    print(f'\n\t[ {item[3]} ]\nitem_name: {item[1]}\nitem_desc: {item[2]}\nitem_id: {item[0]}')
                    print(f'\nDB.MGMT: fetched all...')
                BIC('')

            else: 
                print(f'\n\t-[ ABORTED ]-\n')
                BIC('')
        elif db_man == 'build':
            print(f'NO WORKING')  
            BIC('')    
        else: BIC('')

    elif cmd == 'mess':
        mess = input(f'MESSAGE [:] ')
        if mess == 'exit':
            BIC('')

    elif cmd == 'game':
        BIC_game = input(f'\t*PRESS ENTER TO START*\n')
        if BIC_game == '':
            g_home = input('HOME: ')
            if g_home == 'new user':
                print(f'\n\t-[ gUSER REGISTRATION ]-\n')
                print(f'(pick an arbitrary password as its stored as plaintext for now)\n')
                g_user = input('USER_NAME: ')
                g_pass = input('PASSWORD: ')
                print(f'USER_NAME: {g_user}\nPASSWORD: {g_pass}\n\nARE YOU SURE? (Y/n)')
                g_confirm = input('(Y/n): ')
                if g_confirm == 'Y':
                    db.execute('INSERT OR IGNORE INTO gusers (gUserName, gPassword) VALUES (?, ?)', g_user, g_pass)
                    db.commit()
                    print(f'DB.MGMT: gUSER {g_user} added to database')
                    BIC('')
                else: BIC('')
            else: BIC('') 
        else: BIC('')
# BIC end ---
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
    password = input('try again: ')
    if password == PASSWORD and login == LOGIN:
        BIC('')
    else:
        print(f'\n\n\n\t-[ ACCESS DENIED ]-\n\n\n\n\n\nexiting program...\n\n\n')
        quit()


