q=int(input("Enter the 6 digit num"))  
num=str(q)
sum1=int(num[0])**1+int(num[1])**2+int(num[2])**3+int(num[3])**4+int(num[4])**5+int(num[5])**6
print(sum1)
sum2=int(num[-1])**1+int(num[-2])**2+int(num[-3])**3+int(num[-4])**4+int(num[-5])**5+int(num[-6])**6
print(sum2-sum1)
