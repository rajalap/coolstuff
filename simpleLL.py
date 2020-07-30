from node import Node

def printList(head):
    if head.data is not None:
        print(head.data)
    if head.next is not None:
        printList(head.next)

def deleteFromList(head, num):
    ogHead = head
    for i in range(num-1):
        head = head.next
    #If I don't free memory here it'll probably blow up eventually
    head.next = head.next.next
    return ogHead

# Default value of list below
# def checkDupes(found=[], head):
def checkDupes(found, count, ogHead, head):
# Should be a hash map here but I forgot how =/
    #if head.data is in found:
    for datum in found:
        if head.data == datum:
            print("Found the dupe, you dope! It's: ", head.data)
            ogHead = deleteFromList(ogHead, count)
            count = count-1
    if head.next is None:
        print("End of the line bub!")
        printList(ogHead)
        return ogHead
    found.append(head.data)
    checkDupes(found, count+1, ogHead, head.next)

def main(usersList):
    print("Simple LL")
    if usersList is None:
        head = Node("Mon")
        Node2 = Node("Tues")
        Node3 = Node("Wed")
        Node4 = Node("Mon")
        Node5 = Node("Tues")
        Node6 = Node("Thurs")
        Node7 = Node("Thurs")
        head.next = Node2
        Node2.next = Node3
        Node3.next = Node4
        Node4.next = Node5
        Node5.next = Node6
        Node6.next = Node7        
    printList(head)
    found = []
    head = checkDupes(found, 0, head, head)
    #printList(head)

if __name__ == "__main__":
    main(usersList=None)