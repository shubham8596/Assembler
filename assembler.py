import os
import sys
name=sys.argv[1]
l=sys.argv[2]
os.system('python symboltable.py %s'%(name))
os.system('python literaltable.py %s'%(name))
os.system('python intermediatecode.py %s'%(name))
os.system('python LstFile.py %s'%(name))

if(l=='-s'):
	print("############## Symbol Table ###########")
	fp=open("sym.txt","r")
	line=fp.readlines()
	for i in range(0,len(line)):
		print(line[i])

if(l=='-l'):
	print("############## Literal Table ###########")
	fp=open("lit.txt","r")
	line=fp.readlines()
	for i in range(0,len(line)):
		print(line[i])

if(l=='-i'):
	print("############## Intermediate Table ###########")
	fp=open("intermediate.txt","r")
	line=fp.readlines()
	for i in range(0,len(line)):
		print(line[i])

if(l=='-lst'):
	print("############## LST  ###########")
	fp=open("LST.txt","r")
	line=fp.readlines()
	for i in range(0,len(line)):
		print(line[i])

