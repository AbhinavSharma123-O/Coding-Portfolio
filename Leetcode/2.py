l1=[2,4,3]
l2=[5,6,4]
i=-1
l3=[]
carry=0
while i>-4:
    q=l1[i]+l2[i]
    if q>=10:
        carry=carry+(q//10)
        q=q%(10*carry)
        l3.append(q)
        i=i-1
        
    else:
        l3.append(q+carry)
        i=i-1
print(l3)


    
    
    

    
    
    
