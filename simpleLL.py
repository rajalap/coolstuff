from node import Node

def printList(head):
    print(head.data)
    if head.next is not None:
        printList(head.next)

# Default value of list below
# def checkDupes(found=[], head):
def checkDupes(found, head):
# Should be a hash map here but I forgot how =/
    #if head.data is in found:
    for datum in found:
        if head.data == datum:
            print("Found the dupe, you dope! It's: ", head.data)
            return
    if head.next is None:
        print("Not being duped here!")
        return
    print("Before append ",found)
    found.append(head.data)
    print("After append ",found)
    checkDupes(found, head.next)

def main(usersList):
    print("Simple LL")
    if usersList is None:
        head = Node("Mon")
        Node2 = Node("Tues")
        Node3 = Node("Wed")
        Node4 = Node("Mon")
        head.next = Node2
        Node2.next = Node3
        Node3.next = Node4
    printList(head)
    found = []
    checkDupes(found, head)

if __name__ == "__main__":
    main(usersList=None)