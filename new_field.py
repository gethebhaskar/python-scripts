import os
import sys
import pandas as pd
from pandas.io.parsers import ParserError

arr = os.listdir()#arr reads 2 file from the current folder,current folder should only have input files and code
arr.remove('new_field.py')

#assign arr[0] and arr[1]
ar1=arr[0]#if you want enter custompath for file1 here instead of arr[0]
ar2=arr[1]#if you want enter custompath for file2 here instead of arr[1]

if ar1.endswith('.xlsx') or ar1.endswith('.xls'):
    df1=pd.read_excel(ar1)
elif ar1.endswith('.txt'):
	try:
		df1=pd.read_csv(ar1,sep="|")	#change delimeter here
	except ParserError:
    		df1=pd.read_csv(ar1,sep="|",nrows=5) #change delimeter here
else:
    df1=pd.read_csv(ar1)
    
if ar2.endswith('.xlsx') or ar2.endswith('.xls'):
   df2=pd.read_excel(ar2)
elif ar2.endswith('.txt'):
    try :
    	df2=pd.read_csv(ar2,sep="|")  #change delimeter here
    except ParserError	:
    	df2=pd.read_csv(ar2,sep="|",nrows=5) #change delimeter here
else:
    df2=pd.read_csv(ar2)

c1=df1.columns
c2=df2.columns
e1=[]
e2=[]

for i in c1 :
    if i not in c2:
        e1.append(i)
      
for i in c2 :
    if i not in c1:
        e2.append(i)
        
if len(e1)!=0:
	df1=df1[[k for k in e1]]
	df1['file name']=ar1
    
if len(e2)!=0:
	df2=df2[[k for k in e2]]
	df2['file name']=ar2
     
f=open("out.txt","w")
for k in e1:
	f.write(k+",")
f.write("--"+ar1+"\n")
for k in e2:
	f.write(k+",")
f.write("--"+ar2)
f.close()

writer=pd.ExcelWriter('out.xlsx',engine='xlsxwriter') 
if len(e1)!=0:
	df1.to_excel(writer,sheet_name='sheet1')
if len(e2)!=0:
	df2.to_excel(writer,sheet_name='sheet2')
writer.save()	
	
    



