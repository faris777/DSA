def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Compare elements from both halves and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append the remaining elements from both halves (if any)
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    right = arr[:mid]
    left = arr[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left,right)



arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = mergesort(arr)
print("Sorted array:", sorted_arr)