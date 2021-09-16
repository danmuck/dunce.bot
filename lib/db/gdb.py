#gBIC db commands
from os.path import isfile
from sqlite3 import connect, IntegrityError

# from apscheduler.triggers.cron import CronTrigger

DB_PATH = './data/db/database.db'
BUILD_PATH = './data/db/build.sql'

conn = connect(DB_PATH, check_same_thread=False)
cur = conn.cursor()


#SINGLE --- --- --- --- --- --- --- --- --- ---

item_id = ('000015')
# item_id required [count it]
item_name = ('bippity')
# item_name
item_desc = ('bop')
# item_description
item_cat = ('test')
# item_category
# weapon | armor | consume | common |  uncommon | rare | priceless | !event | test 
# !example = specific

def insert_item():
    cur.execute("INSERT INTO items VALUES (?, ?, ?, ?)", [(item_id), (item_name or None), (item_desc or None), (item_cat or None)])

    print(f'\n\t-[ NEW ITEM ADDED ]-\n\n\nitem_id: {item_id}\nitem_name: {item_name}\nitem_desc: {item_desc}\nitem_cat: [ {item_cat} ]  \n')

    print(f'DB.MGMT: [ items ] commited...\n')
    conn.commit()
    # conn.close()


#MANY --- --- --- --- --- --- --- --- --- --- 

item_0 = (
    '000000',
    'book of dirtpig',
    'the law',
    'global'
)
item_1 = (
    '000001',
    'test_sword',
    'fake sword',
    'weapons'
)
item_2 = (
    '000002',
    'test_bow',
    'fake bow',
    'weapons'
)
item_3 = (
    '000003',
    'test_pillow',
    'sick armor',
    'armor'
)
item_4 = (
    '000004',
    'test_bread',
    'its a bread',
    'consume'
)
many_items = [
                item_0,
                item_1,
                item_2,
                item_3,
                item_4
]

def insert_items():
    cur.executemany("INSERT or IGNORE INTO items VALUES (?, ?, ?, ?)", many_items)

    print(f'\n\t-[ NEW ITEM ADDED ]-\n\n\n[ {item_0[3]} ]\nitem_id: {item_0[0]}\nitem_name: {item_0[1]}\nitem_desc: {item_0[2]}\n')
    print(f'\n\t-[ NEW ITEM ADDED ]-\n\n\n[ {item_1[3]} ]\nitem_id: {item_1[0]}\nitem_name: {item_1[1]}\nitem_desc: {item_1[2]}\n')
    print(f'\n\t-[ NEW ITEM ADDED ]-\n\n\n[ {item_2[3]} ]\nitem_id: {item_2[0]}\nitem_name: {item_2[1]}\nitem_desc: {item_2[2]}\n')
    print(f'\n\t-[ NEW ITEM ADDED ]-\n\n\n[ {item_3[3]} ]\nitem_id: {item_3[0]}\nitem_name: {item_3[1]}\nitem_desc: {item_3[2]}\n')
    print(f'\n\t-[ NEW ITEM ADDED ]-\n\n\n[ {item_4[3]} ]\nitem_id: {item_4[0]}\nitem_name: {item_4[1]}\nitem_desc: {item_4[2]}\n')
    conn.commit()
    # conn.close()
    print(f'DB.MGMT: [ items ] commited...\n')


#CUSTOM --- --- --- --- --- --- --- --- --- --- 
def custom_item():
    cust_id = (input('\nID#: '))
    cust_name = (input('NAME: '))
    cust_desc = (input('DESC: '))
    cust_cat = (input('CAT: '))
    cur.execute("INSERT or IGNORE INTO items VALUES (?, ?, ?, ?)", [(cust_id), (cust_name or None), (cust_desc or None), (cust_cat or None)])
    
    print(f'\n\t-[ NEW ITEM ADDED ]-\n\n\nitem_id: {cust_id}\nitem_name: {cust_name}\nitem_desc: {cust_desc}\nitem_cat: [ {cust_cat} ]  \n')
    

    print(f'DB.MGMT: [ items ] commited...\n')
    conn.commit()
    # conn.close()


#FETCH
def fetch_items():
    cur.execute('SELECT rowid, * FROM items ORDER BY ItemID ASC')
    items = cur.fetchall()
    for item in items:
        print(f'\n\t[ {item[4]} ]\nitem_name: {item[2]}\nitem_desc: {item[3]}\nitem_id: {item[1]}\n\n')
    print(f'\nDB.MGMT: fetched all...\n')

if __name__ == '__main__':
    fetch_items()
    conn.close()
    print(f'\nDB.MGMT: items fetched...\nDB.MGMT: database connection closed')  

# end ---
    