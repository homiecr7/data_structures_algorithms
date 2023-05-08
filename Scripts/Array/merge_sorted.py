merge = [[0, 1 , 3, 4], [4, 9, 30, 31]]

def mergeSortedArray(array):
    addedArray = []
    for i in range(len(merge)):
        addedArray = addedArray + array[i]
    return addedArray

print(mergeSortedArray(merge))
