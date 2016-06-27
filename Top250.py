import re
import urllib.request

url = "https://movie.douban.com/top250"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
req = urllib.request.Request(url=url, headers=headers)
page = urllib.request.urlopen(req)
contentBytes = page.read()
# contentBytes = contentBytes.decode('utf-8','ignore')
# contentBytes = contentBytes.encode('utf-8')
# contentBytes = contentBytes.decode('utf-8')
# # print(contentBytes)
# with open('e:/pp/webapp/www/a.txt', 'w', encoding='utf-8') as f:
#      f.write(contentBytes)
contentBytes = contentBytes.decode('utf-8')
divre = r'<div class="hd">([\s\S]*?)</div>'
divtext = re.findall(divre, contentBytes)
for text in divtext:
    spanre = r'<span class="title">([\s\S]*?)</span>'
    spantext = re.findall(spanre, text)

spantext = re.findall(r'<div class="hd">(.*)</div>', text)
# images = re.findall(r'^https://[0-9a-zA-Z]*(png|gif|jpg)',str(contentBytes))
# print(images)
# for link,t in images:
# 	urllib.request.urlretrieve("https://img3.doubanio.com/view/photo/thumb/public/p"+link+"."+t,"img/"+link+"."+t)
