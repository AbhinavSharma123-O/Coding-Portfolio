l=[[]]
INPUT=[[1,1],[2,5],[3,3]]
k=0
zz=INPUT[k]
xx=zz[0]
yy=zz[1]
for i in range (1,10):
    for j in range (1,10):
            l.append([i,j])
            if i==xx and j==yy:
                print("Found")
                k=k+1
            zz=INPUT[k]
            xx=zz[0]
            yy=zz[1]    
