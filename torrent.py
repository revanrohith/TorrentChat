import requests
from html.parser import HTMLParser
prev = []
def getdata(term):
    r = requests.get("https://thepiratebay.zone/search/{}/1/99/0".format(term))
    a = ('class', 'detLink')
    b = ('title', 'Download this torrent using magnet')
    messagel=[]
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if a in attrs:
                #print(attrs[2][1][12:])
                messagel.append(attrs[2][1][12:])
            if b in attrs:
                #print(attrs[0][1])
                messagel.append(attrs[0][1])

        def handle_data(self, data):
            if 'Uploaded ' in data:
                messagel.append(data)
                #print(data)
    parser = MyHTMLParser()
    parser.feed(r.text)
    for i in range(len(messagel)//3):
        l = 3 * i
        print(i)
        messagel[l-1],messagel[l-2]=messagel[l-2],messagel[l-1]

    return messagel