def question(ListValue):
    print("Question asked by user given below\n")
    for i in range(len(ListValue)):
        n=i+1
        print(n,".",ListValue[i],"?")
def main():
    length=int(input("How many question you want to add : "))
    ListValue=[]
    print('enter the question')
    for i in range(length):
        ListValue.append((input()))
    ListValue
    question(ListValue)
if __name__ =="__main__":
    main()