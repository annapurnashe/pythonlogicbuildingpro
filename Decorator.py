#Decorator is function which will provide additional functionality to normal function.


def decorator(func):
    def wrapper():
        print("something is happend before")
        func()
        print("something after calling fun")

    return wrapper
@decorator
def hello():
    print("hello")

hello()
