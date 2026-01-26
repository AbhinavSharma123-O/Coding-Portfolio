def Linearsearch(List):
    for i in range (0,len(List)):
        if List[i]==d:
             return(f"Linear search:",d,"Found at",i+1,"position")
def Binarysearch(List):
    for i in range(0,len(List)):
        maxi=List[i]
        for j in range (0,len(List)):
            if List[j]>maxi:
                maxi=List[j]
        
        empty.append(maxi)
        
    mid=len(empty)//2
    while d!=empty[mid]:
        if d not in List:
            return("Not Found")
            break
        if d>empty[mid]:
            mid=(mid+len(empty))/2
        else:
            mid=(0+mid)/2
        return(f"binary search:",d,"Found")
           
        
        
        

empty=[]   
List=[1,3,6,7,9]
d=7
p=Linearsearch(List)
q=Binarysearch(List)
print(List)
print(p)
print(q)

