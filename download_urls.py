import urllib
import urllib2
import getpass
from twill.commands import *

un = getpass.getuser
pw = getpass.getpass

go('http://www.example.com/login.php')

fv("1", "username", un)
fv("1", "password", pw)

submit('0')

def extract(raw_string, start_marker, end_marker):
    start = raw_string.index(start_marker) + len(start_marker)
    end = raw_string.index(end_marker, start)
    return raw_string[start:end]


filehandle = urllib.urlopen('www.example.com/tutorials')
fo = open("source.txt","a+")

for lines in filehandle.readlines():
    if(lines.startswith('identifier1',20)): #you need to specify the string segment in the source code with which you can access the specific lines that has the url(s) to the file(s) that you need to download
        fo.write(extract(lines, "identifier2", "identifier3")) #the url will lie between the specific strings identifier2 and identifier3
        fo.write("\n");

fo.close()
#Dowload code with status bar:
with open("source.txt") as f:
    for line in f:
        line = line.strip()
        url = line
        file_name = url.split('/')[-1]
        u = urllib2.urlopen(url)
        fd = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
    
            file_size_dl += len(buffer)
            fd.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status

        fd.close()

f.close()

filehandle.close()
