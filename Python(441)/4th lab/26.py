for i in range(1,10):
    for j in range(1,10):
        if((i+j==6 and i<5)or(i+j==6 and j>4)or(i-j==4 and i>4)or(i-j==4 and j>4)):
            print("*",end="")
        else:
            print("*",end="")
    print()
