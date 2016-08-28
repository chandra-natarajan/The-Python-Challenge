# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 11:34:05 2016

@author: Mouli
"""
from urllib.request import urlopen
import re 

htmlStart = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
htmlEnd = r'12345'
htmlEndArray=['12345']
p = re.compile(r'next nothing is (\w+)')
q = re.compile(r'\D')
for i in range(250):
	with urlopen(htmlStart+htmlEnd) as response:
		for line in response:
			line = line.decode('utf-8')  # Decoding the binary data to text.
			x = p.findall(line)
			if x:				
				htmlEnd =x[0]
				htmlEndArray.extend(x)
				y = q.findall(x[0])
				if y:
					break				

print (htmlEndArray)