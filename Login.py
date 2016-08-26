import http.client
import urllib
reqheaders={
'MACHINE_CODE':'SH001',
'Host':'192.168.118.224:3000'}  
reqheaders2={
'MACHINE_CODE':'SH002',
'Host':'192.168.118.224:3000'} 
reqheaders3={
'MACHINE_CODE':'SH003',
'Host':'192.168.118.224:3000'}
reqheaders4={
'MACHINE_CODE':'SH004',
'Host':'192.168.118.224:3000'}
reqheaders5={
'MACHINE_CODE':'XH001',
'Host':'192.168.118.224:3000'}
reqheaders6={
'MACHINE_CODE':'XH002',
'Host':'192.168.118.224:3000'}
reqconn = http.client.HTTPConnection("192.168.118.224:3000")
reqconn.request("GET","/machine/login?machine_code=SH001&password=123456",None,reqheaders)

reqconn2 = http.client.HTTPConnection("192.168.118.224:3000")
reqconn2.request("GET","/machine/login?machine_code=SH002&password=123456",None,reqheaders2)

reqconn3 = http.client.HTTPConnection("192.168.118.224:3000")
reqconn3.request("GET","/machine/login?machine_code=SH003&password=123456",None,reqheaders3)

reqconn4 = http.client.HTTPConnection("192.168.118.224:3000")
reqconn4.request("GET","/machine/login?machine_code=SH004&password=123456",None,reqheaders4)

reqconn5 = http.client.HTTPConnection("192.168.118.224:3000")
reqconn5.request("GET","/machine/login?machine_code=XH001&password=123456",None,reqheaders5)

reqconn6 = http.client.HTTPConnection("192.168.118.224:3000")
reqconn6.request("GET","/machine/login?machine_code=XH002&password=123456",None,reqheaders6)

res = reqconn.getresponse()
print (res.status, res.reason)
print (res.msg)
print (res.read())

