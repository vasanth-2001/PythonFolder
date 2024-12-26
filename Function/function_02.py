#postition/keyword/Default
def Full_Name(FirstName,LastName,NAtionality='Indian'):
    return f'Name : {FirstName} {LastName} Nationality : {NAtionality}'

def main():
    Result = Full_Name('Vasanth','Rajendran')
    print('Positional Argument : ',Result)
    Result= Full_Name('Other','Vasanth','Rajendran')
    print('Positional Argument exchange : ',Result)
    Result = Full_Name(LastName='Rajendran',FirstName='Vasanth')
    print('keyword Argument : ',Result)
    Result = Full_Name(NAtionality='Other',LastName='Rajendran',FirstName='Vasanth')
    print('keyword Argument : ',Result)
    
if __name__ == '__main__':
    main()