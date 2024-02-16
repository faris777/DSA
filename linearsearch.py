#the algorithm time complexity depend on the input data it is linear growth

def linearSearch(lst, key):
    for i in lst:
        if i == key:
            return lst.index(i)
    return -1


lst = [1, 4, 4, 2, 5, -3, 6, 2]
print(linearSearch(lst,-4))