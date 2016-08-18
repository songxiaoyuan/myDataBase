#-*- coding:utf-8 -*-
import os
import sys
import csv
import MySQLdb

class DataBase(object):
	"""docstring for DataBase"""
	def __init__(self):
		print 'the DataBase is init'
		self.getConnection()
	def __del__(self):
		print 'the database is not connect'
		self.closeConnection()

	def getConnection(self):
		"'connect to the database"
		try:
			db = MySQLdb.connect("localhost","root","111111","test",charset='utf8')
			cursor = db.cursor()
			self.__CURSOR__ = cursor
			self.__DB__ = db
		except Exception, e:
			raise e

	def closeConnection(self):
		"'the is used to close the connect"
		self.__CURSOR__.close()
		self.__DB__.close()

	def getCompanyName(self,companyCode_):
		"'get the company name through company Code"
		sql = 'select Company_name from publiccompany where Company_code = %s' % companyCode_
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()
		# 'return a tuple and the tuple in is another tuple'
		for row in data:
			if len(row) ==0:
				return ''
			else : 
				companyName = row[0]
				return companyName

	def getInformationFromInvestmentRelation(self,companyCode_):
		"'this is used to get information through companyCode, the information is  AcquireeName and StyleOfGetStock"
		getInfomation = ('AcquireeName','StyleOfGetStock',companyCode_)
		sql = 'select %s,%s from investmentrelation where Company_code = %s ' %getInfomation
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()

		returnDic = dict()
		for row in data:
			# import pdb
			# pdb.set_trace()
			StyleOfGetStock = row[1]
			AcquireeName = row[0]
			if StyleOfGetStock in returnDic:
				returnDic[StyleOfGetStock].append(AcquireeName)
			else :
				returnDic[StyleOfGetStock] = []
				returnDic[StyleOfGetStock].append(AcquireeName)
		return returnDic

	def getNameAndPostFromboardofdirectors(self,companyCode_):
		"'this is used to get the name and director form the table boardofdirectors"
		getInfomation = ('name','post',companyCode_)
		sql = 'select %s,%s from boardofdirectors where Company_code = %s' %getInfomation

		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()

		returnDic =dict()
		tmpDicSet = dict()
		# 字典里面先用set，然后在抓换成数组，因为里面是有重复的，
		for row in data:
			name = row[0]
			post = row[1]

			if name in tmpDicSet:
				tmpDicSet[name].add(post)
			else:
				tmpDicSet[name] = set()
				tmpDicSet[name].add(post)

		for item in tmpDicSet:
			returnDic[item] = []
			for itemInSet in tmpDicSet[item]:
				returnDic[item].append(itemInSet)
		return returnDic

	def getNameAndPostFromexecutives(self,companyCode_):
		"'this is used to get name and post from the table executives'"
		getInfomation = ('Name','Post',companyCode_)
		sql = 'select %s,%s from executives where Company_code = %s' % getInfomation

		dontContain = [u'独立董事',u'董事长',u'非执行董事',u'董事',u'执行董事']
		dontContainSet = set(dontContain)

		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()

		returnDic = dict()
		tmpDicSet = dict()

		for row in data:
			name = row[0]
			post = row[1]

			if post in dontContainSet:
				continue
			else:
				if  name in tmpDicSet:
					tmpDicSet[name].add(post)
				else:
					tmpDicSet[name] = set()
					tmpDicSet[name].add(post)
		for item in tmpDicSet:
			returnDic[item] = []
			for itemInSet in tmpDicSet[item]:
				returnDic[item].append(itemInSet)

		return returnDic

	def getKeyWords(self,companyCode_):
		"'this is used to get the key hot words from the table keyhotwords"
		getInfomation = ('keyhotwords',companyCode_,'2016')
		sql = 'select %s from keyhotwords where Company_code = %s and year = %s'%getInfomation
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()

		returnArray = []
		for row in data:
			returnArray = row[0].split(';')
			# returnArray.append(keyword)
		return returnArray

	def getScopeFromCompanyScope(self,companyCode_):
		"'this is used to get the scope from the table companyscope"
		getInfomation = ('scope',companyCode_)
		sql = 'select %s from companyscope where Company_code = %s'%getInfomation
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()

		returnArray = []
		for row in data:
			returnArray = row[0].split(';')
			# returnArray.append(keyword)
		return returnArray

	def getInformationFromNewsSourceCount(self,companyCode_):
		"'this is used to get information through companyCode, the information is  tensource"
		getInfomation = ('tensource',companyCode_)
		sql = 'select %s from newssourcecount where Company_code = %s ' %getInfomation
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()

		returnDic = dict()
		returnDic['name'] = []
		returnDic['count'] = []
		for row in data:
			if len(row) ==0:
				pass
			else:
				# 这是获取到的数据，是一个元组
				data = row[0]
				tenArray = data.split(',')
				# print tenArray
				for item in tenArray:
					itemArray = item.split(';')
					returnDic['name'].append(itemArray[0])
					returnDic['count'].append(itemArray[1])
		return returnDic

	def getInformationFromNewsTimeCount(self,companyCode_):
		"'this is used to get information through companyCode, the information is  timesegment and newscount"
		getInfomation = ('timesegment','newscount',companyCode_)
		sql = 'select %s,%s from newstimecount where Company_code = %s ' %getInfomation
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()

		returnDic = dict()
		for row in data:
			# import pdb
			# pdb.set_trace()
			timesegment = row[0]
			newscount = row[1]
			returnDic[timesegment] = newscount
		return returnDic

	def getInformationFromNewsYearCountAll(self,companyCode_):
		"'this is used to get information through companyCode, the information is  year and newscount"
		getInfomation = ('year','newscount',companyCode_)
		sql = 'select %s,%s from newsyearcountall where Company_code = %s ' %getInfomation
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()

		returnDic = dict()
		for row in data:
			# import pdb
			# pdb.set_trace()
			year = row[0]
			newscount = row[1]
			returnDic[year] = newscount
		return returnDic

	def getInformationFromCompanyReportNumberChange(self,companyCode_):
		"'this is used to get information through companyCode, the information is  reportcompany year and reportnumber"
		getInfomation = ('reportcompany','year','reportnumber',companyCode_)
		sql = 'select %s,%s,%s from companyreportnumberchange where Company_code = %s ' %getInfomation
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()

		returnDic = dict()
		for row in data:
			# import pdb
			# pdb.set_trace()
			reportcompany = row[0]
			year = row[1]
			reportnumber = row[2]
			if year in returnDic:
				returnDic[year][reportcompany] = reportnumber
			else:
				returnDic[year] = dict()
				returnDic[year][reportcompany] = reportnumber
		return returnDic


	def getInformationFromNewsSentiment(self,companyCode_):
		"'this is used to get information through companyCode, the information is  year and sentiment"
		getInfomation = ('year','sentiment',companyCode_)
		sql = 'select %s,%s from newssentiment where Company_code = %s ' %getInfomation
		# print sql
		self.__CURSOR__.execute(sql)
		data = self.__CURSOR__.fetchall()

		returnDic = dict()
		for row in data:
			# import pdb
			# pdb.set_trace()
			year = row[0]
			sentiment = row[1]
			sentimentArray = sentiment.split(',')
			returnDicArray = []
			returnDicArray.append(sentimentArray[0].split(';')[1])
			returnDicArray.append(sentimentArray[1].split(';')[1])
			# print timesegment
			# print newscount
			returnDic[year] = returnDicArray
		return returnDic
	
	def InvReaAndPubCompany(self):
		"'detec the Company_code with publiccompany and investmentrelation'"

		sql1 = 'select Company_code from  investmentrelation'
		sql2 = 'select Company_code from publiccompany'

		companyCodeSet = set()
		self.__CURSOR__.execute(sql2)
		data = self.__CURSOR__.fetchall()
		# import pdb
		# pdb.set_trace()
		for row in data:
			companycode = row[0]
			# print companycode
			companyCodeSet.add(str(companycode))

		# print companyCodeSet
		self.__CURSOR__.execute(sql1)
		data2 = self.__CURSOR__.fetchall()
		# import pdb
		# pdb.set_trace()
		for row in data2:
			companycode = row[0]
			if companycode in companyCodeSet:
				continue
			else : 
				print 'the company_code is not in publiccompany : '+companycode
		print 'Done!'
		

if __name__ == '__main__':
	database = DataBase()
	
	companyname = database.getCompanyName('601900')
	print companyname
	newstimecount = database.getInformationFromCompanyReportNumberChange('000002')
	# print newstimecount
	array = database.getScopeFromCompanyScope('000099')
	print array
	# print companyname==None
	# returnDic = database.getInformationFromInvestmentRelation('000005')
	# print len(returnDic)
	# database.InvReaAndPubCompany()
	# dontContain = [u'独立董事',u'董事长',u'非执行董事',u'董事',u'执行董事']
	# dontContainSet = set(dontContain)
	# print str('独立董事') in dontContain
	# data = database.getNameAndPostFromboardofdirectors('000001')
	# print type(data)
	# print type(dontContain[0])
	# print data in dontContainSet
	# for name in data:
	# 	print 'the name is :' + name+' and the post is :'
	# 	for item in data[name]:
	# 		print item

	

		