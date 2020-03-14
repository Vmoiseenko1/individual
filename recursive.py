# the recursive approach
import time

def binary_search(a, x, start , finish):
    if start > finish:
        return None
    else:
        mid = (start + finish) // 2
    if x == a[mid]:
        return mid
    if x < a[mid]:
        return binary_search(a, x, start, mid)
    else:
        return binary_search(a, x, mid, finish)

a = list(map(int, input().split()))
a.sort()
x = int(input())
start = 0
finish = len(a) - 1
startt = time.time()
print(binary_search(a, x, start, finish))
print("Time of programm's work: " + str(time.time()-startt) + ' sec.')