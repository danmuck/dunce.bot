# gBIC db commands
# from cli_launcher import gbic
from sqlite3 import connect, IntegrityError

# from apscheduler.triggers.cron import CronTrigger

DB_PATH = './data/db/database.db'
BUILD_PATH = './data/db/build.sql'

conn = connect(DB_PATH, check_same_thread=False)
cur = conn.cursor()

def insert_todo():
    todo = (input('\nTO:DO \n:'),)
    cur.execute("INSERT INTO todo_ VALUES (?, CURRENT_TIMESTAMP)", todo)
    print(f'\nTO:DO added')
    print(f'DB.ADD: changes commited...\n')
    conn.commit()
    # conn.close()

def fetch_todo():
    cur.execute('SELECT rowid, * FROM todo_ ORDER BY Added ASC')
    items = cur.fetchall()
    for item in items:
        print(
            f'\n[{item[0]}: {item[2]}]\n\n{item[1]}')
    print(f'\nDB.items: fetched all...\n')


if __name__ == '__main__':
    fetch_todo()
    