n=int(input("enter"))
if n>=10 and n<=99:
    print("2 digit num")
elif n>=0 and n<=9:
    print("1 digit number")
elif n>=100 and n<=999:
    print("3 digit number")
else:
    print("other digit number")
    
