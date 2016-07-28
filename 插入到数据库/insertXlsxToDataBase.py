#-*- coding:utf-8 -*-
import os
import sys
import csv
import MySQLdb
from openpyxl import Workbook
from openpyxl import load_workbook

def insertInoDataBase():
	try:
		db = MySQLdb.connect(host = "localhost",user = "root",passwd="111111",db="test", charset='utf8')
		cursor = db.cursor()
		xlsxPath = './data.xlsx'
		xlsxFileReader = load_workbook(xlsxPath)
		index = 1
		for sheet in xlsxFileReader.get_sheet_names() :
			print sheet
			sheet_ranges = xlsxFileReader[sheet]
			for row in sheet_ranges.rows :
				if index ==1:
					index = index + 1
					continue
				# print len(row)
				insertRow = [] 
				for cell in row:
					# print type(cell.value)
					# import pdb
					# pdb.set_trace()
					if type(cell.value) == unicode:
						insertRow.append(cell.value.encode('utf-8'))
					else :
						# print 'the cell of value is '+cell.value + ' : and the type is '+type(cell.value)
						insertRow.append(str(cell.value))
					# insertRow.append(str(cell.value.encode('utf-8')))
				# for tmp in insertRow:
				# 	if type(tmp) ==str:
				# 		continue
				# 	else:
				# 		# print type(tmp)
				# 		print  tmp
				insertSql = 'insert into investmentrelation values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
				cursor.execute(insertSql,insertRow)

		# 	pass
		# for line in csvFile:
		# 	if index ==1:
		# 		index = index +1
		# 		continue
		# 	else :
		# 		cells =line.split(',')
		# 		insertRow = []
		# 		for x in xrange(0,7):
		# 			insertRow.append(cells[x].strip())
		# 		# print len(insertRow)
		# 		# import pdb
		# 		# pdb.set_trace()
		# 		insertSql = 'insert into investmentrelation values(%s,%s,%s,%s,%s,%s,%s)'
		# 		cursor.execute(insertSql,insertRow)
		# 		# if index ==2 :
		# 		# 	break
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

