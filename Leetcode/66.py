digits=[9,0,9]
digits=digits[::-1]
i=0
while True:
    if i<len(digits):
        if digits[i]==9:
            digits[i]=0
        else:
            digits[i]=digits[i]+1
            break
    else:
        digits.append(1)
        break
    i=i+1

print(digits[::-1])
    

        
