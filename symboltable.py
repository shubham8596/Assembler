import sys
import os
db=1
dd=4
dw=2
dq=8
tot=0
symdef='D'
add=['0']
i=0
var=''
varnm=''
lit=[]
m=0
f=open("sym.txt","w")
f2=open("lit.txt","r")
li=f2.readlines()
for k in range(3,len(li)):
	str1=li[k].split()
	if(str1!=[]):
		lit.append(str1[1])

f.write(("\nName\tSize\tTotal\tS/L\tD/U\tAddr\tLiteralEntry")+os.linesep)
if __name__=="__main__":
	fp=open(sys.argv[1],"r")
	line=fp.readlines()
        for st in range(0,len(line)):
		str1=line[st].split()
	
#****************************** data ********************************************

		if 'dd' in str1 :
			varnm=str1[0]	
			cnt=0
			if(str1[2].find(',')>0):
				tot=str1[2].split(',')			
				str2=len(tot)
				cnt=str2
				
			else:
				cnt+=1
			symbol='S'
			addr=add[i]
			i=i+1
			add.insert(i,(db*cnt+int(addr)))
			if(str(st) in lit):
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dd,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
			else:
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dd,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
			
		if line[st].find('db')>0:
			if line[st].find('\"')>0:			
				string=line[st]		
				newst=''
				left=0
				right=0
				new=len(string)
				for m in range(0,len(string)):
					if(string[m]!='\"'):
						left=left+1
					else:
						break			
				while(string[new-1]!="\""):
					new-=1				
					right+=1
				right=len(string)-right
				newst=string[left+1:right-1]
				symbol='S'
				cnt=len(newst)
				addr=add[i]
				i=i+1
				add.insert(i,(dd*cnt+int(addr)))

				if(str(st) in lit):
					f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],db,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
				else:
					f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],db,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
					
			else:
				varnm=str1[0]			
				cnt=0
				if(str1[2].find(',')>0):
					tot=str1[2].split(',')			
					str2=len(tot)
					cnt=str2
			
				else:
					cnt+=1
				symbol='S'
				addr=add[i]
				i=i+1
				add.insert(i,(db*cnt+int(addr)))
				if(str(st) in lit):
					f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],db,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
					
				else:
					f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],db,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
					

		if 'dq' in str1 :
			cnt=0
			if(str1[2].find(',')>0):
				tot=str1[2].split(',')
				str2=len(tot)
				cnt=str2
				
			else:
				cnt+=1
			symbol='S'
			addr=add[i]
			i=i+1
			add.insert(i,(dq*cnt+int(addr)))

			if(str(st) in lit):
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dq,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
			else:
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dq,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)


		if 'dw' in str1 :
			cnt=0
			if(str1[2].find(',')>0):
				tot=str1[2].split(',')
				str2=len(tot)
				cnt=str2
				
			else:
				cnt+=1
			symbol='S'
			addr=add[i]
			i=i+1
			add.insert(i,(dw*cnt+int(addr)))

			if(str(st) in lit):
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dw,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
				
			else:
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dw,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)


		if 'equ' in str1 :
			
			symbol='S'
			str2=str1[2][2:]
			addr=add[i]
			i=i+1
			add.insert(i,(dw*cnt+int(addr)))
			if(str(str2) in lit):
				f.write(("%s\t%c\t%c\t%s\t%c\t%s\tLIT%s"%(str2[0],'-','-',symbol,symdef,addr,str(str2-1)))+os.linesep)
				
			else:
				f.write(("%s\t%c\t%c\t%s\t%c\t%s\tLIT%s"%(str1[0],'-','-',symbol,symdef,addr,str(str2-1)))+os.linesep)


# ************************************************ bss ******************************************************	

		if 'resb' in str1:
			resbsize=1
			cnt=1
			symbol='S'
			addr=add[i]
			i=i+1
			add.insert(i,(resbsize*cnt+int(addr)))		
			if(str(st) in lit):
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],db,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
				
			else:
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],db,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
				
		
		if 'resd' in str1:
			resdsize=4
			cnt=1
			symbol='S'
			addr=add[i]
			i=i+1
			add.insert(i,(resdsize*cnt+int(addr)))		
			if(str(st) in lit):
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dd,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
				
			else:
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dd,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
				

		if 'resw' in str1:
			reswsize=2
			cnt=1
			symbol='S'
			addr=add[i]
			i=i+1
			add.insert(i,(reswsize*cnt+int(addr)))		
			if(str(st) in lit):
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dw,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
				
			else:
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dw,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
					

		if 'resq' in str1:
			resqsize=8
			cnt=1
			symbol='S'
			addr=add[i]
			i=i+1
			add.insert(i,(resqsize*cnt+int(addr)))		
			if(str(st) in lit):
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dq,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
				
			else:
				f.write(("%s\t%d\t%d\t%s\t%c\t%s\tLIT%s"%(str1[0],dq,cnt,symbol,symdef,addr,str(st-1)))+os.linesep)
				

#******************* LABELS ***************************
		
		if (line[st].find('jz')>0 or line[st].find('jnz')>0 or line[st].find('jmp')>0 or line[st].find('loop')>0):
			str1=line[st].split()
			nn=str1[1]+':'
			flag=0
			for e in range(0,len(line)):
				str2=line[e].split()
				if(nn==str2[0]):
					flag=1
					break					
						
			if(flag==1):
				f.write(("%s\t%c\t%c\t%s\t%c\t%s\t%c"%(str1[1],'-','-','L','D','-','-'))+os.linesep)
				
			else:
				f.write(("%s\t%c\t%c\t%s\t%c\t%s\t%c"%(str1[1],'-','-','L','U','-','-'))+os.linesep)
				
			
