
instances=[]
instance=[]
sizeOfInstances=100


     
def returnInstances():
    
    global instance
    global instances
    for i in range(sizeOfInstances) :
    
        satFile=open("UF75.325.100/uf75-0"+str(i+1)+".cnf")
        lineCounter=0
        fileEndingBool=True
        while fileEndingBool:
     
             x=satFile.readline() 
     
             if x[0] == "%":
                 fileEndingBool=False
             if x[0] != "c" and x[0] !="p" and x[0] !="%" and x[0] !="0" :
                 y=x.replace('0\n','').replace("\n","")
                 clause=y.split(" ")
                 if clause[0] == '' :
                     clause.pop(0)
                 clause.pop(3)
                 instance.append(list(map(int,clause)))
                 lineCounter+=1
        
        instances.append(instance)
        instance=[]         
    return instances

    
