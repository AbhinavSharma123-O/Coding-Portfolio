def abc(x):
    if(x==0):
        return 0
    else:
        return x+abc(x-1)
res= abc(10000)
print(res)
        
    
    
