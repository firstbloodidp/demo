import urllib
import re

for i in range(1,2):
    url = 'http://www.cel.ro/casti/0a-' + str(i)
    json = urllib.urlopen(url).read()
    find = '<h4 class="productTitle"><a href="http://www.cel.ro/casti/'
    flag = 1
    for j in range(0,40):
        aux = json.find(find)
        json = json[(aux+58):]
        newurl = json[0:100]
        final1 = '/"'
        aux1 = newurl.find(final1)
        newurl = newurl[0:aux1] + '/'
        #url = 'http://www.cel.ro/casti/casti-cu-microfon-sennheiser-pc-8-interfata-usb-pMCMwPT0n-l/'
        url = 'http://www.cel.ro/casti/' + newurl
        json1 = urllib.urlopen(url).read()    

        str2 = '<span class="productPrice" itemprop="price">'
        str3 = '<h2 itemprop="name" class="productName">'

        aux = json1.find(str2)
        pret = json1[(aux+44):(aux+60)]
        final = '</'
        aux = pret.find(final)
        pret = pret[0:aux]

        aux = json1.find(str3)
        produs = json1[(aux+40):(aux+240)]
        aux = produs.find(final)
        produs = produs[0:aux]

        print produs, pret

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