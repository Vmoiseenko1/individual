# the iterative approach

import time

def binary_search(a, x):
    length = len(a)
    mid_element = length // 2
    the_lowest = 0
    the_highest = len(a) - 1
    while a[mid_element] != x and the_lowest <= the_highest:
        if x > a[mid_element]:
            the_lowest += mid_element
        else:
            the_highest -= mid_element
        mid_element = (the_lowest + the_highest) // 2
    if the_lowest > the_highest:
        return None
    else:
        return mid_element

a = list(map(int, input().split()))
a.sort()
x = int(input())
start = time.time()
print(binary_search(a, x))
print("Time of programm's work: " + str(time.time()-start) + ' sec.')