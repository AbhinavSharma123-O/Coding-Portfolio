num=[2,7,11,15]
target=26
output=[]
k=0
p=1
while True:
    if p==len(num):
        p=0
        k=k+1
    elif p==k:
        p=p+1
    else:
        if num[p]+num[k]==target:
            break
        else:
            p=p+1
print(output)

    
