thesqlcommands = open('/Users/Krissi/Desktop/HR/Gagnavinnsla/SQL/ml-100k/ratings_demo.dat','r')
userid = []
movieid = []
rating = []
for i in thesqlcommands:
    userid.append(int(i.split('::',1)[0]))
    movieid.append(int(i.split('::',2)[1]))
    rating.append(float(i.split('::',3)[2]))
