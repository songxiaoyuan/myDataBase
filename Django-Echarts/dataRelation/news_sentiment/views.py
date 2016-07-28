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
	newsSentimentDict =database.getInformationFromNewsSentiment(companyCode)
	if companyName ==None:
		if len(newsSentimentDict) ==0 :
			return HttpResponse(companyCode + " : is wrong!! ")
		else:
			return render(request,'news_sentiment/index.html',{
				'newsSentimentDict':json.dumps(newsSentimentDict),
				'companyName':json.dumps(companyCode)
				})
	else:
		return render(request,'news_sentiment/index.html',{
			'newsSentimentDict':json.dumps(newsSentimentDict),
			'companyName':json.dumps(companyName)
			})
