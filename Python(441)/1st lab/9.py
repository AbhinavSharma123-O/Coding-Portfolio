x = int(input("Enter value of x"))
y = int(input("Enter value of y"))
n = int(input("Enter vLUE OF N"))

Num1 = x ** 2 + x ** 3
Num2 = (y/4) + (y/3) + (y ** 8)

First_Term = (Num1/Num2)**(2*n)
Num3 = (y ** 6) + (y ** 2)
Num4 = x**9

Sec_Term = Num3/Num4
Answer = First_Term * Sec_Term

print(Answer)
