import re
import urllib.request


def getmovie(i, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/48.0.2564.116 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    page = urllib.request.urlopen(req)
    contentBytes = page.read()
    contentBytes = contentBytes.decode('utf-8')
    divre = r'<div class="hd">([\s\S]*?)</div>'
    divtext = re.findall(divre, contentBytes)
    movienames = {}
    # i = 1
    for text in divtext:
        spanre = r'<span class="title">([\s\S]*?)</span>'
        spantext = re.findall(spanre, text)
        singlemoviename = ""
        for name in spantext:
            singlemoviename += name
        singlemoviename = singlemoviename.replace("&nbsp;", "")
        singlemoviename = singlemoviename.replace("&#39;", "\'")
        movienames[i] = singlemoviename
        i += 1
    for (k, v) in movienames.items():
        print("dict[%s]=" % k, v)
    return i, movienames


url = "https://movie.douban.com/top250"
page = 0
i = 1
movienames = {}
while page < 226:
    pageurl = "?start=" + str(page) + "&filter="
    movieurl = url + pageurl
    i, movienamedict = getmovie(i, movieurl)
    movienames.update(movienamedict)
    page += 25
