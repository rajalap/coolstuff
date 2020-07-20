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

    def testCycle(self):
        cycleList = []
        found = False
        printval = self.head
        while printval is not None:
            print(printval.data)
            cycleList.append(printval.data)
            printval = printval.next
        for i, datum in cycleList:
            for j, cycleList.__len__ - i:
                if cycleList[i] == cycleList[j]:
                    print("Found the cycle: ", datum)
                    found = True
        if found == False:
            print("No cycle found")
                    
    
def main(llSource=["Mon","Tue","Wed"]):
    print("Make LL")
    list = SLinkedList()
    for i, datum in enumerate(llSource):
        list.AtEnd(llSource[i])
    list.printList()

if __name__=="__main__":
    main()    

