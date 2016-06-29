import requests
from bs4 import BeautifulSoup
import json
import pymysql


#获取字符串中的数字
def trans2numbers(string):
    return int(''.join(a for a in string.strip() if a.isdigit()))

#sqltest
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='newoa', charset='utf8')
cur = conn.cursor()
cur.execute("SELECT * FROM think_user")
print(cur.description)
for row in cur:
    print(row)
cur.close()
conn.close()

#获取电影id、评分、上映时间
url = 'http://theater.mtime.com/China_Zhejiang_Province_Ningbo/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/49.0.2623.112 Safari/537.36'}
response = requests.get(url, header)
soup = BeautifulSoup(response.text, "html.parser")
soup.li['class'] = "clearfix"
moviesdict = {}
for x in soup.findAll('a', class_="picbox __r_c_"):
    movieid = trans2numbers(x['href'])
    moviesdict[str(movieid)] = x['title']
for (k, v) in moviesdict.items():
    print("dict[%s]=" % k, v)
    response = requests.get("http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType="
                            "Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&"
                            "Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%"
                            "2F" + k + "%2F&t=201662816374949644&Ajax_CallBackArgument0=" + k)
    soup = BeautifulSoup(response.text, "html.parser")
    json_str = str(soup).split('=')
    json_str2 = str(json_str[1]).split(';')
    json1_data = json.loads(json_str2[0])
    ratint = json1_data["value"]["movieRating"]["RatingFinal"]
    if ratint == -1:
        responsemovie = requests.get("http://movie.mtime.com/" + k + "/details.html", header)
        soupmovie = BeautifulSoup(responsemovie.text, "html.parser")
        print(soupmovie.select('.datecont')[1].get_text())
