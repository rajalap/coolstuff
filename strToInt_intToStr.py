import stringToInt
#import intToString

def main():
    strIn1 = "-12345"
    strIn2 = "12345"
    print(strIn1)
    print(strIn2)
    intOut1 = stringToInt.strToInt(strIn1)
    intOut2 = stringToInt.strToInt(strIn2)
    print(intOut1)
    print(intOut2)
#    strOut1 = intToString.intToStr(intOut1)
#    strOut2 = intToString.intToStr(intOut2)
#    print(strOut1)
#    print(strOut2)


if __name__ == "__main__":
    main()