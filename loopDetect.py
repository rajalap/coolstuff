import makeLL
from makeLL import SLinkedList

def main():
    print("Loop Detection")
    makeLL.main()
    list = SLinkedList()
    for i, datum in enumerate(llSource):
        list.AtEnd(llSource[i])
    list.printList()
    list.testCycle()

if __name__ == "__main__":
    main()