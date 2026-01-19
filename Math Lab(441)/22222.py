def gauss(a1, b1, c1, d1,
          a2, b2, c2, d2,
          a3, b3, c3, d3,):    
    x, y, z = 0 , 0, 0  
    for i in range(n):
        x = (d1 - b1*y - c1*z)/a1
        y = (d2 - a2*x - c2*z)/ b2
        z = (d3 - a3*x - b3*y)/c3
    return x, y, z
n=3
print(gauss(8,-3,2,20,4,11,-1,33,6,3,12,36))
