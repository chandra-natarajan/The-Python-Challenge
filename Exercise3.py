# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 11:34:05 2016

@author: Mouli
"""
import urllib.request
import re

fname = 'text.txt'
urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/equality.html', fname)
#fname = 'text1.txt'

with open(fname) as f:
    content = f.readlines()
dictionary ={}

for line in content:
    p = re.compile(r'A-ZA-ZA-Za-zA-ZA-ZA-Z')
    p.search(line)
    print (p.findall(line))
