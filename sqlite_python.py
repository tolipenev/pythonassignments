# SQLite and Python
# Anatoli Penev
# 15.04.2018
# SQLite integration in Python

import sqlite3
import sys

# connect to the database
conn = sqlite3.connect("C:\\sqlite\\EAL.db") 
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE customer(
                idCust integer NOT NULL,
                name text,
                email text, 
                address text,
                city text)
               """)
conn.commit

# insert data in the table
customer = [('1', 'Per', 'pda@eal.dk', 'MyStreet 1', 'Odense'),
            ('2', 'Artur', 'at@hotmail.com', 'Allstreet 741', 'Vilnius'),
            ('3', 'Alice', 'al@gmail.com', 'Topstreet 56', 'London')]
cursor.executemany("INSERT INTO customer VALUES (?,?,?,?,?)", customer)
conn.commit()

# retrieve data from the table
cursor.execute('''SELECT idCust, name, email, address, city  FROM customer''')
for row in cursor:
    print('{0}, {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2], row[3], row[4]))

# updating data in the table
email = 'alice@gmail.com'
idCust = 3
cursor.execute('''UPDATE customer SET email = ? WHERE id = ? ''',
            (email, idCust))

conn.commit()
