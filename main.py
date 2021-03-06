import helloWorld
import reverseLL
#import isUnique
import palinPerm
import desPatt
import rotMat
import zeroMat
import grphCalc
#import binSrchTree
import loopDetect
import simpleLL
# Attempting to import external configuration files for functions (Can I put together a make or cmake list?)
# Include mass importer/.includes:
# Maybe make a tasks .json file?

# Using a dictionary instead of a case statement since the practice is more 'Python-esque'
switcher = {
    "HW"  :  helloWorld,
    "RLL" :  reverseLL,
    "IU"  :  isUnique,
    "PP"  :  palinPerm,
    "DP"  :  desPatt,
    "RM"  :  rotMat,
    "ZM"  :  zeroMat,
    "GC"  :  grphCalc,
    #"BST" :  binSrchTree,
    "LD"  :  loopDetect,
    "SLL" :  simpleLL
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
    print("1  : Hello World - HW")
    print("2  : Reverse - RLL")
    print("3  : Is Unique - IU")
    print("4  : Palindrome Permutation - PP")
    print("5  : Design Patterns - DP")
    print("6  : Rotate Matrix - RM")
    print("7  : Zeroed Matrix - ZM")
    print("8  : Graphing Calculator - GC")
    print("9  : Binary Search Tree - BST")
    print("10 : Loop Detection - LD")
    print("11 : Simple Linked List - SLL")
#   print("11 : Simple Linked List - SLL <Optional python list with args>")
    userIn = input("What function would you like to test? ")

    if userIn in switcher.keys():
        mod = switcher.get(userIn)
        #mod with optional arguments
        mod.main()
        # mod.main(<passed in arguments if there>)
    else:
        print("Invalid Option")
        
    restart()

if __name__=="__main__":
    main()



