def insertionSort(A):
    for i in range(1, len(A)):
        j = i
        while A[j-1] > A[j] and j > 0:
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1





A = [2,7,4,1,3,8,5,9,6]
insertionSort(A)
print(A)
