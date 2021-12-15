import sqlite3
from sqlite3.dbapi2 import IntegrityError

def startdb():
    global cur,conn
    conn=sqlite3.connect("bdays.db")
    cur=conn.cursor()

def connect():
    startdb()
    cur.execute("CREATE TABLE IF NOT EXISTS bday (name TEXT PRIMARY KEY, day INTEGER, month INTEGER, year INTEGER)")
    conn.commit()
    conn.close()

def add(name,day,month,year):
    startdb()
    try:
        cur.execute("INSERT INTO bday VALUES (?,?,?,?)",(name,day,month,year))
    except IntegrityError:
        cur.execute("UPDATE bday SET day=?, month=?, year=? WHERE name=?",(day,month,year,name))
    conn.commit()
    conn.close()

def view():
    startdb()
    cur.execute("SELECT * FROM bday ORDER BY name")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name,day,month,year):
    startdb()
    if name:
        cur.execute("SELECT * FROM bday WHERE name LIKE ?",(name,))
    elif day and month and year:
        cur.execute("SELECT * FROM bday WHERE day=? AND month=? AND year LIKE ?",(day,month,year))
    elif day and month:
        cur.execute("SELECT * FROM bday WHERE day=? AND month=?",(day,month))
    elif day and year:
        cur.execute("SELECT * FROM bday WHERE day=? AND year LIKE ?",(day,year))
    elif month and year:
        cur.execute("SELECT * FROM bday WHERE month=? AND year LIKE ?",(month,year))
    elif day:
        cur.execute("SELECT * FROM bday WHERE day=?",(day,))
    elif month:
        cur.execute("SELECT * FROM bday WHERE month=?",(month,))
    elif year:
        cur.execute("SELECT * FROM bday WHERE year LIKE ?",(year,))
    else:
        cur.execute("SELECT * FROM bday WHERE name=? OR day=? OR month=? OR year=?",(name,day,month,year))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(name):
    startdb()
    cur.execute("DELETE FROM bday WHERE name=?",(name,))
    conn.commit()
    conn.close()

def count_months():
    startdb()
    cur.execute("SELECT month, COUNT(name) FROM bday GROUP BY month")
    rows=cur.fetchall()
    conn.close()
    return rows

connect()

if __name__=="__main__":
    #add("Vitez Koja",1,2,1984)
    #delete('Sima Simić')
    #print(view())
    print(search(month=8))
    print(count_months())
