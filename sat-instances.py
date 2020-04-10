
instances=[]
instance=[]
sizeOfInstances=100
filePath=1
i=0
for i in range(sizeOfInstances) :
    
    satFile=open("UF75.325.100/uf75-0"+str(filePath)+".cnf")
    lineCounter=0
    fileEndingBool=True
    while fileEndingBool:
     
         x=satFile.readline() 
     
         if x[0] == "%":
             fileEndingBool=False
         if x[0] != "c" and x[0] !="p" and x[0] !="%" and x[0] !="0" :
             y=x.replace('0\n','').replace("\n","")
             c=y.split(" ")
             if c[0] == '' :
                 c.pop(0)
             c.pop(3)
             instance.append(list(map(int,c)))
             lineCounter+=1
    filePath+=1         
     
 
print(lineCounter)
print(instance)  

    
