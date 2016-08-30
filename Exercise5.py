# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 10:33:05 2016

@author: Mouli
"""
from urllib.request import urlopen
import pickle
banner = r'http://www.pythonchallenge.com/pc/def/banner.p'
for line in pickle.load(urlopen(banner)):
	for item in line:
		print(item[0]*item[1], end='')
	print()