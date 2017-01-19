path=r'D://loglog//'
file=open(path+'B.txt','r')
lines=file.readlines()
rptNo=set(['10006620160005','10006620160004','04006620150034','04006620150024','04006620150025','04006620150037'])
for line in lines:
	ss=line.split(',')
	#if (ss[2]=='0100059836' or ss[2]=='010206') and ss[6]=='0\n':
	rptNo.add(ss[5])
	#	print(ss[5])
file.close()
wfile=open(path+'w.txt','w')
for v in rptNo:
	wfile.write(v+'\n')
wfile.close()
