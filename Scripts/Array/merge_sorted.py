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
    firstArray = array[0]
    secArray = array[1]

    first_index = second_index = 0
    flag = 0

    while (len(firstArray) - 1 >= first_index and len(secArray) - 1 > second_index):
        print(len(firstArray) - 1, first_index, second_index)
        if firstArray[first_index] > secArray[second_index]:
            merged.append(secArray[second_index])
            second_index += 1
        else:
            merged.append(firstArray[first_index])
            first_index += 1
        if first_index == len(firstArray) - 1:
            flag = 1
    
    if flag == 1:
        for item in secArray[second_index:]:
            merged.append(item)
    else:
        for item in firstArray[first_index:]:
            merged.append(item)
    return merged
print(mergeSortedArray(merge))
