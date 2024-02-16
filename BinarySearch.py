#binary search
#it takes input as sorted list
#it will return the position of the element other wise it will return null
#binary will take log n base 2


def binarySearch(lst,key):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = high+low
        guess = lst[mid]
        if guess == key:
            return mid
        elif guess > key:
            high -=1
        elif guess < key:
            low +=1
    return -1
array = [1, 3, 5, 7, 9]

print(binarySearch(array,5))
