from bs4 import BeautifulSoup
import urllib.request as urllib2
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
url = "https://www.lance.com.br/tabela#2022/Brasileirao/Serie-A/tabela"
response = opener.open(url)
html = response.read()
soup = BeautifulSoup(html)
table = soup.find(table)
print(table)