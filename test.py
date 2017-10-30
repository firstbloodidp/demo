import urllib
import re
from collections import namedtuple

MyStruct = namedtuple("HeadphonesList", "title id priceList")


lol = []
lol.append(MyStruct("casca", "1", ["link1","200","lin2","300"]))
lol.append(MyStruct("casca", "2", ["link1","200","lin2","300"]))

#print lol

for i in range(1,26):
    url = 'http://www.cel.ro/casti/0a-' + str(i)
    print url
    json = urllib.urlopen(url).read()
    start = '<h4 class="productTitle"><a href="http://www.cel.ro/casti/'
    end = '/" class="productListing-data-b product_link product_name"'
    start1 = '<span itemprop="name">'
    end1 = '</span></a>'
    start2 = '<b itemprop="price" content="'
    end2 = '">'
    flag = 1
    for j in range(0,40):

        aux = json.find(start2)
        json = json[(aux+29):]
        pret = json[0:100]
        aux1 = pret.find(end2)
        pret = pret[0:aux1] 
        print pret

        aux = json.find(start)
        json = json[(aux+58):]
        newurl = json[0:300]
        aux1 = newurl.find(end)
        newurl = newurl[0:aux1] + '/'
        url = 'http://www.cel.ro/casti/' + newurl
        print url

        aux = json.find(start1)
        json = json[(aux+22):]
        titlu = json[0:300]
        aux1 = titlu.find(end1)
        titlu = titlu[0:aux1]
        print titlu

        print

print
print 
print 

#for i in range(1,10):
#    url = 'https://www.emag.ro/casti-pc/p' + str(i) + '/c'
#    print url
#    json = urllib.urlopen(url).read()
#    find = '<a href="https://www.emag.ro/cas'
#    flag = 1
#    for j in range(0,80):
#        aux = json.find(find)
#        json = json[(aux+32):]
#        newurl = json[0:300]
#        final1 = '" rel='
#        aux1 = newurl.find(final1)
#        newurl = newurl[0:aux1]
        #url = 'http://www.cel.ro/casti/casti-cu-microfon-sennheiser-pc-8-interfata-usb-pMCMwPT0n-l/'
#        url = 'https://www.emag.ro/cas' + newurl
#        print url
#        json1 = urllib.urlopen(url).read()    

#        str2 = '<span class="productPrice" itemprop="price">'
#        str3 = '<h2 itemprop="name" class="productName">'

#        aux = json1.find(str2)
#        if aux == -1:
#            break
#        pret = json1[(aux+44):(aux+60)]
#        final = '</'
#        aux = pret.find(final)
#        pret = pret[0:aux]

#        aux = json1.find(str3)
#        produs = json1[(aux+40):(aux+340)]
#        aux = produs.find(final)
#        produs = produs[0:aux]

#        print produs, pret

#url = 'http://www.cel.ro/casti/casti-cu-microfon-sennheiser-pc-8-interfata-usb-pMCMwPT0n-l/'
#json = urllib.urlopen(url).read()    

#str2 = '<span class="productPrice" itemprop="price">'
#str3 = '<h2 itemprop="name" class="productName">'

#aux = json.find(str2)
#pret = json[(aux+44):(aux+60)]
#final = '</'
#aux = pret.find(final)
#pret = pret[0:aux]

#aux = json.find(str3)
#produs = json[(aux+40):(aux+240)]
#aux = produs.find(final)
#produs = produs[0:aux]

#print produs, pret