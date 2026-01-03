for i in range(1,10):
    for j in range (1,10):
        if i==9 or i==1 or j==9 or j==1:
            print("*",end="")
        else:
            print("",end='')
    print("")
