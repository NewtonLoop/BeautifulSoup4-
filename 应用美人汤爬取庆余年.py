import urllib.request
from bs4 import BeautifulSoup
import re
import codecs



url = "http://www.aixiawx.com/16/16039"
response = urllib.request.urlopen(url)
with urllib.request.urlopen(url,timeout=30) as rep:
    rep.read()

soup=BeautifulSoup(response,'html.parser')

print(soup.a)


file = codecs.open("YuNianTest13", "wb", "utf-8")
file.close
for link in soup.find_all('a'):
    x = link.get('href')
    r2 = re.compile('/16/16039/1', re.I)


    if r2.search(x):
        print(link.text)
        url = "http://www.aixiawx.com" + link.get('href')
        with urllib.request.urlopen(url, timeout=30) as rep:
            rep.read()
        response1 = urllib.request.urlopen(url)
        soup = BeautifulSoup(response1, 'html.parser')
        x1 = soup.find(id='content')
        file = codecs.open("YuNianTest13", "a+", "utf-8")
        file.write(link.text)
        file.write('\n')
        file.write(x1.get_text())
        file.close
    #
    # elif r3.search(x):
    #     print(link.text)
    #     url = "http://www.aixiawx.com" + link.get('href')
    #     with urllib.request.urlopen(url, timeout=30) as rep:
    #         rep.read()
    #     response1 = urllib.request.urlopen(url)
    #     soup = BeautifulSoup(response1, 'html.parser')
    #     x1 = soup.find(id='content')
    #     # file = codecs.open("YuNianTest11", "a+", "utf-8")
    #     file.write(link.text)
    #     file.write('\n')
    #     file.write(x1.get_text())
    #     # file.close
    #
    # elif r4.search(x):
    #     print(link.get('href'))
    #     print(link.text)
    #     url = "http://www.aixiawx.com" + link.get('href')
    #     with urllib.request.urlopen(url, timeout=30) as rep:
    #         rep.read()
    #     response1 = urllib.request.urlopen(url)
    #     soup = BeautifulSoup(response1, 'html.parser')
    #     x1 = soup.find(id='content')
    #     # file = codecs.open("YuNianTest11", "a+", "utf-8")
    #     file.write(link.text)
    #     file.write('\n')
    #     file.write(x1.get_text())
    #     # file.close

file.close
print("end")
