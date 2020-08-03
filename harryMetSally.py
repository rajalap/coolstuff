from node import Node

def printLL(node):
    print(node.data)
    if node.next is not None:
        printLL(node.next)

def conjunctionJunction(head1, head2):
    

def main():
    hHead = Node("t")
    hNode2 = Node("a")
    hHead.next = hNode2
    hNode3 = Node("c")
    hNode2.next = hNode3
    hNode4 = Node("o")
    hNode3.next = hNode4
    hNode5 = Node("c")
    hNode4.next = hNode5
    hNode6 = Node("a")
    hNode5.next = hNode6
    hNode7 = Node("t")
    hNode6.next = hNode7

    mHead = Node("m")
    mNode2 = Node("e")
    hHead.next = mNode2
    mNode3 = Node("o")
    mNode2.next = mNode3
    mNode4 = Node("w")
    mNode3.next = mNode4
    mNode5 = Node("c")
    mNode4.next = mNode5
    mNode6 = Node("a")
    mNode5.next = mNode6
    mNode7 = Node("t")
    mNode6.next = mNode7

    printLL(hHead)



if __name__ == "__main__":
    main()