satFile=open("UF75.325.100/uf75-01.cnf")
instances=[]
instance=[]
lineCounter=0

while satFile.readline() !='':
     x=satFile.readline()
     if x[0] != "c" and x[0] !="p" and x[0] !="%" and x[0] !="0" :
         y=x.replace('0\n','').replace("\n","")
         c=y.split(" ")
         print(c)
    
 

   

    
