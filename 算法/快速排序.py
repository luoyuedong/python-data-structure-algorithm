from random import randint
import timeit


def quickSort(alist):
    quick_sort_standord(alist,0,len(alist)-1)
    return alist


def quick_sort_standord(arr,low,high):
    if low < high:
        key = partion(arr,low,high)
        quick_sort_standord(arr,low,key)
        quick_sort_standord(arr,key+1,high)

def partion(arr,low,high):
    key = arr[low]
    while low<high:
        while low<high and arr[high]>=key:
            high -= 1

        if low<high:
            arr[low] = arr[high]

        while low<high and arr[low]<key:
            low += 1

        if low<high:
            arr[high] = arr[low]

    arr[low] = key
    return low

if __name__ == '__main__':
    max = 100000
    list = [randint(-max, max) for x in range(max)]
    alist = list[:]
    blist = list[:]
    t2 = timeit.Timer('quickSort(blist)', 'from __main__ import quickSort,blist')
    print('快速排序: %s s' % t2.timeit(number=1))