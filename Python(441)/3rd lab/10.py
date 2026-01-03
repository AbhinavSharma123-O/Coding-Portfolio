m1=int(input("Enret sub 1"))
m2=int(input("enter sub 2"))
m3=int(input("enter sub 3"))
avg=(m1+m2+m3)/3
if m1>35 and m2>35 and m3>35:
    if avg>=75:
        print("grade o")
    elif avg>=60:
        print("grade a")
    else:
        print("just passed")
else:
    print("failed")
month=int(input("Enter month number"))
if 1<=month<=12:
    if month==2:
        print("28/29 days")
    elif month==4 or month==6 or month==9 or month==11:
        print("30 days")

    else:
        print("31 days")
else:
    print("worng month number")
    
    
