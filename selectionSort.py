#selection sort
def selection_sort(arr):
    for i in range(len(arr)-1):
        # print(i+1,"pass",end=" ")
        min=i
        #print("current min is ",arr[min])
        for j in range(i+1,len(arr)):
            # print("current item under observasion ",arr[j])
            if arr[j]<arr[min]:
                # print("current item is less then min")
                min = j
                # print("min is now has become ",arr[min])
        
        arr[i],arr[min] = arr[min],arr[i]
        # print(arr)
        # print("*"*50)
    print(arr)

#example
arr=[1,2,3,2,3,14,12,30]
selection_sort(arr)