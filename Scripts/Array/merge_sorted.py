merge = [[1, 3 ,5 ,7], [2, 4, 6, 8, 10, 12]]

# def mergeSortedArray(array):
#     addedArray = []
#     for i in range(len(merge)):
#         addedArray = addedArray + array[i]
#     return addedArray

# print(mergeSortedArray(merge))

def mergeSortedArray(array):
    # checking input
    if len(array[0]) == 0 and len(array[1]) == 0:
        return "wrong input"
    elif len(array[0]) == 0:
        return array[1]
    elif len(array[1]) == 0:
        return array[0]
    
    merged = []
    index1 = array[0]
    index2 = array[1]
    
    i = 0
    while(i < len(max(array[0], array[1]))):
        if index1[i] > index2[i]:
            merged.append(index2[i])
            merged.append(index1[i])
            i += 1

        else:
            merged.append(index1[i])
            merged.append(index2[i])
            i += 1
    return merged
print(mergeSortedArray(merge))
