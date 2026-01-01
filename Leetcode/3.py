"""Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3."""
s='abcabcabcbb'
a=''
q=0
x=''
p=0
for i in s:
    if i not in x:
        x=x+i
        q=q+1
        if q>p:
            p=q
    else:
        x=''
        q=0
        
print(p)
        
    
    
