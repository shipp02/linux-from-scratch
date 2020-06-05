from tarfile import TarFile
import tarfile

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
    # resp = req.get('http://download.savannah.gnu.org/releases/sysvinit/sysvinit-2.96.tar.xz')
    # tarfile.is_tarfile(resp.content)

    regex = re.compile(r"\S*\.tar\.\S*")
    url_file = file('urls.txt', mode='w')
    for a in hrefs:
        # print(a['href'])
        if regex.match(a['href']):
            # resp = req.get(a['href'])
            print(a['href'])
            url_file.write('{} \n'.format(a['href']))
            # tarfile.is_tarfile(resp.content)

    url_file.close()