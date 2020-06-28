import helloWorld
import reverseLL
import isUnique
import palinPerm
import desPatt
import rotMat
import zeroMat
import grphCalc

# Using a dictionary instead of a case statement since the practice is more 'Python-esque'
switcher = {
    "HW"  :  helloWorld,
    "RLL" :  reverseLL,
    "IU"  :  isUnique,
    "PP"  :  palinPerm,
    "DP"  :  desPatt,
    "RM"  :  rotMat,
    "ZM"  :  zeroMat,
    "GC"  :  grphCalc
}

def restart():
    command = input("Would you like to test another function? Y/N ")
    if command.upper() == "Y":
        main()
    elif command.upper() == "N":
        exit()
    else:
        print("Invalid option")
        restart()

def main():
    print("Below are the available functions:")
    print("1: Hello World - HW")
    print("2: Reverse - RLL")
    print("3: Is Unique - IU")
    print("4: Palindrome Permutation - PP")
    print("5: Design Patterns - DP")
    print("6: Rotate Matrix - RM")
    print("7: Zeroed Matrix - ZM")
    print("8: Graphing Calculator - GC")
    userIn = input("What function would you like to test? ")

    if userIn in switcher.keys():
        mod = switcher.get(userIn)
        mod.main()
    else:
        print("Invalid Option")
        
    restart()

if __name__=="__main__":
    main()



