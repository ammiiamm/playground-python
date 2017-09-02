import urllib.request
S3TTR4D3NEWS = "https://twitter.com/S3TTR4D3NEWS"
page = urllib.request.urlopen(S3TTR4D3NEWS)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "lxml")

all_links = soup.find_all('a')
for links in all_links:
    print (links.get('href'))
