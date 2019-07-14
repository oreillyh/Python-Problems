import pymysql

conn = None

def connect():
	global conn
	conn = pymysql.connect(host="localhost", user="root", password="root", db="World", cursorclass=pymysql.cursors.DictCursor)

def view_15():
		if (not conn):
		connect();
	print("Choice:1")
		query = "SELECT * FROM city where id<16;"
		
		with conn:
			cursor = conn.cursor()
			cursor.execute(query)