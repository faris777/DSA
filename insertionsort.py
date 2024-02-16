#the algorithm is o(n**2) the best case is o(n)

def insertionsort(arr):
    for i in range(1,len(arr)-1):
        for j in range(0,i):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr