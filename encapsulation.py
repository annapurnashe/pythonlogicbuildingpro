#encapsulation is process of hiding the confidencial information //


class person:
    def __init__(self,name):
        self.name=name
        print(f"Hello,my name is {self.name}.")

    def __del__(self):
        print(f"Goodbye from {self.name}.")

p=person("Alice")
del p

