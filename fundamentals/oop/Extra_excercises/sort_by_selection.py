# Selection sort in Python
def selectionSort(array):
    size = len(array)
    for ind in range(size): #####Original loop that provides the value that will be compare
        print(f"Original loop {ind}")
        min_index = ind
        for j in range(ind + 1, size): ############second loop starting from 1
            # select the minimum element in every iteration
            print(f"Comparing if {array[j]} is  less than {array[min_index]} ")
            if array[j] < array[min_index]: 
                min_index = j ##This will basically set the index with the minnimum value.
                print(f"Doing something {min_index}")
            else:
                print("Not doing shit")
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
        print(array)

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]

selectionSort(arr)
print(arr)