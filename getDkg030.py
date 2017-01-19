import os

path=r'd://loglog//'
files=os.listdir(path)
for file in files:
	data = open(path+file, 'r')
	bak=open(path+file+"_bak_bak.txt",'w')
	lines=data.readlines()
	for line in lines:
		if 'com.cathay.dj.a2.module.DJA2_0110_mod.003' in line:
			bak.write(line)
	bak.close()
	data.close()
