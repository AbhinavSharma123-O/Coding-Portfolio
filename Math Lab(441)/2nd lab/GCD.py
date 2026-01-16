def GCD2(a,b):
    a,b=abs(a),abs(b)
    while b!=0:
        a,b=b,a%b
    return a 
def GCD3(a,b,c):
    a,b,c=abs(a),abs(b),abs(c)
    l=GCD2(a,b)
    r=GCD2(c,l)
    return r
x=int(input("Enter the 1st num"))
y=int(input("Enter the 2nd num"))
z=int(input("Enter the 3rd num"))
print(GCD3(x,y,z))


