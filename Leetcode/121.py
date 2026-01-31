prices=[3,2,6,5,0,3]
i=0
BuyPrice=prices[0]
m=0
while i<len(prices)-1:
    if prices[i]>=BuyPrice:
        i=i+1
        continue
    else:
        BuyPrice=prices[i]
        m=i
        i=i+1
SellPRICE=max(prices[m:len(prices)])
print(BuyPrice)
print(SellPRICE)
print(SellPRICE-BuyPrice)
