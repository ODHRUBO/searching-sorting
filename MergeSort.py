#merge_sorted function for merge 2 array

def merge_sorted(arr1,arr2):
    i=j=0
    merged = []
    while i<len(arr1) and j <len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1

    while i < len(arr1):
        merged.append(arr1[i])
        i+=1

    while j < len(arr2):
        merged.append(arr2[j])
        j+=1
    return merged


#Merge sort//
#Merge sort//
#Merge sort//

def merge_sort(arr):
    if len(arr)==1:
        return arr
    
    mid=len(arr)//2
    left = arr[ : mid]
    right = arr[mid : ]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge_sorted(left,right)


#example
arr =[1,2,3,6,9,5,3,2,4,1]
print(merge_sort(arr))
