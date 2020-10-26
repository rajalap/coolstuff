intDict = {"0":0, "1":1, "2":2, "3":3, "4":4,
           "5":5, "6":6, "7":7, "8":8, "9":9}

def strToInt(str):
    int = 0
    neg = False
    for i in str:
        if i == "-":
            neg = True
            continue
        int = 10* int + intDict[i]
        print(int)
    if neg:
        int = int * -1
        print(int)
    return int