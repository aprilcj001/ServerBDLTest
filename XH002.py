#coding=gbk
import re
import http.client
import urllib

reqheaders={
'MACHINE_CODE':'XH002',
'Host':'192.168.118.224:3000'} 

try:
	f=open('E:/Works/八达岭/python/tickets607/6_tickets607_/2_6_tickets607.txt','r') 

	n = 48286
	b = n
	while n > 0:
		strT = f.readline()
		T = re.split(r'\|',strT)
		Ticketcode = T[2]+'10000' 

	#	if T[4] == '150':	
		reqconn = http.client.HTTPConnection("192.168.118.224:3000")
		reqconn.request("GET","/ticket/leave?iccard="+Ticketcode,None,reqheaders)
		res = reqconn.getresponse()

		print (res.status, res.reason)
#		print (res.msg)
		print (res.read())	
		print (Ticketcode)
		print (b-n+1)
		print ("\n")	
		n = n-1

except Exception as e:
	print ('Error:',e)

finally:		
	reqconn.close()
	f.close()