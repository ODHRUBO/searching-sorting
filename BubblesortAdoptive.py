#Bubble sort
#adoptive

def bubble_sort(arr):
    for i in range (len(arr)-1):
        flag=0
        for j in range (len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]#sorting
                flag = 1
        if flag == 0:
            break 
           
    print(arr)

#Example
arr=[1,2,3,4,53,4,7,12,97,4]
bubble_sort(arr)