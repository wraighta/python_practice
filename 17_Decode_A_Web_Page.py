#17 Decode a Web Page

import requests
from bs4 import BeautifulSoup


r = requests.get('http://www.nytimes.com')
r_html = r.text


soup = BeautifulSoup(r_html, "html.parser")
print(soup.title)

#title = soup.find('span', 'articletitle').string

#print soup.title

print(soup.find('body'))


