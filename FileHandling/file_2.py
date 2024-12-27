import os 
def Readfile(Filename):
    if(os.path.exists(Filename)):
        file=open(Filename,"r")
        Data=file.read()
        Createfile(Data)
        file.close()
    else:
        print('File does exist')
def Createfile(Data):
    fd=open('demo.txt','w')
    fd.write(Data)
    print('Content copy successfully')
    fd.close()

def main():
    print("enter the file ")
    filname=input()
    Readfile(filname)
if __name__ =='__main__':
    main()