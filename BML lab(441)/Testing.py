#WAP to print ABHINAV SHARMA
#Print addition of 2 user num
#return sq root of user input number
#Swap 2 variables
#sum of digits of num
#2d array 3x3
#WAP to return list of even num from 1 to 100
#Find LCM two user input
#WAP takes score as input print Grade
#WAp to check a year leap or not
import math
import numpy as np
print("Abhinav Sharma")
q=int(input("1st number"))
p=int(input("2nd Number"))
print(p+q)
l=int(input("Num to be sq root"))
print(math.sqrt(l))
a,b=1,2
print(f"Before Swapp \n Now a =",a,"and b=",b)
a,b=b,a
print(f"After Swapp \n Now a =",a,"and b=",b)
arr=np.empty((3,3))
print(arr)
for h in range(1,101):
    if h%2==0:
        print(h)
bb=int(input("Enter 1st to lcm"))
aa=int(input("Enter 2nd to LCM"))
print(math.lcm(aa,bb))
score=int(input("ENter marks"))
if score>90:
    print('A')
elif score<90 and score>80:
    print("B")
elif score<80 and score>70:
    print('C')
else:
    print('D')
year=int(input("Enter year"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("Year is leap")
else:
    print("not Leap")
