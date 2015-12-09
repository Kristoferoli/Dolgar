import psycopg2
import getpass
import random as r
import pandas as pd




host = 'localhost'
#dbname = input('Database name: ')
dbname = 'hopaverkefni2'

#username = input('User name for {}.{}: '.format(host,dbname))
username = 'Krissi'
#pw = getpass.getpass()
pw = 1234

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

print("Connecting to database {}.{} as {}".format(host, dbname, username))

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

print("Connected!\n")
thesqlcommands = open('/Users/Krissi/Desktop/HR/Gagnavinnsla/SQL/ml-100k/movies.dat','r') #moguleiki ad tad turfi ad breyta slodinni
for i in thesqlcommands:
    index = int(i.split('::',1)[0])
    #Title = i.strip('::').split('::',2)[1]
    Title = i.split('::',1)[1].rsplit('(',1)[0].strip()
    Year = i.rsplit(')',1)[0].rsplit('(',1)[1]
    Genre = i.split('::',2)[2].strip().split('|')
    print([index], [Title], [Year], Genre)
