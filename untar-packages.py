import tarfile as tar

def get_name(url):
    for i in range(0, len(url), 1):
        if line[len(url) - i - 1] == '/':
            return url[len(url)-i:len(url)]



url_file = open('urls.txt', mode='r')
lines = url_file.readlines()
lines = [x.strip() for x in lines]
url_file.close()



if __name__=='__main__':
    for line in lines:
        name = get_name(line)
        print(name)
        tfile = tar.open(name, mode='r:*')
        tfile.extractall()
        tfile.close()
