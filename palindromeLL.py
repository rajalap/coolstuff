from node import Node

def printLL(node):
    print(node.data)
    if node.next is not None:
        printLL(node.next)

def check4Pals(node, LL):
    LL.append(node.data)
    if node.next is not None:
        check4Pals(node.next, LL)
    print(len(LL))
    if len(LL) == 1:
        print("Linked List of size 1")
        return
    if len(LL) == 2:
        if LL[0] == LL[1]:
            print("Pal of size 2")
    for x, num in enumerate(LL):
        print("hi ", x)
        if x == len(LL)/2:
            print("Found a buddy, pal!")
            return
        if LL[x] != LL[len(LL)-1-x]:
            print("Not a pal!")
            return   

def main():
    tHead        = Node("t")
    tNode2       = Node("a")
    tHead.next   = tNode2
    tNode3       = Node("c")
    tNode2.next  = tNode3
    tNode4       = Node("o")
    tNode3.next  = tNode4
    tNode5       = Node("c")
    tNode4.next  = tNode5
    tNode6       = Node("a")
    tNode5.next  = tNode6
    tNode7       = Node("t")
    tNode6.next  = tNode7

    hHead        = Node("h")
    hNode2       = Node("a")
    hHead.next   = hNode2
    hNode3       = Node("n")
    hNode2.next  = hNode3
    hNode4       = Node("n")
    hNode3.next  = hNode4
    hNode5       = Node("a")
    hNode4.next  = hNode5
    hNode6       = Node("h")
    hNode5.next  = hNode6

    bHead        = Node("b")
    bNode2       = Node("a")
    bHead.next   = bNode2
    bNode3       = Node("d")
    bNode2.next   = bNode3

    LL = []
    printLL(tHead)
    check4Pals(tHead, LL)
    LL = []
    printLL(hHead)
    check4Pals(hHead, LL)
    LL = []
    printLL(bHead)
    check4Pals(bHead, LL)

if __name__ == "__main__":
    main()
