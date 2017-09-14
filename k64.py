import os
import os.path
import time
def getFile(path):
        files=os.listdir(path)
        for file in files:
            filename=file
            file=path+'\\'+file
            if os.path.isfile(file):
                attrs=os.stat(file)
                filesize = os.path.getsize(file)//1024
                if 'jsp' in file and filesize>64:
                    file_list.append(filename+'  '+str(filesize)+'K')
            else:
                getFile(file)
print('正在查找大于64K的jsp文件...')
file_list=[]
path=r'D://0100060928_view10//workspace//CXLCS//Web Content//html'
getFile(path)
#文件名取当前的年月日时分秒
s_now=time.strftime('%Y%m%d%H%M%S')
file=open('E://logs//'+s_now+'.txt','w+')
if len(file_list)==0:
    file.write('empty set')
else:
    i=0
    for filename in file_list:
        print(filename)
        file.write(filename)
file.close()
print('end')

  
