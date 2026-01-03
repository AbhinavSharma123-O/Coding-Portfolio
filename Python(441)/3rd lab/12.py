while True:
    a=int(input("enter num"))
    b=int(input("enter num2"))
    print("1.ADD")
    print("2.SUB")
    print("3.MULTI")
    print("4.divi")
    print("5.Quit")
    ch=int(input("enter your choice"))
    if ch==1:
        print(a+b)
    elif ch==2:
        print(a-b)
    elif ch==3:
        print(a*b)
    elif ch==4:
        print(a/b)
    elif ch==5:
        break
    else:
        print("invalid choice")
