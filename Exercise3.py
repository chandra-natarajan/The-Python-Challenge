# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 11:34:05 2016

@author: Mouli
"""
import urllib.request
import re

fname = 'text.txt'
urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/equality.html', fname)
with open(fname) as f:
    content = f.readlines()
for line in content:
    p = re.compile(r'[\sa-z][A-Z]{3}([a-z])[A-Z]{3}[\sa-z]')
    x = p.findall(line)
    if x:
        print(x)
