import os
import multiprocessing
import time
import threading

def DisplayNumber():
    print('Display Number from 1 to 50')
    for i in range(1,51,1):
        print(i,end=" ")
def DisplayReverse():
    print('\nDisplay Number from 50 to 1')
    for i in range(50,0,-1):
        print(i,end=" ")
def main():
    #creating Processess
    t1=threading.Thread(target=DisplayNumber)
    t2=threading.Thread(target=DisplayReverse)
    
    #starting process p1
    t1.start()
    print('T1',threading.get_native_id())
    #starting process p1
    t2.start()
    print('T2',threading.get_native_id())
    # print('Process p1',p1.pid)
    # print('Process p2',p2.pid)
    #wait untill p1 is finished
    t1.join()
    t2.join()
if __name__ =="__main__":
    start_time=time.process_time()
    print('main Pid:',os.getpid())
    main()
    end_time=time.process_time()
    print('Execution time :' ,end_time-start_time)

