def mergeSort(array):
    if (len(array) == 1):
        return array
    # split the array
    length = len(array)
    left = array[:length // 2]
    right = array[length // 2:]

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    print(left, right)
    array = []
    leftIndex = 0
    rightIndex = 0
    while (leftIndex < len(left) and rightIndex < len(right)):
        if left[leftIndex] < right[rightIndex]:
            array.append(left[leftIndex])
            leftIndex += 1
        else:
            array.append(right[rightIndex])
            rightIndex += 1
    return array + left[leftIndex:] + right[rightIndex:]

print(mergeSort([2, 5, 8, 10, 11, 3, 1, 4]))

