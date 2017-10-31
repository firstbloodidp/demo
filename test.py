import urllib
import re
from collections import namedtuple
import sqlconfig

MyStruct = namedtuple("HeadphonesList", "title id priceList")

lol = []
lol.append(MyStruct("casca", "1", ["link1","200","lin2","300"]))
lol.append(MyStruct("casca", "2", ["link1","200","lin2","300"]))

#print lol

for i in range(1,1):
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

        aux = json.find(start)

        if aux == -1:
        	break

        json = json[(aux+58):]
        newurl = json[0:300]
        aux1 = newurl.find(end)
        newurl = newurl[0:aux1] + '/'
        url = 'http://www.cel.ro/casti/' + newurl

        aux = json.find(start1)
        json = json[(aux+22):]
        titlu = json[0:300]
        aux1 = titlu.find(end1)
        titlu = titlu[0:aux1]

        print titlu, pret, url
        print

print
print 
print 

for i in range(1,11):
    url = 'https://www.emag.ro/casti-pc/p' + str(i) + '/c'
    print url
    json = urllib.urlopen(url).read()
    start = '<a href="https://www.emag.ro/cas'
    end = '"'
    start1 = 'class="product-title js-product-url" data-zone="title">'
    end1 = '</a>'
    start2 = '<p class="product-new-price">'
    end2 = '</sup> <span>Lei</span></p>'
    flag = 1
    for j in range(0,60): 

        aux = json.find(start)

        if aux == -1:
        	break

        json = json[(aux+9):]
        newurl = json[0:300]
        aux1 = newurl.find(end)
        newurl = newurl[0:aux1] 
        url =  newurl

        aux = json.find(start1)
        json = json[(aux+55):]
        titlu = json[0:300]
        aux1 = titlu.find(end1)
        titlu = titlu[0:aux1]

        aux = json.find(start2)
        json = json[(aux+29):]
        pret = json[0:100]
        aux1 = pret.find(end2)
        pret = pret[0:aux1].replace("<sup>",".")

        print titlu, pret, url
        print