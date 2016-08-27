import urllib.request

response = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")

page_source = response.read()

print (page_source)