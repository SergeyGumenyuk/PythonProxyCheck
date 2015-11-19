# -*- coding utf-8 -*-
from grab import Grab

g = Grab()
f = open('proxylist.txt', 'w')

g.go('https://best-proxy.com/russian/index.php')
for elem in g.doc.select('//div[@class="table-wrap"]/div/ul/li[@class="proxy"]/text()'):
	f.write(elem.text()+'\n')
print ('1')

i = 2
while i < 11:
	print (i)
	g.go('https://best-proxy.com/russian/index.php?p='+str(i))
	for elem in g.doc.select('//div[@class="table-wrap"]/div/ul/li[@class="proxy"]/text()'):
		f.write(elem.text()+'\n')
	i+=1
f.close()
print('Done!')
