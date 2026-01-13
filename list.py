#understanding the binary research
def bin(l,key):
    #here code beigns
    low = 0
    high = len(l)-1

    while low<=high:
        mid = (low+high)//2
        if key == l[mid]:
            return mid
        elif key < l[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

#main
n = int(input("Enter the number of elements in the list:"))
lst=[]
for element in range(n):
     lst.append(int(input("enter the element to be entered in the list")))
lst.sort()    
target = int(input("Enter the element to be found"))
y = bin(lst,target)
print("The item is at",target,"the index:",y,"and the list is:",lst)
     
    
                
