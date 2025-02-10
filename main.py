import requests
from bs4 import BeautifulSoup
url = "https://timesofindia.indiatimes.com/city/nagpur"

r = requests.get(url)
htmlContent = r.content
print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# markup = "<p><!-- this is a comment -->"
# soup2 = BeautifulSoup(markup)
# print(soup2.p)
# exit()

# print(type(title))
# print(type(title.string))
# print(type(soup))
title = soup.title

paras = soup.find_all('p')
# print(paras)
print(soup.find('p'))
print(soup.find('p')['class'])

# print(anchors)
# anchors = soup.find_all('a')

# for link in anchors:
#   print(link)



print(soup.find_all("p", class_="lead"))

print(soup.find('p').get_text())
print(soup.get_text())

anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link.get("href") != 'a'):
        links = "https://timesofindia.indiatimes.com/city/nagpur" + link.get('href')
        all_links.add(links)
        print(links)

# navsupportedlink = soup.find(id = "nav-content")
# for elem in navsupportedlink.contents:
#     print(elem)


