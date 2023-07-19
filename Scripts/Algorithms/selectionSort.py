def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selectionSort([100, 53, 22, 89, 47, 73, 66, 91, 30, 10, 80]))


        