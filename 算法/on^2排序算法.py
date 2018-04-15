from random import randint
import timeit

def bubble_sort(alist):
    n = len(alist)
    for i in range(n-1):
        exchang = False
        for j in range(0,n-1-i):
            if(alist[j]>alist[j+1]):
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                exchang = True
        if not exchang:
            break
    return alist


def selectionSort(alist):
    for i in range(len(alist)):
        minposition=i
        for j in range(i,len(alist)):
            if alist[minposition]>alist[j]:
                minposition=j
        alist[i], alist[minposition] = alist[minposition], alist[i]
    return alist

def insertionSort(alist):
    for i in range(1,len(alist)):
        currenvalue = alist[i]
        position = i
        while alist[position-1]>currenvalue and position>0:
            alist[position] = alist[position-1]
            position = position-1
        alist[position] = currenvalue
    return alist

if __name__=='__main__':
    max = 5000
    list = [randint(-max, max) for x in range(max)]
    # 使用切片可以真正将一份list复制给其他变量，如果不用切片，即alist=list，只是指针而已。
    alist = list[:]
    blist = list[:]
    clist = list[:]
    dlist = list[:]
    t1=timeit.Timer('bubble_sort(alist)','from __main__ import bubble_sort,alist')
    print('短路冒泡排序: %s s' %t1.timeit(number=1))

    t2 = timeit.Timer('selectionSort(blist)', 'from __main__ import selectionSort,blist')
    print('选择排序: %s s' % t2.timeit(number=1))

    t3 = timeit.Timer('insertionSort(clist)', 'from __main__ import insertionSort,clist')
    print('插入排序: %s s' % t3.timeit(number=1))
