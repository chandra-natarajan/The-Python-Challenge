# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 11:34:05 2016

@author: Mouli
"""
from urllib.request import urlopen
import re

p = re.compile(r'[\sa-z][A-Z]{3}([a-z])[A-Z]{3}[\sa-z]')

with urlopen('http://www.pythonchallenge.com/pc/def/equality.html') as response:
	for line in response:
		line = line.decode('utf-8')  # Decoding the binary data to text.
		x = p.findall(line)
		if x:
			print(x)