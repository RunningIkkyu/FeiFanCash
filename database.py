import sqlite3
import os
import datetime
DBFILENAME = "FeiFanAccount"


def db_init():
    conn = sqlite3.connect(DBFILENAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cash 
            (item text, price real, note text, customer text, owed bool, day date, ts timestamp)''')
    conn.commit()
    conn.close()


def db_insert(item, price, note='', customer='', owed=False):
    conn = sqlite3.connect(DBFILENAME)
    c = conn.cursor()
    now = datetime.datetime.now()
    today = datetime.date.today()
    c.execute('''INSERT INTO cash VALUES(?,?,?,?,?,?,?)''', (item, price, note, customer, owed, today, now))
    conn.commit()
    conn.close()


def show_today():
    conn = sqlite3.connect(DBFILENAME)
    c = conn.cursor()
    today = datetime.date.today()
    c.execute('''SELECT * FROM cash WHERE day = '%s' '''% str(today))
    l = c.fetchall()
    for i in l:
        print(i)
    conn.close()


def db_update(ts, item, price, note='', customer='', owed=False):
    conn = sqlite3.connect(DBFILENAME)
    c = conn.cursor()
    c.execute("""UPDATE cash SET item=?, price=?, note=?, customer=?, owed=? WHERE ts = ?""",
              (item, price, note, customer, owed, ts,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    db_init()
    show_today()


