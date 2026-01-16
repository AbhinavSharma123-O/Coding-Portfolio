def gcd(a, b):
    a,b=abs(a), abs(b)
    while b!= 0:
        a,b=b,a%b
    return a
s=[]
a = int(input("Enter the a"))
b = int(input("Enter the b"))
m=int(input("enter m"))
def congurence(a,b,m):
    d=gcd(a,m)
    if b%d!=0:
        print("NO solution")
    else:
        for i in range(m):
            if ((a*i)-b)%m==0:
                s.append(i)
    print(s)
congurence(a,b,m)
                 
               
    

