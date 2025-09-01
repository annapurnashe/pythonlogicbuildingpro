try:
    a=input("enter the value of a")
    b=input("enter the value of b")

    x=float(a)
    y=float(b)
    z=x/y
except(ZeroDivisionError):
    print("don't enter the 0 and symbol")
else:
    print("value of x=",x)
    print("value of y=",y)
    print("div=",z)