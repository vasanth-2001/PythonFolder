import os
def Createfile(Filename):
    if(os.path.exists(Filename)):
        print("File already exists")
    else:
        file=open(Filename,"w")
def main():
    print("enter the file you want to create")
    file_name=input()
    Createfile(file_name)
if __name__ =='__main__':
    main()