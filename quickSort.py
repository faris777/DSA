#divide and conquer algorithms approach for approach
#the o(nlogn)

def quicksort(arr):

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [ i for i in arr[1:] if i <= pivot]
        greator = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greator)


lst = [1, 4, 4, 2, 5, -3, 6, 2]
print(quicksort(lst))