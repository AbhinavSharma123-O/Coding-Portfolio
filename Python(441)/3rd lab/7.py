bill=int(input("bill amount"))
if bill>=5000:
    discount=0.2*bill
    bill=bill-discount
print("BIll is of",bill)
age=int(input("enter your age"))
if age>=18:
    print("you can vote")
else:
    print("you can't vote")
num=int(input("enter your num"))
if num%2==0:
    print("even")
else:
    print("not even")

side=int(input("Enter no of side"))
if side==3:
    print("triangle")
elif side==5:
    print("Pentagon")
elif side==4:
    print("rectangle/square")
else:
    print("IDK :D")

integer=int(input("ENter kar ree"))
if integer>0:
    if integer%2==0:
        print("even")
    else:
        print("odd")
else:
    print("Positive value dal re")
