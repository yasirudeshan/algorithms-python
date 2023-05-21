def binarySearch(A, n):
    l = 0;
    u = len(A) -1
    

    while l <= u:
        m = (l+u) // 2
        
        if A[m] == n:
            globals() ['pos'] = m
            return True

        else:
            if n > A[m]:
                l = m + 1
            else:
                u = m - 1

    return False
        

    
A = [34,45,55,75,89,97,104,136,145,187] 
n = 55

if binarySearch(A, n):
    print("Found in position" , pos)
else:
    print("not found")


