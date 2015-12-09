import psycopg2
import getpass
import random as r


host = 'localhost'
#dbname = input('Database name: ')
dbname = 'hlodver'

#username = input('User name for {}.{}: '.format(host,dbname))
username = 'postgres'
#pw = getpass.getpass()
pw = 1234

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

print("Connecting to database {}.{} as {}".format(host, dbname, username))

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

print("Connected!\n")
thesqlcommands = open('movies.dat','r') #moguleiki ad tad turfi ad breyta slodinni
for i in thesqlcommands:
    index = int(i.split('::',1)[0])
    Title = i.strip('::').split('::',2)[1]
    Genre = i.split('::',2)[2].strip().split('|')
    print([index], [Title], Genre)
