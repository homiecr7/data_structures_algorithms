def bubbleSort(arr):
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            else:
                continue
    return arr

print(bubbleSort([100, 53, 22, 89, 47, 73, 66, 91, 30, 10, 80]))