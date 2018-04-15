from random import randint
import timeit


def mergeSort(seq):
    if len(seq) <= 1:
        return seq
    mid = int(len(seq) / 2)
    left = mergeSort(seq[:mid])
    right = mergeSort(seq[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

max=100000
list=[randint(-max,max) for x in range(max)]
alist=list[:]
blist=list[:]
t1=timeit.Timer('mergeSort(alist)','from __main__ import mergeSort,alist')
print('归并排序: %s s' % t1.timeit(number=1))