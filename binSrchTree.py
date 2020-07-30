class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

class Tree:
    def __init__ (self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    
    #TODO fill out print function
    #def __repr__(self):


def split_list(list):
    half = len(list)
    return list[:half], list[half:]

def bst(arr, myBST):
    if len(arr) == 1:
        myBST.insert(arr)
    else:
        myBST.insert(arr[len(arr)/2])
        arr.remove(arr[len(arr)/2])
        arrLeft, arrRight = split_list(arr)
        if arrLeft is not None:
             bst(arrLeft, myBST)
        if arrRight is not None:
             bst(arrRight, myBST)

def main():
    print("Binary Search Tree")
    array = [1,2,3,4,5,6,7,8,9,10]
    myBST = Tree()
    bst = (array, myBST)

if __name__ == "__main__":
    main()