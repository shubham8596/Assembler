import sys
import os
arr=[]
f=open("lit.txt","w")

f.write(("\nSr No\tLine No\t\tValues \t\t\tHex Value")+os.linesep)
if __name__=="__main__":
	fp=open(sys.argv[1],"r")
	line=fp.readlines()
	j=0
        for st in range(0,len(line)):
		str1=line[st].split()
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
				ele=''
				for k in range(0,len(newst)):		
					ele=ele+str(hex(ord(newst[k])))
					hexvalue=ele.replace("0x","").upper()
				
				f.write("%d\t%d\t\t%s\t\t\t%s"%(j,st,newst,hexvalue)+os.linesep)
				j+=1
			
			else:
				str2=line[st].split()	
				if(len(str2[2])>1):			
					str3=str2[2].split(',')
					ele=''
					for k in range(0,len(str3)):		
						ele=ele+str(hex(int(str3[k])))
					ele=ele.replace("0x","").upper()
					f.write("%d\t%d\t\t%s\t\t\t%s"%(j,st,str3,ele)+os.linesep)
					j+=1
				
		
		if (line[st].find(' dd ')>0 or line[st].find(' dq ')>0 or line[st].find(' dw ')>0 or line[st].find(' resb ')>0 or line[st].find(' resd ')>0 or line[st].find(' resw ')>0 or line[st].find(' resq ')>0):
			str2=line[st].split()		
			if(len(str2[2])>1):			
				str3=str2[2].split(',')
				ele=''
				for k in range(0,len(str3)):
					ele=ele+str(hex(int(str3[k])))
				ele=ele.replace("0x","").upper()
				f.write("%d\t%d\t\t%s\t\t\t%s"%(j,st,str3,ele)+os.linesep)
				j+=1
			else:
				f.write("%d\t%d\t\t%s\t\t\t%x"%(j,st,str2[2],int(str2[2]))+os.linesep)
				j+=1



		str2=line[st].split()
		if(len(str2)>1):
			str3=str2[1].split(',')
			if len(str3)==2:
				nn=str3[1][0]
				if(ord(nn)>=48 and ord(nn)<=58):
					p=int(str3[1])
					z=str(hex(p))
					hexvalue=z.replace("0x","").upper()
					f.write("%d\t%d\t\t%s\t\t\t%s"%(j,st,str3[1],hexvalue)+os.linesep)
					j+=1
