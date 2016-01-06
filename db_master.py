
import sqlite3 as lite
import sys
import json




def create_tables():

	con = lite.connect('sqlite.db')

	with con:
		cur = con.cursor()    
		# cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")

		cur.execute("CREATE TABLE favorites(ID INTEGER PRIMARY KEY   AUTOINCREMENT, name TEXT)")
		cur.execute("CREATE TABLE locations(ID INTEGER PRIMARY KEY   AUTOINCREMENT, lat REAL, lon REAL, name TEXT)")

   	con.close()


def insert_favorites(url):

	con = lite.connect('sqlite.db')

	with con:
	
		cur = con.cursor()    
	
		cur.execute("INSERT INTO favorites (name) VALUES(?)",(url,))

	con.close()


def insert_location(lat=15.4444,lon=33.5334333,name='Timbuktu'):

	con = lite.connect('sqlite.db')

	with con:
	
		cur = con.cursor()    
	
		cur.execute("INSERT INTO locations (lat, lon, name) VALUES(?, ?, ?)",(lat, lon, name,))

	con.close()



def get_favorites():

	con = lite.connect('sqlite.db')

	with con:
		
		cur = con.cursor()
		cur.execute("SELECT * FROM favorites")

	rows = cur.fetchall()

	con.close()

	l=[]
	for row in rows:
	    print row
	    l.append(row[1])
	
	

	return json.dumps(l)
	


def get_locations():

	con = lite.connect('sqlite.db')

	with con:
		
		cur = con.cursor()
		cur.execute("SELECT * FROM locations")

	rows = cur.fetchall()

	for row in rows:
	    print row
	
	con.close()



#create_tables()
#insert_favorites()

# print get_favorites()



# insert_location()

# get_locations()