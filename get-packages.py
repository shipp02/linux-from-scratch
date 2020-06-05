import bs4 as bs
import requests as req
import re

if __name__ == '__main__':
    page = req.get('http://www.linuxfromscratch.org/lfs/view/stable/chapter03/packages.html')
    soup = bs.BeautifulSoup(page.content, 'html.parser')
    tag = soup.dl
    print(tag.name)
    print(tag['class'])
    hrefs = soup.find_all('a', {'class': 'ulink'})
    # print(hrefs)

    regex = re.compile('\S*.tar.\S*')
    for a in hrefs:
        # print(a['href'])
        if regex.match(a['href']):
            print(a['href'])
