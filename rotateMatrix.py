def print2D(array):
    for i in array:
        for j in i:
            print(j, end=" ")
        print()

def rotateArray(array):
    newArray = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    n = array.sizeof()
    for i, row in array:
        for j, column in i:
            newArray[n - j][i] = array[i][j]
    return newArray

def main():
    array = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    print2D(array)
    array = rotateArray(array)
    print2D(array)

if __name__ == "__main__":
    main()
