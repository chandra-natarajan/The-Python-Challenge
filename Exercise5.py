# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 10:33:05 2016

@author: Mouli
"""
from urllib.request import urlopen
import pickle, pprint

htmlFile = r'http://www.pythonchallenge.com/pc/def/banner.p'
p = pickle.load(urlopen(htmlFile))
for item in p:
	print (item)