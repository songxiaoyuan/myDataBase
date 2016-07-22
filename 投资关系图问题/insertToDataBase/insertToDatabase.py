#-*- coding:utf-8 -*-
import os
import sys
import csv
import MySQLdb

def insertInoDataBase():
	try:
		db = MySQLdb.connect(host = "localhost",user = "root",passwd="111111",db="test", charset='utf8')
		cursor = db.cursor()
		csvPath = './data.csv'
		csvFile = open(csvPath)
		index = 1
		for line in csvFile:
			if index ==1:
				index = index +1
				continue
			else :
				cells =line.split(',')
				insertRow = []
				for x in xrange(0,7):
					insertRow.append(cells[x].strip())
				# print len(insertRow)
				# import pdb
				# pdb.set_trace()
				insertSql = 'insert into investmentrelation values(%s,%s,%s,%s,%s,%s,%s)'
				cursor.execute(insertSql,insertRow)
				# if index ==2 :
				# 	break
		db.commit()
		cursor.close()
		db.close()
	except Exception, e:
		raise e
		# pass
	
if __name__ == '__main__':
	# for x in xrange(0,7):
	# 	print x
	insertInoDataBase()

# def creatTableInvestmentRelation():
# 	sql = 'create table investmentrelation (
# 		Company_code  char(100) 
# 		Year   date
# 		AcquireeName  char(100)
# 		DateToGetStock  date
# 		CostToGetStock  double(30,10)
# 		ProportionOfGetStock  double(30,10)
# 		StyleOfGetStock  char(100)
# 	)'

