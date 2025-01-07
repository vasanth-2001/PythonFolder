import os
import multiprocessing
import time

def Square(num):
    print('Square pid:',os.getpid())
    print('Square of the Number:',num**2)

def Cube(num):
    print('Cube Pid:',os.getpid())
    print('Cube of the Number:',num**3)

def main():
    #creating Processess
    p1=multiprocessing.Process(target=Square,args=(5,))
    p2=multiprocessing.Process(target=Cube,args=(5,))
    
    #starting process p1
    p1.start()
    #starting process p1
    p2.start()
    print('Process p1',p1.pid)
    print('Process p2',p2.pid)
    #wait untill p1 is finished
    p1.join()
    p2.join()
if __name__ =="__main__":
    start_time=time.process_time()
    print('main Pid:',os.getpid())
    main()
    end_time=time.process_time()
    print('Execution time :' ,end_time-start_time)

