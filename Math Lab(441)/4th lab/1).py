def solve():
    a1,b1=4,1
    a2,b2=5,-2
    c1,c2=50,30
    x=(c1*b2-c2*b1)/(a1*b2-b1*a2)
    y=(a1*c2-c1*b2)/(a1*b2-b1*a2)
    print(f"the solutions are{x}and{y}")
solve()
