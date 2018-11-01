import urllib.request
import chardet
urls = open('D:/Desktop/urls.txt')
n = 0
for url in urls:
    respond = urllib.request.urlopen('http://'+url).read()
    encode = chardet.detect(respond)
    respond = respond.decode(str(encode['encoding']))
    n += 1
    with open('D:/Desktop/whale','w') as f:
        f.write(respond)