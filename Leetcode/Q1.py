l=[1,2,3,4,5,6]
n=3
num=l[n:len(l)]
print(l)
o=1
for i in range(len(l)//2):
    l.insert(o,num[i])
    o=o+2
print(num)
print(l)
    
    
    
    
