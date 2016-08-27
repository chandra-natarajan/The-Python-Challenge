# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 11:34:05 2016

@author: Mouli
"""
import urllib.request
import re

fname = 'text.txt'
urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/ocr.html', fname)

with open(fname) as f:
    content = f.readlines()
dictionary ={}

for line in content:
    if(re.search(r'%',line)):
        for i in line:
            if i in dictionary.keys():
                dictionary[i] += 1
            else:
                dictionary[i] = 1

for key in dictionary.keys():
    if dictionary[key] < 10:
        print (str(key)+' : '+ str(dictionary[key]))