def print2D(array):
    for i in array:
        for j in i:
            print(j, end=" ")
        print()

def zeroArray(array):
    newArray = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    for i, row in array:
        for j, elem in i:
            # Found a zero, 0 the column and row
            if array[i][j] == 0:
                for k, elem in j:
                    newArray[k][j] = 0
                for l, elem in i:
                    newArray[i][l] = 0
            # Have already marked the location as zero from a previous chain, do nothing
            elif newArray[i][j] == 0:
                pass
            # Default case, array doesn't have a zero and newArray at that location is still unset
            else:
                newArray[i][j] = array[i][j]
    return newArray

def main():
    array = [[0, 1, 1], [1, 1, 1], [1, 1,0]]
    print2D(array)
    array = zeroArray(array)
    print2D(array)

if __name__ == "__main__":
    main()

