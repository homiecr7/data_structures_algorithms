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
    
    merged = [] # initialinzing expty list
    firstArray = array[0]
    secArray = array[1]

    first_index = second_index = 0
    flag = 0 # flag to check if first array is checked

    while (len(firstArray) - 1 >= first_index and len(secArray) - 1 > second_index): # looping through each array until one them is covered
        print(len(firstArray) - 1, first_index, second_index)
        if firstArray[first_index] > secArray[second_index]:
            merged.append(secArray[second_index])
            second_index += 1
        else:
            merged.append(firstArray[first_index])
            first_index += 1
        if first_index == len(firstArray) - 1: # checking everytime if first array is itrated
            flag = 1
    
    if flag == 1: # if first is itrated then push the all the elements of the array
        for item in secArray[second_index:]:
            merged.append(item)
    else: # else push the first one
        for item in firstArray[first_index:]:
            merged.append(item)
    return merged
print(mergeSortedArray(merge))
