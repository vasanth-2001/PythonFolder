import os
import multiprocessing
import time
from threading import Thread

def Square(num):
    print('Square pid:',os.getpid())
    print('Square of the Number:',num**2)

def Cube(num):
    print('Cube Pid:',os.getpid())
    print('Cube of the Number:',num**3)

def main():
    #creating Processess
    t1=Thread(target=Square,args=[5])
    # t1.run()
    t2=Thread(target=Cube,args=(3,))
    # t2.run()
    
    #starting process p1
    t1.start()
    #starting process p1
    t2.start()
    # print('Process t1',t1.pid)
    # print('Process t2',t2.pid)
    #wait untill p1 is finished
    t1.join()
    t2.join()
if __name__ =="__main__":
    start_time=time.process_time()
    print('main Pid:',os.getpid())
    main()
    end_time=time.process_time()
    print('Execution time :' ,end_time-start_time)

