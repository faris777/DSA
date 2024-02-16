#recursion fucntion which means a function call it self there is two case the base case and recursion case
#the base case when the function doesn't call it self
#the recursive case when the function does it call him self
#note the alternative way of loop


def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)

def fact(n):
    if n == 0: #base case
       return 1
    else:
       return n * fact(n-1) #recurcive case


def sum(arr):
    flag = len(arr)
    add = 0
    if flag == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])

def countNumber(lst):
    if not lst:
        return 0
    else:
        lst.pop()
        return 1+countNumber(lst)

def maximumNumber(lst):
    if not lst:
        return 0
    else:
        max = lst[0]
        rest_max = maximumNumber(lst[1:])
        return max if max > rest_max else rest_max

print(maximumNumber([1,2,9,4,5]))