for i in range(1,10):
    for j in range(1,10):
        if((i==j and j<6)or (i+j==10 and i<6)or(j==5 and i>4)):
            print("*",end="")
        else:
            print("*",end="")
    print()
