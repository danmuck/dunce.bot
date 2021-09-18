# client import
from lib.db import db, gdb
from lib.messenger import mess
from lib.client import client
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
                \n   :run         :db man     :post        :game       [:]items
                \n
                \n   :bot        [:]view     [:]send      [:]new user   :add     
                \n
                \n   :run        [:]items     :           [:]           :del
                \n
                \n   :?          [:]build     :           [:]          [*]exit

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

    elif cmd == 'db man':
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
                gbic('db man')

            elif search_db == 'exp':
                db.cur.execute("SELECT * FROM exp ORDER BY XP DESC")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ exp ]\n')
                for row in rows:
                    print(
                        f'user: {row[1]}\nlevel: {row[3]} \ntotal xp: {row[2]}\nlock expires: {str(row[4])[11:]} UTC\n\n')
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

                print(f'WORK ON ME IN system.py?')

            elif search_db == 'items':
                gdb.fetch_items()
                gbic('db man')

            elif search_db == 'gusers':
                db.cur.execute("SELECT * FROM gusers ORDER BY gUSERNAME")
                rows = db.cur.fetchall()
                print(f'\nDISPLAYING CONTENT: [ gusers ]\n')
                for row in rows:
                    print(f': {row[0]}\n')
                    print(f'DB.MGMT: fetched all...\n')
                gbic('db man')

            else:
                gbic('db man')
        elif db_man == 'build':
            db.build()
            gbic('db man')

        elif db_man == 'items':
            add_items = input(f'DB.items.. : ')
            if add_items == 'help':
                print(f'''
                        ITEM CLASSIFIERS
                        \nweapon | armor | consume | common |  uncommon | rare | NFT | !event | test 
                        \n!example = specific\n''')
                gbic('db man')
            elif add_items == 'add':
                gdb.custom_item()
                gbic('db man')
                return db_man == 'items'
            elif add_items == 'many':
                gdb.insert_items()
                gbic('db man')
            elif add_items == 'del':
                gdb.delete_item()
                gbic('db man')
                return db_man == 'items'
            elif add_items == 'view':
                gdb.fetch_items()
                gbic('db man') 
            elif add_items == 'purge!':
                gdb.purge_items()
                gbic('db man')
            else:
                gbic('db man')

        else:
            gbic('db man')

    elif cmd == 'post':
        messenger = input(f'POSTAL [:] ')
        if messenger == 'send':
            mess.message_()
            gbic('post')
        if messenger == 'exit':
            gbic('')
        else:
            gbic('post')

    elif cmd == 'gb':
        bic_game = input(f'\ngBIC: ')
        if bic_game == '':
            gbic('gb')
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
                gbic('gb')
            else:
                gbic('gb')
        elif bic_game == 's':
            print(f'SIGN IN')
            guser = (input('gUSER: '))
            gpassw = (input('gPASS: '))

            def ruser():
                gdb.cur.execute(
                    "SELECT gUserName FROM gusers WHERE gUserName = ?", (guser,))
                user = gdb.cur.fetchone()
                return (user,)

            def rpass():
                gdb.cur.execute(
                    "SELECT gPassword FROM gusers WHERE gUserName = ?", (gpassw,))
                passw = gdb.cur.fetchone()
                return (passw,)

            if (guser,) == ruser() and (gpassw,) == rpass():
                print('testing')

            else:
                gbic('game')

        else:
            gbic('game')

    elif cmd == 'td':
        todo_ = input('TODO [:] ')
        if todo_ == 'view':
            gdb.cur.execute('SELECT * FROM todo_ ORDER BY Added')
            gdb.cur.fetchall()
            gbic('td')
        elif todo_== 'add':

            gbic('td')
        elif todo_ == 'del':

            gbic('td')
        elif todo_ == 'exit':
            gbic('')
        else:
            gbic('td')
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
