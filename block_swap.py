def leftRotate(arr, d, n):
    if(d == 0 or d == n):
        return
    i = d
    j = n - d
    while(i != j):
        if(i < j):
            swap(arr, d-i, d+i-j, i)
            j -= 1
        else:
            swap(arr, d-i, d, j)
            i =- j
    swap(arr, d-i, d,i)
    
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
d = 0
leftRotate(arr, d, n)
print(leftRotate, arr)