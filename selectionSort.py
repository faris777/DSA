#the selection sort algorithm is big O n*n
# you have to touch every element at least onces so it is now efficient algorithm

def findSmallest(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

def selectionsort(arr):
    for i in range(len(arr)-1):
        currentMin = arr[i]
        currentMinIndex = i
        for j in range(i+1,len(arr)):
            if currentMin > arr[j]:
                currentMin  = arr[j]
                currentMinIndex = j
        if currentMinIndex != i:
            arr[currentMinIndex] = arr[i]
            arr[i] = currentMin
    return arr

#decreasing order
def selectionSortDec(lst):
    for i in range(len(lst)):
        currentindex = i
        currentValue = lst[i]
        for j in range(i+1,len(lst)):
            if currentValue < lst[j]:
                currentValue = lst[j]
                currentindex = j
        if currentindex != i:
            lst[currentindex] = lst[i]
            lst[i] = currentValue
    return lst


def srt(lst:list)->list:
    for i in range(len(lst)):
        minindex = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[minindex]:
                minindex = j
        lst[i], lst[minindex] = lst[minindex], lst[i]
    return lst

print(srt([9,5,2,4,6]))
