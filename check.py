# coding=utf-8
from grab import Grab
g = Grab()

f = open('proxylist.txt')
av = open('goodproxy.txt', 'w')

num_lines = sum(1 for line in f)
print ('Proxies in file: ' + str(num_lines))
f.close()

with open('proxylist.txt') as f:
    mylist = [line.rstrip('\n') for line in f]

cycle = 0
while cycle < num_lines:
	s = mylist[cycle]
	try:
		g.setup(proxy=s)
		g.go('http://google.com')
		print 
		av.write(s+'\n')
		print (s +' - ok ['+str(cycle)+'|'+str(num_lines)+'] '+g.doc.select('//title').text().encode('utf-8'))
	except Exception as inst:
		print (s +' - '+ str(inst) +' ['+str(cycle)+'|'+str(num_lines)+']')
	cycle += 1
print ('Done')
