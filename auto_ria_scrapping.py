from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

html = urlopen('https://auto.ria.com/legkovie/state/kiev/?page=1')
bsObj = BeautifulSoup(html, "html.parser")

auto_list = bsObj.find_all('span', {'class': 'blue bold'})


for auto in auto_list:
    print(auto.get_text())


