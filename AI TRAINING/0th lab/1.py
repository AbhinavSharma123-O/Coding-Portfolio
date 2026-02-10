items=[]
n=int(input("Number of items:"))
for i in range(n):
    q = input(f"Item Num {i+1} Item Name:")
    items.append(q)
print(f"{items}")
l = int(input("Do you want to remove an item?0-no,1-yes:"))
if l == 1:
    r = int(input("Enter the Item num to remove: ")) 
    items.pop(r-1)
    print(f"{items}")
else:
    print(items)
