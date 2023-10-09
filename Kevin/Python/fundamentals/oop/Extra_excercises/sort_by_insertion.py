#Sort by selection in Python
def selectionSort(array):
    size = len(array)-1
    for ind in range(0,size): 
        print(f"Original loop {ind}--------------------------")
        min_index = ind
        for j in array[0:min_index+1]: 
            print(f"This is the pointer{array[min_index+1]}")
            if array[min_index+1] < j:
                print("True")
                x= array.pop(min_index+1)
                array.insert(min_index,x)
                min_index = min_index -1
            else:
                print("False")
            print(array)


arr = [-2,45,0,11,-9,88,-97,-202,747]
selectionSort(arr)
print(arr)

######################Sort by insertion for lists with dictinoaries

def selectionSort(array):
    size = len(array)-1
    for ind in range(0,size): 
        print(f"Original loop {ind}--------------------------")
        min_index = ind
        for j in array[0:min_index+1]: 
            print(f"This is the pointer{array[min_index+1]['Attempts']}")
            if array[min_index+1]['Attempts'] < j['Attempts']:
                print("True")
                x= array.pop(min_index+1)
                array.insert(min_index,x)
                min_index = min_index -1
            else:
                print("False")
            print(array)




arr = [{'user': 'kevin T', 'Attempts': 2}, {'user': 'Kevin Arturo', 'Attempts': 1}, {'user': 'Arturo jacome', 'Attempts': 3}]
# print(arr[0]['Attempts'])

selectionSort(arr)
print(arr)