# client import
from lib.db import db, gdb
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

def gbic(cmd):
    cmd = cmd or input(f'BIC: ')

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
        gbic('')

    elif cmd == 'test':
        test = input(f'TESTING [:] ')
        if test == 'exit':
            gbic('')
        elif test == 'ftest':
            input(f'F-TEST [:] ')
            if 'exit':
                gbic('')
        else: gbic('')

    elif cmd == 'db man':
        db_man = input(f'DB.MGMT.. [:] ')
        if db_man == 'exit':
            gbic('')
        elif db_man == 'view':
            search_db = input(f'VIEW: ')
            if search_db == 'links':
                db.cur.execute("SELECT * FROM links ORDER BY ChannelID")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ links ]\n')
                for row in rows:
                    print(f'[ #{row[2]} ] {row[1]}\n\ncontext: \t"{row[3]}"\n\n\n')
                # cmd = 'db man'
                gbic('db man')

            # input('SEARCH: ')
            elif search_db == 'exp':
                db.cur.execute("SELECT * FROM exp ORDER BY XP DESC")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ exp ]\n')
                for row in rows:
                    print(f'user: {row[1]}\nlevel: {row[3]} \ntotal xp: {row[2]}\nlock expires: {str(row[4])[11:]} UTC\n\n')
                    print(f'DB.MGMT: fetched all...\n')
                gbic('db man')

            elif search_db == 'guilds':
                db.cur.execute("SELECT * FROM guilds ORDER BY GuildID")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ guilds ]\n')
                for row in rows:
                    print(f'{row}\n\n')
                    print(f'DB.MGMT: fetched all...\n')
                gbic('db man')

                print(f'WORK ON ME')

            elif search_db == 'items':
                gdb.fetch_items()
                gbic(cmd='db man')
                
            elif search_db == 'gusers':
                db.cur.execute("SELECT * FROM gusers ORDER BY gUSERNAME")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ gusers ]\n')
                for row in rows:
                    print(f': {row[0]}\n')
                    print(f'DB.MGMT: fetched all...\n')
                gbic('')

            else: 
                print(f'\n\t-[ ABORTED ]-\n')
                gbic('')
        elif db_man == 'build':
            db.build()
            gbic('')

        elif db_man == 'items':
            add_items = input(f'ADD ITEMS.. [:] ')
            if add_items == 'add':
                gdb.custom_item()
                gbic('add')
            elif add_items == 'many':
                gdb.insert_items()
                gbic('add')
            else:
                gbic('db man')

        else: gbic('')

    elif cmd == 'mess':
        mess = input(f'MESSAGE [:] ')
        if mess == 'exit':
            gbic('')

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
                    gbic('')
                else: 
                    gbic('')
            else: 
                gbic('') 
        else: 
            gbic('')
# BIC end ---
    else: 
        gbic('')


# login ---
print(f'\n\t-[ submit credentials ]-\n\n')
print(f'Big Idiot Console [ LOGIN ]\n')
login = input('username: ')
password = input('password: ')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
if login == LOGIN and password == PASSWORD:
    print(f'\n\n\n\t-[ WELCOME TO DUNCE.BOT ({VERSION}) ]-\n\n')
    gbic('')

else:
    password = input('try again: ')
    if password == PASSWORD and login == LOGIN:
        gbic('')
    else:
        print(f'\n\n\n\t-[ ACCESS DENIED ]-\n\n\n\n\n\nexiting program...\n\n\n')
        quit()


