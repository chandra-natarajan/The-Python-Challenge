# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 11:34:05 2016

@author: Mouli
"""
from urllib.request import urlopen
import re 

def crawlNext( htmlEnd ):
	htmlStart = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
	p = re.compile(r'next nothing is (\w+)')
	for i in range(250): #assume max iteration as 250
		#print (i)
		with urlopen(htmlStart+htmlEnd) as response:
			for line in response:
				line = line.decode('utf-8')  # Decoding the binary data to text.
				x = p.findall(line)
			if x:				
				htmlEnd = x[0]
			else:
				print (htmlEnd)
				print(line)
				break
	return htmlEnd

htmlEnd = r'12345'
htmlEnd = crawlNext(htmlEnd)
htmlEnd = str(int(htmlEnd)/2)
htmlEnd = crawlNext(htmlEnd)