import os
import sys
from dictionary import *
count=0
i=0
flag=0
literal=[]
symbol=[]
sym=[]
fptr=open("intermediate.txt","w")
name=sys.argv[1]
if(os.system('python symboltable.py %s'%(name))==0 and os.system('python literaltable.py %s'%(name))==0):
	f=open(name,"r")
	line=f.readlines()
	while((line[i].find('ain:')<0)):
		count=count+1
		i=i+1
	for i in range(0,count):
		fptr.write((line[i])+os.linesep)
	f1=open('lit.txt','r')
	line1=f1.readlines()
	for j in range(2,len(line1)):
		str1=line1[j].split()
		literal.append(str1[2])
	
	f2=open('sym.txt','r')
	line2=f2.readlines()
	for j in range(1,len(line2)):
		str2=line2[j].split()
		symbol.append(str2[0])
	f3=open(name,'r')
	line3=f3.readlines()
	for j in range(count,len(line3)):
		flag=0
		string=line3[j]
		str3=line3[j].split()
		if(line3[j].find('dword')>0):
			str4=str3[1].split('[')
			str5=str4[1][0]
			str9=str4[1][:-1]
			if(str9 in reg32):
				k=reg32.index(str9)
				line3[j]=line3[j].replace(str(str9),regval1[k])

			if(str9 in reg16):
				k=reg16.index(str9)
				line3[j]=line3[j].replace(str(str9),regval2[k])

			if(str9 in reg8):
				k=reg8.index(str9)
				line3[j]=line3[j].replace(str(str9),regval3[k])


			if(str5 in symbol):
				k=symbol.index(str5)
				line3[j]=line3[j].replace(str5,'SYM#'+str(k))
		if(len(str3)>=1):
			if(line3[j].find(':')>0):
				str6=str3[0]
				lth=len(str6)-1
				str6=str6[0:lth]
				if(str6 in symbol):
					k=symbol.index(str6)
					line3[j]=line3[j].replace(str6,'SYM#'+str(k))
		if(len(str3)==2):
			if(line3[j].find(',')>0):
				str4=str3[1].split(',')
				str3=str4
				if(str3[1] in symbol):
					k=symbol.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'SYM#'+str(k))
					
				elif(str3[1] in literal):
					k=literal.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'LIT#'+str(k))
			else:
				if(str3[1] in symbol):
					k=symbol.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'SYM#'+str(k))
				elif(str3[1] in literal):
					k=literal.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'LIT#'+str(k))
			
		if(len(str3)==3):
			if(line3[j].find(',')>0):
				str4=str3[2].split(',')
				str3=str4
				if(str3[1] in symbol):
					k=symbol.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'SYM#'+str(k))
					
				elif(str3[1] in literal):
					k=literal.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'LIT#'+str(k))
					
			else:
				if(str3[1] in symbol):
					k=symbol.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'SYM#'+str(k))
				
				elif(str3[1] in literal):
					k=literal.index(str3[1])
					line3[j]=line3[j].replace(str3[1],'LIT#'+str(k))
				if(str3[0] in symbol):
					k=symbol.index(str3[0])
					line3[j]=line3[j].replace(str3[0],'SYM#'+str(k))
				
				elif(str3[0] in literal):
					k=literal.index(str3[0])
					line3[j]=line3[j].replace(str3[0],'LIT#'+str(k))
				if(str3[2] in symbol):
					k=symbol.index(str3[2])
					line3[j]=line3[j].replace(str3[2],'SYM#'+str(k))
				
				elif(str3[2] in literal):
					k=literal.index(str3[2])
					line3[j]=line3[j].replace(str3[2],'LIT#'+str(k))
			if(str4[0] in reg32 or str4[1] in reg32) or (str4[0] in reg16 or str4[1] in reg16) or (str4[0] in reg8 or str4[1] in reg8) :
				if(str4[0] in reg32):
					k=reg32.index(str4[0])
					line3[j]=line3[j].replace(str(str4[0]),str(regval1[k]))
				if(str4[1] in reg32):
					k=reg32.index(str4[1])
					line3[j]=line3[j].replace(str(str4[1]),str(regval1[k]))
				if(str3[0] in reg16):
					k=reg16.index(str3[0])
					line3[j]=line3[j].replace(str(str3[0]),str(regval2[k]))
				if(str3[1] in reg16):
					k=reg16.index(str3[1])
					line3[j]=line3[j].replace(str(str3[1]),str(regval2[k]))
				if(str3[0] in reg8):
					k=reg8.index(str3[0])
					line3[j]=line3[j].replace(str(str3[0]),str(regval3[k]))
				if(str3[1] in reg8):
					k=reg8.index(str3[1])
					line3[j]=line3[j].replace(str(str3[1]),str(regval3[k]))


		str3=line3[j].split()
		if(line[j].find(',')>0):
				str4=str3[1].split(',')
				if(len(str4)>1):
					if(str4[0] in reg32):
						k=reg32.index(str4[0])
						line3[j]=line3[j].replace(str(str4[0]),str(regval1[k]))
					if(str4[1] in reg32):
						k=reg32.index(str4[1])
						line3[j]=line3[j].replace(str(str4[1]),str(regval1[k]))
					if(str4[0] in reg16):
						k=reg16.index(str4[0])
						line3[j]=line3[j].replace(str(str4[0]),str(regval2[k]))
					if(str4[1] in reg16):
						k=reg16.index(str4[1])
						line3[j]=line3[j].replace(str(str4[1]),str(regval2[k]))
					if(str4[0] in reg8):
						k=reg8.index(str4[0])
						line3[j]=line3[j].replace(str(str4[0]),str(regval3[k]))
					if(str4[1] in reg8):
						k=reg8.index(str4[1])
						line3[j]=line3[j].replace(str(str4[1]),str(regval3[k]))
		else:
			if(len(str3)==2):
				if(str3[1] in reg32):
					k=reg32.index(str3[1])
					line3[j]=line3[j].replace(str(str3[1]),str(regval1[k]))
				if(str3[1] in reg16):
					k=reg16.index(str3[1])
					line3[j]=line3[j].replace(str(str3[1]),str(regval2[k]))
				if(str3[1] in reg8):
					k=reg32.index(str3[1])
					line3[j]=line3[j].replace(str(str3[1]),str(regval3[k]))
			
		
		fptr.write("%s"%(line3[j])+os.linesep)

