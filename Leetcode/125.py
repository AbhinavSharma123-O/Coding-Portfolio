s="New1  qweN"
ls=True
q=""

for i in range(len(s)):
            if s[i].isalpha():
                q=q+s[i]
            else:
                continue
print(q)


p=q
if p[::-1]==q:
    print("Pallidrom")
