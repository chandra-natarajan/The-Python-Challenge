# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 23:36:30 2016

@author: Mouli
"""
#from string import maketrans
#intab = "abcdefghijklmnopqrstuvwxyz"
#outtab = "cdefghijklmnopqrstuvwxyzab"
#trantab = maketrans(intab, outtab)
#print (str.translate(trantab))

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj";
a = "http://www.pythonchallenge.com/pc/def/map.html"
b = '';
for i in range(0, len(a)):
    if (ord(a[i]) in range (97,123)):
        b = b + ( chr(((ord(a[i])-96+2) % 26)+96));
    else:
        b = b +a[i]
print (b);