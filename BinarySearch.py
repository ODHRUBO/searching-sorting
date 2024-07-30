#binary search
#sorted array

def binary_search(arr,low,high,item):
    # print("low = ",low,"high = ",high,end=' ')
    if low <= high:
        mid = (low+high)//2
        # print("mid value is ",arr[mid])
        if arr[mid]==item:
            return mid
        elif arr[mid]>item:
            return binary_search(arr,low,mid-1,item)
        else:
            return binary_search(arr,mid+1,high,item)
        
    else:
        return -1
    
#example
arr=[11,14,20,24,30,40,50,70,73,90,99,100]
print(binary_search(arr,0,len(arr)-1,100))