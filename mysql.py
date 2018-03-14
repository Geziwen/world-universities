#!/anaconda/bin/python

import csv
import json
import MySQLdb

# Type your DB configuration here

HOST = ""
USER = ""
PWD = ""
DB = ""

connection = MySQLdb.connect(HOST, USER, PWD, DB)
cursor = connection.cursor()

index = 0
with open("world-universities.csv") as f:
    reader = csv.reader(f)
    for line in reader:
        command = "INSERT INTO universities(id, name, country, website) VALUES ('%d', '%s', '%s', '%s')" % (index, line[1], line[0], line[2])
        index += 1
        try:
            cursor.execute(command)
            connection.commit()
        except:
            connection.rollback()

connection.close()
