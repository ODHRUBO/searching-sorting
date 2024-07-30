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

#example
arr1=[1,2,6]
arr2 = [3,5,7,9,10]
print(merge_sorted(arr1,arr2))
