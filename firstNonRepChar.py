def firstNonRep(str):
    list = [] 
    for char in str:
        if char.upper() in list:
            print(char)
            return
        list.append(char.upper())
    print('No Repeats here!')

def main(str):
    firstNonRep(str)
    #print("First Non Repeating Character")
    #str1 = "ThisIsTheEnd"
    #str2 = "OneTwoOne"
    #str3 = "NoReps"
    #print(str1)
    #firstNonRep(str1)
    #print(str2)
    #firstNonRep(str2)
    #print(str3)
    #firstNonRep(str3)

if __name__ == "__main__":
    main()