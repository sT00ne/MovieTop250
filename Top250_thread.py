import threading
import requests
from bs4 import BeautifulSoup
import time

# 创建队列
count = 0
threads = []
myLock = threading.RLock()


def open_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/49.0.2623.112 Safari/537.36','cookie':'bid=p-sfE3hLKnI'}
    response = requests.get(url, headers)
    soup = BeautifulSoup(response.text, "html.parser")
    soup.div['class'] = "item"
    moviedict = {}
    listem = []
    for x in soup.findAll("em"):
        listem.append(x.text)
    i = 0
    for x in soup.findAll(class_="hd"):
        name = ""
        for y in x.findAll(class_="title"):
            name += y.text
        moviedict[listem[i]] = name
        i += 1
    for (k, v) in moviedict.items():
        print("dict[%s]=" % k, v)


def main():
    starttime = time.clock()
    l = list(range(250))
    for p in l[::25]:
        url = 'https://movie.douban.com/top250' + "?start=" + str(p) + "&filter="
        t = threading.Thread(target=open_url, args=(url,))  # 线程的执行函数为working
        threads.append(t)
    for t in threads:
        t.setDaemon(True)
        t.start()
    for i in threads:
        i.join()
    endtime = time.clock()
    print("time=", endtime - starttime)


if __name__ == "__main__":
    main()
