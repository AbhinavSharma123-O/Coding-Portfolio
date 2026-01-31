strs=['flower','flight','flow']
s=''
for i in range (len(strs)-2):
            if strs[i][:2]==strs[i+1][:2]==strs[i+2][:2]:
                s=s+strs[i][:2]
print(s)
        
