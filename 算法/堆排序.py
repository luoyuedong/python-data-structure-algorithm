import random

def Heap_build(heap, root ,HeapSize):
    left = 2*root + 1
    if(left<HeapSize):
        flag = left
        right = left+1
        if(right<HeapSize):
            if(heap[right]>heap[left]):
                flag = right
        if(heap[flag]>heap[root]):
            heap[flag],heap[root] = heap[root],heap[flag]
            Heap_build(heap,flag,HeapSize)

def Heap_sort(heap):
    HeapSize = len(heap)
    for i in range(HeapSize//2,-1,-1):
        Heap_build(heap,i,HeapSize)
    for i in range(HeapSize-1,-1,-1):
        heap[0], heap[i] = heap[i], heap[0]
        Heap_build(heap,0,i)
    return heap

if __name__ == '__main__':
    a = [30,50,57,77,62,78,94,80,84]
    print(a)
    Heap_sort(a)
    print(a)
    b = [random.randint(1,1000) for i in range(1000)]
    print(b)
    Heap_sort(b)
    print(b)

