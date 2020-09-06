'''
	host: localhost
	user: root
	password: 
	port: 
	database: thuctaphe
'''
from mysql import connector

class database():

	def __init__(self, host, user, password, table, port=3306):
		self.host = host
		self.user = user
		self.password = password
		self.table = table
		self.port = port

	def connect(self):
		self.conn = connector.connect(
			host=self.host, 
			user=self.user, 
			password=self.password, 
			database=self.table, 
			port = self.port,
			charset="utf8",
			use_unicode=True
			)
		self.cursor = self.conn.cursor()
			
	def select(self, sql):
		self.connect()
		self.cursor.execute(sql)

	def fetch(self):
		result = self.cursor.fetchall()
		self.cursor.close()
		return 0 if result is None else result

	def insert_data(self, sql, val):
		self.connect()
		self.cursor.execute(sql, val)
		self.conn.commit()
		print(self.cursor.rowcount, "record(s) affected")
		self.cursor.close()
	#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
	#val = ("John", "Highway 21")

	def delete(self, sql):
		self.connect()
		self.cursor.execute(sql)
		self.conn.commit()
		print(self.cursor.rowcount, "record(s) deleted")
		self.cursor.close()

	def update(self, sql):
		self.connect()
		self.cursor.execute(sql)
		self.conn.commit()
		print(self.cursor.rowcount, "record(s) affected")
		self.cursor.close()	
	

def create_list(data, dt):
	data.select('select id from nhanvien')
	result = pandas.DataFrame(data.fetch())
	for i in result[0]:
		data.insert_data('INSERT INTO diemdanh (id,idnv,ngay,checkin,miss) VALUES (%s,%s,%s,%s,%s)',('', i,dt, 0,0))