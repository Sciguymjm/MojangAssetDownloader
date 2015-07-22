import urllib2, os, time
from xml.dom.minidom import parseString

BASE_URL = 'http://assets.minecraft.net/'
def download():
    basexml = urllib2.urlopen(BASE_URL)
    xml = basexml.read()
    dom = parseString(xml)
    files = dom.getElementsByTagName('Contents')
    if not os.path.isdir('mojang/'):
        os.mkdir('mojang/')
    for file in files:
        if file.getElementsByTagName('Size')[0].firstChild.nodeValue != '0':
            d = file.getElementsByTagName('Key')[0].firstChild.nodeValue
            url = BASE_URL + d
            try:
                
                path = "mojang/"+d
                if not os.path.isdir(os.path.dirname(path)):
                    data = os.path.dirname(path)
                    os.makedirs(data)
                if not os.path.isfile(path):
                    with open(path, "wb") as local_file:
                        print 'Downloading %s' % url
                        f = urllib2.urlopen(url)
                        local_file.write(f.read())
                        time.sleep(1)
            except Exception as e:
                print 'Error:' + e.message
            except:
                pass
            

if __name__ == '__main__':
    download()