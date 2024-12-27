from functools import reduce
# def CheckNumber(num):
#     if(num>=70 and num<=90):
#         return True
#     return False
# def IncrementNumber(num):
#     return num+10

# def Addition(num1,num2):
#     return num1+num2

def main():
    number=[78,90,45,34,88,98] #sequence/iterable
    filter_result=tuple(filter(lambda num : num>=70 and num<=90,number))
    print ("filter() :",filter_result)
    map_result=tuple(map(lambda num : num+10,filter_result))
    print ("map() :",map_result)
    reduce_result=reduce(lambda num1,num2 :num1+num2,map_result)
    print ("reduce() :",reduce_result)

if __name__ == '__main__':
    main()