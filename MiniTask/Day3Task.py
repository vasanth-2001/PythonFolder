def AreaOfCircle(radius,pi=3.14):
    result=pi*radius**2
    return result

def main():

    print("Area of circle using positional :",AreaOfCircle(10,3.15))
    print("Area of circle using Default :",AreaOfCircle(10))
    print("Area of circle using Keyword :",AreaOfCircle(radius=10,pi=3.16))
    print("Area of circle using Keyword and Default :",AreaOfCircle(radius=20))


if __name__ == '__main__':
    main()