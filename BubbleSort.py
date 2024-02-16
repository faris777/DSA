def bubblesort(array):
    size = len(array) #the size of the input array
    flag = True
    while flag:
        flag = False
        for j in range(size-1): #decreasing the size of the array in order reduce the time complexity but it is insigifance
            if array[j] > array[j+1]:
                array[j+1],array[j] = array[j] ,array[j+1]
                flag = True
        size-=1
    return array


array = [1,5,4,2,3]
print(bubblesort(array))
