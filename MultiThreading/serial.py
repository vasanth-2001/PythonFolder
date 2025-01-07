import os

def Square(num):
    print('Square pid:',os.getpid())
    print('Square of the Number:',num**2)

def Cube(num):
    print('Cube Pid:',os.getpid())
    print('Cube of the Number:',num**3)

def main():
    Square(5)
    Cube(5)

if __name__ =="__main__":
    print('main Pid:',os.getpid())
    main()
