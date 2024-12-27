from functools import reduce
def CheckNumber(num):
    if(num>=70 and num<=90):
        return True
    return False
def IncrementNumber(num):
    return num+10

def Addition(num1,num2):
    return num1+num2

def main():
    number=[78,90,45,34,88,98] #sequence/iterable
    filter_result=tuple(filter(CheckNumber,number))
    print ("filter() :",filter_result)
    map_result=tuple(map(IncrementNumber,filter_result))
    print ("map() :",map_result)
    reduce_result=reduce(Addition,map_result)
    print ("reduce() :",reduce_result)

if __name__ == '__main__':
    main()