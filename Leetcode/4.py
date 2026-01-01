num1=[1,3]
num2=[2]
for i in num2:
    num1.append(i)
num1.sort()
if len(num1)%2!=0:
    q=(len(num1)+1)/2
    print(num1[q])
else:
    q=(((len(num1)+1)/2)+((len(num1)/2)))/2
    print(num1[q])
    
    
