from bs4 import BeautifulSoup
import urllib.request
#所有的业务
businesses=["CXLAA","CXLAB","CXLAC","CXLAD","CXLAE","CXLAF","CXLAG","CXLAH","CXLAJ","CXLAK","CXLAL","CXLAR","CXLAT","CXLBC","CXLDA","DBDJ" 
,"DBDK" ,"CXLEM","CXLFA","CXLFB","CXLFM","CXLCM","CXLKA","CXLZX","CXLZY","CXLZZ"]
f=open(r'D:\tables\CXLAZ.txt','a')
url="http://IP:PORT/html/CM/TableIndex.jsp?Schema="
total=0
for business in businesses:
  final_url=url+business
  response=urllib.request.urlopen(final_url)
  if response.getcode()!=200:
    print(response.getcode())
    break
  html=response.read().decode("gbk")
  response.close()
  soup=BeautifulSoup(html,"html.parser")
  thTAG=soup.find("th")
  allAs=soup.findAll("a")
  i=0
  for a in allAs:
    i=i+1
    f.write(thTAG.text)
    f.write(".")
    f.write(a.text)
    f.write('\n')
  total=total+i
  print(thTAG.text)
  print(i)
print(total)
f.close()

