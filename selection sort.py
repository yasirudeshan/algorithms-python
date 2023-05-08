def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if(arr[j] < arr[min]):
               min  = j

        arr[i], arr[min] = arr[min], arr[i]


arr = [2, 6, 5, 1, 3, 4]

selection_sort(arr)

print(arr)
