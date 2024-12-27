# the argument that are given after the name of the program in the command line shell of the operating system.
from sys import *
def Addition(value1,value2):
    Ans=value1+value2
    return Ans

def main():
    print('Application Name : ',argv[0])  #cmd.py
    # print('First Argument : ',argv[1])
    # print('First Second : ',argv[2])
    if(len(argv)==2):
        if(argv[1]=='--U'):
            print('Pass Arguments: Application_name First Argument Second Argument')
            exit()

        if(argv[1]=='--H'):
            print('Help: Application use to add two numbers')
            exit()
    if(len(argv)!=3):
        print('Invalid number of arguments')
        print('Please use --U flag to get usage')
        print('Please use --H flag for help')
        exit()
    result=Addition(int(argv[1]),int(argv[2]))
    print('Addition',result)

if __name__ == '__main__':
    main()