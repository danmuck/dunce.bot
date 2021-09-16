# client import
from re import search
import re
from lib.db import db, gdb
from lib.messenger import mess
from logging import debug
from lib.client import client
from sqlite3 import Cursor
# .env import
import os
from dotenv import load_dotenv
load_dotenv()
VERSION = 'BIC'


def gbic(cmd):
    cmd = cmd or input(f'\nBIC: ')

    # run bot ---
    if cmd == 'run':
        client.run(VERSION)
        gbic('')

    elif cmd == 'help':
        print(f''' \n\n\n                          -[ BIC cmds ]-
                \n                           ___     ____
                \n                          [BIC]   [FITO]                                 
                \n                           TTT     TTTT
                \n-------------------------------------------------------------------- ||
                \n   :run         :dbm        :post        :game       [:]items
                \n
                \n   :           [:]view     [:]send      [:]new user   :     
                \n
                \n   :           [:]items     :           [:]           :
                \n
                \n   :           [:]build     :           [:]          [*]exit

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
        else:
            gbic('')

    elif cmd == 'dbm':
        db_man = input(f'DB.MGMT.. [:] ')
        if db_man == 'exit':
            # print(f'\n\t-[ DB.MGMT EXIT ]-\n')
            gbic('')
        elif db_man == 'view':
            search_db = input(f'VIEW: ')
            if search_db == 'links':
                db.cur.execute("SELECT * FROM links ORDER BY ChannelID")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ links ]\n')
                for row in rows:
                    print(
                        f'[ #{row[2]} ] {row[1]}\n\ncontext: \t"{row[3]}"\n\n\n')
                gbic('dbm')

            elif search_db == 'exp':
                db.cur.execute("SELECT * FROM exp ORDER BY XP DESC")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ exp ]\n')
                for row in rows:
                    print(
                        f'user: {row[1]}\nlevel: {row[3]} \ntotal xp: {row[2]}\nlock expires: {str(row[4])[11:]} UTC\n\n')
                    print(f'DB.MGMT: fetched all...\n')
                gbic('dbm')

            elif search_db == 'guilds':
                db.cur.execute("SELECT * FROM guilds ORDER BY GuildID")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ guilds ]\n')
                for row in rows:
                    print(f'{row}\n\n')
                    print(f'DB.MGMT: fetched all...\n')
                gbic('dbm')

                print(f'WORK ON ME')

            elif search_db == 'items':
                gdb.fetch_items()
                gbic(cmd='dbm')

            elif search_db == 'gusers':
                db.cur.execute("SELECT * FROM gusers ORDER BY gUSERNAME")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ gusers ]\n')
                for row in rows:
                    print(f': {row[0]}\n')
                    print(f'DB.MGMT: fetched all...\n')
                gbic('dbm')

            else:
                gbic('dbm')
        elif db_man == 'build':
            db.build()
            gbic('dbm')

        elif db_man == 'items':
            add_items = input(f'DB.items.. [:] ')
            if add_items == 'add':
                gdb.custom_item()
                gbic('dbm')
                return db_man == 'items'
            elif add_items == 'many':
                gdb.insert_items()
                gbic('dbm')
            elif add_items == 'del':
                gdb.delete_item()
                gbic('dbm')
                return db_man == 'items'
            elif add_items == 'view':
                gdb.fetch_items()
                gbic('dbm')
            else:
                gbic('dbm')

        else:
            gbic('dbm')

    elif cmd == 'post':
        messenger = input(f'POSTAL [:] ')
        if messenger == 'send':
            mess.message_()
            gbic('post')
        if messenger == 'exit':
            gbic('')
        else:
            gbic('post')

    elif cmd == 'game':
        bic_game = input(f'\ngBIC: ')
        if bic_game == '':
            gbic('game')
        elif bic_game == 'exit':
            gbic('')
        elif bic_game == 'new':
            print(f'\n\t-[ gUSER REGISTRATION ]-\n')
            print(f'(pick an arbitrary password as its stored as plaintext for now)\n')
            g_user = input('USER_NAME: ')
            g_pass = input('PASSWORD: ')
            print(
                f'USER_NAME: {g_user}\nPASSWORD: {g_pass}\n\nARE YOU SURE? (Y/n)')
            g_confirm = input('(Y/n): ')
            if g_confirm == 'Y' or 'y':
                db.execute(
                    'INSERT OR IGNORE INTO gusers (gUserName, gPassword) VALUES (?, ?)', g_user, g_pass)
                db.commit()
                print(f'DB.MGMT: gUSER {g_user} added to database')
                gbic('game')
            else:
                gbic('game')
        elif bic_game == 's':
            print(f'SIGN IN')
            guser = (input('gUSER: '))
            gpassw = (input('gPASS: '))

            def ruser():
                user = str(gdb.cur.execute(
                    "SELECT gUserName FROM gusers WHERE gUserName = ?", (guser,)))
                return user

            def rpass():
                passw = str(gdb.cur.execute(
                    "SELECT gPassword FROM gusers WHERE gUserName = ?", (guser,)))
                return passw

            if guser == ruser() and gpassw == rpass():
                input('testing')
            else:
                gbic('game')

        else:
            gbic('game')
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
        print(
            f'\n\n\n\t-[ ACCESS DENIED ]-\n\n\n\n\n\nexiting program...\n\n\n')
        quit()
