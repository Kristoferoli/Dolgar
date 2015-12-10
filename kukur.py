import psycopg2
import numpy as np

host = 'localhost'
username = 'Krissi'
dbname = 'hopaverkefni2' #ykkar database
pw = 1234
try:
    conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)
    print("Connecting to database {}.{} as {}".format(host, dbname, username))
    print("Connected!\n")
except:
    print("I can not connect to the server")

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print("Connected!\n")


movies = ['Toy Story 2 (1999)', 'South Park: Bigger, Longer and Uncut (1999)','American Psycho (2000)']

cursor.execute("Select DISTINCT movieid from moviesdata where title = 'Toy Story 2 (1999)'")

mID = (cursor.fetchall())[0][0]
print(mID)
s = "Select rating from ratingsdata where movieid = {};".format(mID)
cursor.execute(s)

#cursor.execute("Select DISTINCT rating from ratingsdata where movieid = %s;",str(mID))

einkunn = cursor.fetchall()
lowerbound = np.mean(einkunn) - np.std(einkunn)
upperbound = np.mean(einkunn) + np.std(einkunn)
bil=[]
if lowerbound >= 0:
    bil.append(lowerbound)
else:
    bil.append(0)
if lowerbound >= 5:
    bil.append(upperbound)
else:
    bil.append(5)

print("Bilið okkar er",bil)

cursor.execute("Select DISTINCT genres from moviesdata where movieid = '3114';")
genres=cursor.fetchall()[0][0]
genres=genres.split('|')
print(genres)
print(len(genres))
print(genres[4])






cursor.execute("Select title from moviesdata where genres='Adventure|Animation|Children|Comedy|Fantasy';")
titles=cursor.fetchall()
print(titles)
