from node import Node

class SLinkedList:
    def __init__(self):
        self.head = None

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next=NewNode
    
    def printList(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

def main(llSource=["Mon","Tue","Wed"]):
    print("Make LL")
    list = SLinkedList()
    for i, datum in enumerate(llSource):
        list.AtEnd(llSource[i])
    list.printList()

if __name__=="__main__":
    main()    

