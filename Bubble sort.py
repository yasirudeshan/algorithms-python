def sort(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(0, i):
            temp = A[j]
            if A[j] > A[j + 1]:
                A[j] = A[j + 1]
                A[j + 1] = temp


li = []

for i in range(8):
    li.append(int(input("Enter Number: ")))

print(li)

sort(li)

print(li)




                
                
    
    
    
