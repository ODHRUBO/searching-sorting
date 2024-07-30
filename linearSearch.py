#linear search
#brute force

def linear_search(arr,item):
    for i in range(len(arr)):
        if arr[i]==item:
            return i
    
    return -1   #value not found

arr=[12,34,54,23,1,100,20,97]
print(linear_search(arr,101))
