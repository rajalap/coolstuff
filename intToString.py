strDict = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4",
           5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}

def intToStr(int):
    string = atoi(int)
    if (string[0] == "-"):
        
    int = int >> string(int).len()-1
    print(int)
    return string

def main():
    intIn1 = -12345
    intIn2 = 12345
#    print(intIn1)
#    print(intIn2)
    strOut1 = intToStr(intIn1)
    strOut2 = intToStr(intIn2)
#    print(strOut1)
#    print(strOut2)

if __name__ == "__main__":
    main()