p = input("Enter a string: ")
q = input("Enter another string: ")

c = ''
d = min(len(p), len(q))

for i in range(d):
    c = c + str(p[i]) + str(q[i])
    
print(c)
