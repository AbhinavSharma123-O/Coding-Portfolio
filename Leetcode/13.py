s = "MCMXCIV"
sum = 0
i = 0
n = len(s)
while i < n:
    if i < n - 1 and s[i] == "I" and s[i+1] == "V":
        sum = sum + 4
        i = i + 2
    elif i < n - 1 and s[i] == "I" and s[i+1] == "X":
        sum = sum + 9
        i = i + 2
    elif i < n - 1 and s[i] == "X" and s[i+1] == "L":
        sum = sum + 40
        i = i + 2
    elif i < n - 1 and s[i] == "X" and s[i+1] == "C":
        sum = sum + 90
        i = i + 2
    elif i < n - 1 and s[i] == "C" and s[i+1] == "D":
        sum = sum + 400
        i = i + 2
    elif i < n - 1 and s[i] == "C" and s[i+1] == "M":
        sum = sum + 900
        i = i + 2
    elif s[i] == "I":
        sum = sum + 1
        i = i + 1
    elif s[i] == "V":
        sum = sum + 5
        i = i + 1
    elif s[i] == "X":
        sum = sum + 10
        i = i + 1
    elif s[i] == "L":
        sum = sum + 50
        i = i + 1
    elif s[i] == "C":
        sum = sum + 100
        i = i + 1
    elif s[i] == "D":
        sum = sum + 500
        i = i + 1
    elif s[i] == "M":
        sum = sum + 1000
        i = i + 1

print(sum)
