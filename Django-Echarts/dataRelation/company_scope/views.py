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
	scopeArray = database.getScopeFromCompanyScope(companyCode)
	if companyName ==None:
		if len(scopeArray) != 0:
			return render(request,'investment_relation/index.html',{
				'scopeArray':  json.dumps(scopeArray),
				'companyName':  json.dumps(companyCode)
				})
		else:
			return HttpResponse(companyCode + " : is not found the companyName")
	elif len(scopeArray) ==0:
		return HttpResponse(companyCode +"the company name is : "+companyName + "is not found investment relation")
	else:
		return render(request,'investment_relation/index.html',{
			'scopeArray':  json.dumps(scopeArray),
			'companyName':  json.dumps(companyName)
			})