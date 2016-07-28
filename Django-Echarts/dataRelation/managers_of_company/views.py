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
	directorsOfCompany =database.getNameAndPostFromboardofdirectors(companyCode)
	executivesOfCompany =database.getNameAndPostFromexecutives(companyCode)
	if companyName ==None:
		if len(directorsOfCompany) ==0 and len(executivesOfCompany) ==0:
			return HttpResponse(companyCode + " : is wrong!! ")
		else:
			return render(request,'managers_of_company/index.html',{
				'directorsOfCompany':json.dumps(directorsOfCompany),
				'executivesOfCompany':json.dumps(executivesOfCompany),
				'companyName':json.dumps(companyCode)
				})
	else:
		return render(request,'managers_of_company/index.html',{
			'directorsOfCompany':json.dumps(directorsOfCompany),
			'executivesOfCompany':json.dumps(executivesOfCompany),
			'companyName':json.dumps(companyName)
			})
