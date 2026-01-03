for i in range(1,10):
    for j in range(1,10):
        if((i==j and j<6)or(i==5 and j>6)or(i+j==10 and i>4)):
            print("*",end="")
        else:
            print("*",end="")
    print()
