import re
import urllib.request
import requests
from bs4 import BeautifulSoup


# 使用自带的库
def getmovie(i, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/48.0.2564.116 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    pagesource = urllib.request.urlopen(req)
    pagecontent = pagesource.read()
    pagecontent = pagecontent.decode('utf-8')
    divre = r'<div class="hd">([\s\S]*?)</div>'
    divtext = re.findall(divre, pagecontent)
    movienamesdict = {}
    # i = 1
    for text in divtext:
        spanre = r'<span class="title">([\s\S]*?)</span>'
        spantext = re.findall(spanre, text)
        singlemoviename = ""
        for name in spantext:
            singlemoviename += name
        singlemoviename = singlemoviename.replace("&nbsp;", "")
        singlemoviename = singlemoviename.replace("&#39;", "\'")
        movienamesdict[i] = singlemoviename
        i += 1
    # for (k, v) in movienamesdict.items():
    #     print("dict[%s]=" % k, v)
    return i, movienamesdict


# 使用Requests以及BeautifulSoup库
def getmovie_requests(i, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    soup.div['class'] = "item"
    moviedict = {}
    for x in soup.findAll(class_="hd"):
        name = ""
        for y in x.findAll(class_="title"):
            name += y.text
        moviedict[i] = name
        i += 1
    return i, moviedict


url = "https://movie.douban.com/top250"
page = 0
i = 1
movienames = {}
while page < 226:
    pageurl = "?start=" + str(page) + "&filter="
    movieurl = url + pageurl
    i, movienamedict = getmovie_requests(i, movieurl)
    movienames.update(movienamedict)
    page += 25
for (k, v) in movienames.items():
    print("dict[%s]=" % k, v)
