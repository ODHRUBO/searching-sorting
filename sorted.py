#is array sorted?
def is_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            sorted = False
    
    return sorted

#example
arr =[1,2,3,4,5,6]
print(is_sorted(arr))