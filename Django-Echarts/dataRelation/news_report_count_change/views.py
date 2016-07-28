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

# Create your views here.
def home(request):
	companyCode = request.GET.get('CompanyCode')
	database = dataBase.DataBase()
	companyName =database.getCompanyName(companyCode)
	newsCompanyReportNumberDict =database.getInformationFromCompanyReportNumberChange(companyCode)
	if companyName ==None:
		if len(newsCompanyReportNumberDict) ==0 :
			return HttpResponse(companyCode + " : is wrong!! ")
		else:
			return render(request,'news_report_count_change/index.html',{
				'newsCompanyReportNumberDict':json.dumps(newsCompanyReportNumberDict),
				'companyName':json.dumps(companyCode)
				})
	else:
		return render(request,'news_report_count_change/index.html',{
			'newsCompanyReportNumberDict':json.dumps(newsCompanyReportNumberDict),
			'companyName':json.dumps(companyName)
			})
