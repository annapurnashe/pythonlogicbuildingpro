#Decorator is function which will provide additional functionality to normal function.

def decorator(func):
    def disply():
        print("something is happend before")
        func()
        print("something after calling fun")

    return disply()
@decorator
def hello():
    print("hello")
