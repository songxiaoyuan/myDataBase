# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import sys
# add the module  path of python
PYTHON_DIR = os.path.dirname(os.path.abspath(__file__))
tmp = os.path.join(PYTHON_DIR, '..', 'database')
sys.path.append(tmp)
import dataBase

def home(request):
	companyCode = request.GET.get('CompanyCode')
	database = dataBase.DataBase()
	companyName =database.getCompanyName(companyCode)
	newstimecountDict =database.getInformationFromNewsTimeCount(companyCode)
	if companyName ==None:
		if len(newstimecountDict) ==0 :
			return HttpResponse(companyCode + " : is wrong!! ")
		else:
			return render(request,'news_publish_time_count/index.html',{
				'newstimecountDict':json.dumps(newstimecountDict),
				'companyName':json.dumps(companyCode)
				})
	else:
		return render(request,'news_publish_time_count/index.html',{
			'newstimecountDict':json.dumps(newstimecountDict),
			'companyName':json.dumps(companyName)
			})