#sorted algorithom
def is_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            sorted = False
    
    return sorted


#Monkey sort
import time
import random

def monkey_sort(arr):

    while not is_sorted(arr):
        time.sleep(0.1)
        random.shuffle(arr)
        print(arr)

    print(arr)

#example
a=[12,24,11,56,34,20]
monkey_sort(a)