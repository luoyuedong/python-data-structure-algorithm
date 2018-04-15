class Node():
    def __init__(self,item):
        self.item = item
        self.next =None

def findfloop(head):
    slowPtr = head
    fastPtr = head
    loopExist = False
    while fastPtr.next != None and fastPtr.next.next != None:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        if slowPtr == fastPtr:
            loopExist = True
            print("存在环结构")
            break

    if loopExist == True:
        slowPtr = head
        while slowPtr!=fastPtr:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
        return slowPtr
    print("不是环结构")
    return fastPtr

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    print(findfloop(node1).item)