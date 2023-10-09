arr = [8,1,5,3,2,0,12,14,13]*100

def bubble_sort(arr):
    for j in range(0,len(arr)-1): ### THis will do as many times as values in the list. 
        for i in range(0,len(arr)-1):###This is one itineration
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

bubble_sort(arr)
print(arr)