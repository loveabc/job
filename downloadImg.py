#path是包含二十万数字的文件
import urllib.request
path=r'd://xxx.txt';
imgFile=open(path,'r')
lines=imgFile.readlines()#所有的数字
for line in lines:
	imgPath=''#根据数字组装成图片的地址,类似 http://www.baidu.com/images/美女.jpg
	response=urllib.request.urlopen(imgPath)
    if response.getcode()!=200:
       #状态码不是200,下载失败,直接下载下一张
       continue
    con=response.read()#从网络拿到图片文件流
    response.close()
    imgFileName=''#图片文件名,文件的保存路径,类似D://美女图片//美女.jpg
    saveImage=open(imgFileName,'w')
    saveImage.write(con)
    saveImage.close()
imgFile.close()
