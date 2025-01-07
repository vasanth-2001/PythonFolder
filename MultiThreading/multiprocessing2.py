import os
import multiprocessing
import time

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
    p1=multiprocessing.Process(target=DisplayNumber)
    p2=multiprocessing.Process(target=DisplayReverse)
    
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

