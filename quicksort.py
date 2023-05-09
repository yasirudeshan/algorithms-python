def quickSort(A, left, right):
    if left < right:
        part = partition(A, left, right)
        quickSort(A, left, part - 1)
        quickSort(A, part + 1, right)

def partition(A, left, right):
    i = left
    j = right - 1
    pivot = A[right]

    while i < j:
        while i < right and A[i] < pivot:
            i += 1
        while j > left and A[j] > pivot:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    if A[i] > pivot:
        A[i], A[right] = A[right], A[i]

    return i
            


A = [12,45,34,76,89,43,56]
quickSort(A, 0, len(A) - 1)
print(A)
