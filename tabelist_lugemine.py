import sqlite3

ühendus = sqlite3.connect('andmebaas.db')
c = ühendus.cursor()

c.execute("SELECT * FROM õppijad WHERE perenimi = 'Kivi'")

for row in c:
   print("eesnimi = ", row[0])
   print("perenimi = ", row[1])

c.execute("SELECT * FROM õppijad WHERE perenimi = 'Kivi'")
print(c.fetchall())

ühendus.close()