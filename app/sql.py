# sql.py
# SQL Backend Implementation

import pymssql
from app.util import *
import datetime
import random

# host		IP地址
# user      用户名
# password  密码
# database  数据库名称

class SQL_Server():
	def __init__(self, host='192.168.199.1', user='sa', password='123456', database='Factory', autocommit=True):
		self.host = host
		self.user = user
		self.password = password
		self.database = database
		self.autocommit = autocommit
		# following varibles are for data base
		self.tableList = None
		self.attributeList = None

	def connection(self):
		conn = pymssql.connect(host=self.host, user=self.user, password=self.password, database=self.database, autocommit=self.autocommit)
		return conn

	def loginDetect(self, username, password):
		conn = self.connection()
		cursor = conn.cursor()
		username = "'" + username + "'"
		password = "'" + password + "'"
		cursor.execute('SELECT * FROM UserTable WHERE id = ' + username + ' and password = ' + password + ';')
		results = cursor.fetchall()
		cursor.close()
		conn.close()
		return results

	def register(self, username, password):
		# try to insert (username, password) into USERTABLE
		conn = self.connection()
		cursor = conn.cursor()
		username = "'" + username + "'"
		password = "'" + password + "'"
		statement = '(' + username + ', ' + password + ')'
		return self.insertIntoTable('USERTABLE', statement)

	def getTAList(self):
		# get table list
		self.getTableList()

		# get attribute list for each table
		self.getAttributeList()

	def tableDetect(self, tablename):
		# update table and attribute
		self.getTAList()

		if tablename in self.tableList:
			return True
		return False

	def getAttributeListOfTable(self, table):
		index = getIndex(table, self.tableList)
		return self.attributeList[index]

	def getAttributeListForSelectShow(self, table, attribute):
		if attribute == '*':
			return self.getAttributeListOfTable(table)
		return [attribute]

	def selectFromTable(self, table, attribute):
		# update table and attribute
		self.getTAList()

		# SQL query
		conn = self.connection()
		cursor = conn.cursor()
		try:
			if table == 'MAKE' or table == 'ASSEMBLE':
				cursor.execute('SELECT ' + attribute + ' FROM ' + table + ' order by date desc')
			else:
				cursor.execute('SELECT ' + attribute + ' FROM ' + table)
			results = cursor.fetchall()
			return results
		except Exception as e:
			print ('No such query, input again')
		else:
			index = getIndex(table, self.tableList)
			showResults(table, self.attributeList[index], attribute, results)
		finally:
			cursor.close()
			conn.close()

	def insertIntoTable(self, table, insertSQL):
		# update table and attribute
		self.getTAList()

		statement = insertSQL

		# SQL query
		conn = self.connection()
		cursor = conn.cursor()
		try:
			cursor.execute('INSERT INTO ' + table + ' VALUES ' + statement)
		except Exception as e:
			print ('Something error')
			return 'Failed'
		else:
			print ('Succeed')
			return 'Succeeded'
		finally:
			cursor.close()
			conn.close()

	def deleteFromUserTable(self, table, deleteSQL):
		# update table and attribute
		self.getTAList()

		statement = deleteSQL

		# SQL query
		conn = self.connection()
		cursor = conn.cursor()
		try:
			cursor.execute('DELETE FROM ' + table + ' WHERE ' + statement)
		except Exception as e:
			print ('Something error, please input again')
			return 'Failed'
		else:
			print ('Succeed or no such value')
			return 'Succeeded'
		finally:
			cursor.close()
			conn.close()

	def dropTable(self, table):
		# update table and attribute
		self.getTAList()

		# SQL query
		conn = self.connection()
		cursor = conn.cursor()
		try:
			cursor.execute('DROP TABLE ' + table)
		except Exception as e:
			print ('Something error, please input again')
			return 'Failed'
		else:
			print ('Succeed')
			return 'Succeeded'
		finally:
			cursor.close()
			conn.close()

	def getWorkshopID(self):
		# get workshop_id
		results = self.selectFromTable('WORKSHOP', 'workshop_id')
		workshop_id = []
		for res in results:
			workshop_id.append(res[0])
		return workshop_id

	def getWarehouseID(self):
		# get warehouse_id
		results = self.selectFromTable('WAREHOUSE', 'warehouse_id')
		warehouse_id = []
		for res in results:
			warehouse_id.append(res[0])
		return warehouse_id

	def getWorkerID(self):
		# get worker_id
		results = self.selectFromTable('WORKER', 'worker_id')
		worker_id = []
		for res in results:
			worker_id.append(res[0])
		return worker_id

	def getPartID(self):
		# get part_id
		results = self.selectFromTable('PART', 'part_id')
		part_id = []
		for res in results:
			part_id.append(res[0])
		return part_id

	def produceParts(self, part_id, weight, price, warehouse_id, workshop_id):
		# make SQL statement
		# statement1: insert into PART
		statement1 = 'INSERT INTO PART VALUES ( '
		statement1 += "'" + part_id + "', "
		statement1 += weight + ', ' + price + ', '
		statement1 += "'" + warehouse_id + "', "
		statement1 += "'" + workshop_id + "')"

		# statement2: insert into MAKE
		worker_id = random.choice(self.getWorkerID())
		date = datetime.datetime.now().strftime('%Y-%m-%d')
		statement2 = 'INSERT INTO MAKE VALUES ( '
		statement2 += "'" + worker_id + "', "
		statement2 += "'" + part_id + "', "
		statement2 += "'" + date + "')"

		# SQL query
		conn = self.connection()
		cursor = conn.cursor()
		try:
			cursor.execute(statement1)
			cursor.execute(statement2)
		except Exception as e:
			print ('Something error')
			return 'Failed'
		else:
			print ('Succeed')
			return 'Succeeded'
		finally:
			cursor.close()
			conn.close()

	def assembleProducts(self, product_id, class_, price, part_id, warehouse_id):
		# make SQL statement
		# statement1: insert into PRODUCT
		statement1 = 'INSERT INTO PRODUCT VALUES ( '
		statement1 += "'" + product_id + "', "
		statement1 += "'" + class_ + "', "
		statement1 += price + ', '
		statement1 += "'" + warehouse_id + "')"

		# statement2: insert into ASSEMBLE
		date = datetime.datetime.now().strftime('%Y-%m-%d')
		statement2 = 'INSERT INTO ASSEMBLE VALUES ( '
		statement2 += "'" + product_id + "', "
		statement2 += "'" + part_id + "', "
		statement2 += "'" + date + "')"

		# SQL query
		conn = self.connection()
		cursor = conn.cursor()
		try:
			cursor.execute(statement1)
			cursor.execute(statement2)
		except Exception as e:
			print ('Something error')
			return 'Failed'
		else:
			print ('Succeed')
			return 'Succeeded'
		finally:
			cursor.close()
			conn.close()

	def checkState(self):
		# get database's statical information
		# Check the number of workers, warehouses, workshops, parts and products in each factory
		conn = self.connection()
		cursor = conn.cursor()
		statement = """
			select FACTORY.factory_name, COUNT(distinct worker_id) as 'worker_num', COUNT(distinct WAREHOUSE.warehouse_id) as 'warehouse_num', COUNT(distinct WORKSHOP.workshop_id) as 'workshop_num', COUNT(distinct part_id) as 'part_num', COUNT(distinct product_id) as 'product_num'
			from WORKSHOP, WORKER, WAREHOUSE, FACTORY, PART, PRODUCT
			where FACTORY.factory_name = WAREHOUSE.factory_name and FACTORY.factory_name = WORKSHOP.factory_name and WORKER.workshop_id = WORKSHOP.workshop_id and PART.warehouse_id = WAREHOUSE.warehouse_id and PRODUCT.warehouse_id = WAREHOUSE.warehouse_id
			group by FACTORY.factory_name
			"""
		try:
			cursor.execute(statement)
			results = cursor.fetchall()
			return results
		except Exception as e:
			print ('Something error')
			return 'Failed'
		else:
			print ('Succeed')
			return 'Succeeded'
		finally:
			cursor.close()
			conn.close()

	def getTableList(self):
		# get table list
		conn = self.connection()
		cursor = conn.cursor()
		cursor.execute("SELECT Name FROM SysObjects WHERE XType='U' ORDER BY Name")
		self.tableList = cursor.fetchall()
		for i in range(len(self.tableList)):
			self.tableList[i] = self.tableList[i][0]
		cursor.close()
		conn.close()

	def getAttributeList(self):
		# get attribute list for each table
		conn = self.connection()
		cursor = conn.cursor()
		self.attributeList = []
		for table in self.tableList:
			cursor.execute("SELECT column_name FROM information_schema.COLUMNS WHERE table_name='" + table + "'")
			temp = cursor.fetchall()
			for i in range(len(temp)):
				temp[i] = temp[i][0]
			self.attributeList.append(temp)
		cursor.close()
		conn.close()
