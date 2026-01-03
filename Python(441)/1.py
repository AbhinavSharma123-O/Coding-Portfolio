for  i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()
print("\n")
for  i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()
print("\n")
for  i in range(1,6):
    for j in range(i,0,-1):
        print(j,end='')
    print()
print("\n")
for  i in range(1,6):
    for j in range(i,6):
        print(j,end='')
    print()
print("\n")
for  i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end='')
    print()
print("\n")
for  i in range(5,0,-1):
    for j in range(i,6):
        print(j,end='')
    print()
print("\n")
for  i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end='')
    print()
print("\n")
for  i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
        
    print()
print("\n")
for  i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end='')
    print()
print("\n")
for  i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(i,end='')
    print()
print("\n")


for  i in range(1,8):
    for j in range(1,i+1):
        if(j==1 or i==7 or i==j):
            print("*",end="")
        else:
            print("",end="")
    print()
print('\n')
for  i in range(1,8):
    for j in range(1,i+1):
        if(j==7 or i==1 or i+j==8):
            print("*",end="")
        else:
            print("",end="")
    print()
print()
print('\n')
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
print("\n")
for i in range (5,0,-1):
    for k in range (1,6-i):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print("\n")
for i in range(5,0,-1):
    for k in range(1,i):
        print("",end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
print("\n")
for i in range(1,6):
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(i,6):
        print(j,end=" ")
    print()
print("\n")
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
print("\n")
for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
print("\n")

