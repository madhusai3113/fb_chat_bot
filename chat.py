import re
import urllib2 as ulib

#search for a string using google
def searchgoogle(text):
    #repalcing the spaces with "+"
    text = text.replace(" ","+")
    #proxy = ulib.ProxyHandler({'https': "https://10.3.100.207:8080"})
    #opener = ulib.build_opener(proxy)
    #ulib.install_opener(opener)
    req = ulib.Request('https://google.com/search?q='+text, headers={'User-Agent' : "Mozilla/5.0","Accept-Language": "en-US,en;q=0.5"})
    #opening the url
    dumpdata=ulib.urlopen(req)
    #finding urls
    data = re.findall('href=\"/url\?q=(.*?)\"',dumpdata.read())
    retdata = []
    #storing urls
    for url in data:
        url=ulib.unquote(url).decode('utf-8')
        url = url.split("&")
        retdata.append(url[0])
    return retdata
#seaching for a string in a url
def searchforstring(url):
    #proxy = ulib.ProxyHandler({'http': "http://10.3.100.207:8080",'https': "https://10.3.100.207:8080"})
    #opener = ulib.build_opener(proxy)
    #ulib.install_opener(opener)
    req = ulib.Request(url, headers={'User-Agent' : "Mozilla/5.0","Accept-Language": "en-US,en;q=0.5"})
    dumpdata=ulib.urlopen(req)
    return dumpdata.read()




def meaning(q):
    url = searchgoogle(q)
    cont = re.findall('>(.*?)<',searchforstring(url[0]))
    for i in cont:
        if(len(i)>40):
            return i
            break

def location(q):
    return "https://www.google.co.in/maps/place/"+q

def weather_report(text):
    text = text.replace(" ","+")
    req = ulib.Request('https://google.com/search?q='+text, headers={'User-Agent' : "Mozilla/5.0","Accept-Language": "en-US,en;q=0.5"})
    dumpdata=ulib.urlopen(req)
    l=dumpdata.read()
    cont = re.findall('<b>(.*?)</b>',l)
    cont1 = re.findall('<span class="wob_t" style="display:inline">(.*?)</span>',l)
    cont1[0]= cont1[0].replace('\xc2\xb0', ' ')
    cont2 = re.findall('<td style="white-space:nowrap;padding-right:15px;color:#666">(.*?)</td>',l)
    cont3 = re.findall('<td style="white-space:nowrap;padding-right:15px;color:#666">.*?<span class="wob_t" style="display:inline">(.*?)</span></td>',l)
    cont4 = re.findall('<td style="white-space:nowrap;padding-right:0px;vertical-align:top;color:#666">(.*?)</td>',l)
    k=cont[1],cont1[0],cont2[0],"wind: " + cont3[0],","+cont4[0]
    return k
try:
    print weather_report("what is weather today bot")
except:
    print "could not process :( please check again"